import logging
import os
import pathlib
import sys
from datetime import datetime

import pdfkit
from flask import (Flask, make_response, render_template, request,
                   send_from_directory)

import resume
import utils

# # Logging config

# Get the log level from our environment variables, or set a default.

if os.getenv('LOG_LEVEL') is not None:
    level = logging.getLevelName(os.getenv('LOG_LEVEL'))
else:
    level = logging.getLevelName('INFO')

# Declare our log format
Log_Format = "%(levelname)s %(asctime)s - %(message)s"

# Set up a basic logging config for Python to send everything to stdout
logging.basicConfig(stream=sys.stdout, level=level)

# Set up the logging config for the waitress WSGI component
waitress_logger = logging.getLogger('waitress')
waitress_logger.setLevel(level)

# Declare our default logger
logger = logging.getLogger()

# Announce startup (and log level)!
logger.info(f"STARTING! Log level is {logging.getLevelName(logger.getEffectiveLevel())}")

# # End logging config

# Get the current year to plug into some of our templates
current_year = datetime.today().year

# Create a Flask object for the application
app = Flask(__name__, static_folder='static')


@app.route('/favicon.ico')
def favicon():
    """
    Favicon endpoint, primarily meant for situations where the favicon isn't picked up from HTML properly
    and the browser looks at /favicon.ico instead.

    Args:
        None

    Returns:
        The favicon image

    Raises:
        None
    """
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/x-icon')


@app.route('/')
def root():
    """
    The main page!

    Args:
        None

    Returns:
        A HTML page, showing a resume.

    Raises:
        None
    """
    rendered_template = render_template('index.html', resume=resume.get_resume(), environ=os.environ, current_year=current_year)
    template_with_auto_links = utils.auto_link(rendered_template, resume.link_list)
    return template_with_auto_links


@app.route('/robots.txt')
def robots_txt():
    """
    Serves a static robots.txt file for SEO

    Args:
        None

    Returns:
        robots.txt

    Raises:
        None
    """
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt', mimetype='text/plain')


@app.route('/about')
def about():
    """
    The about page.

    Args:
        None

    Returns:
        A HTML page, showing the architecture and design of this site. Very meta.

    Raises:
        None
    """
    rendered_template = render_template('about.html', resume=resume.get_resume(), environ=os.environ, current_year=current_year)
    return rendered_template


@app.route('/pdf')
def pdf_gen():
    """
    An endpoint that returns a download of the resume site in PDF format.

    Originally, I intended to have a link on the main resume page that returns a copy of the resume
    in PDF form, but unfortunately the rendering from pdfkit/wkhtmltopdf just doesn't look right, and
    it seems to be a limitation of those libraries. So, there's no link on the resume page for that anymore.
    However, /pdf will remain available as-is, just to show the extent that I've managed to get that to work.
    If you're curious and looking at this source, feel free to hit that endpoint. If you actually want a PDF
    copy, just save as PDF from your browser :)

    Args:
        None

    Returns:
        A PDF file download.

    Raises:
        500 error code in the event the PDF build process fails.
    """

    # Set the working_dir variable, which amounts to the path the script is running from
    working_dir = pathlib.Path(__file__).parent.resolve()
    # Render the HTML template, including that working_dir value, which changes some variables to reference local files
    resume_html = render_template('index.html', resume=resume.get_resume(), working_dir=str(working_dir), environ=os.environ, current_year=current_year)
    # Output the generated HTML to stdout for debugging
    logger.debug("PDF HTML: \n" + resume_html)
    # Generate PDF
    try:
        # Allow pdfkit to access local files
        pdf_options = {
            'enable-local-file-access': None,
            'javascript-delay': "1000"
        }
        # Generate PDF file from HTML data
        pdf_data = pdfkit.from_string(resume_html, options=pdf_options)
        # Build a response for Flask to reply with
        response = make_response(pdf_data)
        # We're returning a PDF, so we need to set the MIME type appropriately
        response.headers['Content-Type'] = 'application/pdf'
    except Exception as e:
        # If something above has failed, log that error
        logger.error(e)
        # Create a new response with a simple error message
        response = make_response("Error generating PDF")
        # Set the HTTP response code to 500
        response.status_code = 500
        # Return the error response to Flask
        return response
    # Return the PDF download
    return response


@app.route("/ping")
def ping_page():
    """
    A ping/pong utility endpoint for monitoring purposes.

    Args:
        None

    Returns:
        "pong"

    Raises:
        None
    """
    return "pong"


@app.route("/health")
def health():
    """
    A health checking endpoint for monitoring purposes.

    Args:
        None

    Returns:
        HTTP 200 "success" page if loading the resume data is working as expected

    Raises:
        HTTP 500 error if loading the resume data does not work
    """
    try:
        # Try to load the resume data
        resume.get_resume()
        # Build a response for Flask to reply with. All we need to do is send a "success" string.
        response = make_response("success")
    except Exception as e:
        # If something above has failed, log that error
        logger.error(e)
        # Create a new response with a simple error message. If we want to find more error info, we should look at the logs.
        response = make_response("Error loading resume data.")
        # Set the HTTP response code to 500
        response.status_code = 500
        # Return the error response to Flask
        return response
    # Return the successful response
    return response


# Lines below this are to add request/reply information to our logs
@app.before_request
def before_request():
    now = datetime.now()
    timestamp = now.strftime('[%Y-%b-%d %H:%M]')
    logger.info('%s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path)


@app.after_request
def after_request(response):
    now = datetime.now()
    timestamp = now.strftime('[%Y-%b-%d %H:%M]')
    logger.info('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response
