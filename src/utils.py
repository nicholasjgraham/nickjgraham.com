import base64
import os
import pathlib

import requests
from playwright.sync_api import sync_playwright
import jinja2

# This file contains utility functions that can be used elsewhere in the app.


def auto_link(data: str, link_list: dict) -> str:
    """
    This runs through a string and replaces the first instance of keys from a dict with values of those dicts.
    The intention is to find values like "Google" and replace them with "<a href="https://google.com">Google</a>"

    Args:
        data - A string that should probably be html, but in theory can be anything
        link_list - A dict, where keys are strings that should be replaced in `data`, and values are what should replace them.

    Returns:
        A string with replaced values.

    Raises:
        None
    """
    # Iterate through our dict object
    for key, value in link_list.items():
        # Replace the first instance of the dict key with the replacement value
        data = data.replace(f" {key} ", f" <a href=\"{value}\">{key}</a> ", 1)
        data = data.replace(f" {key},", f" <a href=\"{value}\">{key}</a>,", 1)
        data = data.replace(f"({key})", f"(<a href=\"{value}\">{key}</a>)", 1)
        data = data.replace(f" {key}.", f" <a href=\"{value}\">{key}</a>.", 1)
    # Return the updated data
    return data


def generate_pdf(html) -> bytes:
    """
    Generates a PDF from HTML data.

    Args:
        html - A string of HTML data to be converted to PDF.

    Returns:
        A PDF file.

    """
    # Generate PDF file from HTML data
    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch()
        page = browser.new_page()
        page.set_content(html)
        page.wait_for_load_state()
        pdf_data = page.pdf(scale=0.85, width='1300px', height='3500px', print_background=True)
        browser.close()

    return pdf_data


def generate_latex_pdf(template_filename: str, data: dict) -> bytes:
    """
    Generates a PDF from LaTeX data.

    Args:
        filename - The filename of the LaTeX template to be used.
        data - Data to be inserted into the LaTeX template.

    Returns:
        A PDF file.

    """
    # Set the working_dir variable, which amounts to the path the script is running from
    working_dir = pathlib.Path(__file__).parent.resolve()
    # Load the Jinja template file
    template_loader = jinja2.FileSystemLoader(f"{working_dir}/templates")
    template_env = jinja2.Environment(loader=template_loader, variable_start_string='{+', variable_end_string='+}')
    template = template_env.get_template(template_filename)
    latex = template.render(data)
    # Save the templated LaTeX to a file
    with open(f"{working_dir}/temp.tex", "w") as file:
        file.write(latex)
        file.close()
    # Run 'pdflatex <file.tex>' to generate a PDF
    os.system(f"pdflatex -halt-on-error {working_dir}/temp.tex")
    # Read the PDF file
    with open(f"{working_dir}/temp.pdf", "rb") as file:
        pdf_data = file.read()
        file.close()
    # Delete the temporary files
    os.remove(f"{working_dir}/temp.tex")
    os.remove(f"{working_dir}/temp.pdf")
    # Return the PDF data
    return pdf_data


def load_file(file_path: str) -> str:
    """
    Loads a file from disk or the web and returns the contents as a string.

    Args:
        file_path - A string representing the path to the file to be loaded. This can be a local file path or a URL.

    Returns:
        A string containing the contents of the file.

    Raises:
        FileNotFoundError if the local file is not found.
        requests.exceptions.RequestException if there is an issue with the web request.
    """
    # If the file path starts with http, we assume it's a URL
    if file_path.startswith('http'):
        # Load the file from the web
        data = requests.get(file_path).text
        return data
    else:
        # Open the file and read the contents
        with open(file_path, 'r') as file:
            data = file.read()
        # Close the file
        file.close()
        # Return the data
        return data


def image_base64(file_path: str) -> str:
    """
    Loads an image from disk and returns the base64 encoded string.

    Args:
        file_path - A string representing the path to the file to be loaded.

    Returns:
        A string containing the base64 encoded image.

    Raises:
        FileNotFoundError if the file is not found.
    """
    # Open the file and read the contents
    with open(file_path, 'rb') as file:
        data = file.read()
    # Close the file
    file.close()
    # Return the data
    return base64.b64encode(data).decode('utf-8')
