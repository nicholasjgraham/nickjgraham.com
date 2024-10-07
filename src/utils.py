import weasyprint
import pathlib
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


# def generate_pdf(html) -> bytes:
#     """
#     Generates a PDF from HTML data.

#     Args:
#         html - A string of HTML data to be converted to PDF.

#     Returns:
#         A PDF file.

#     """
#     # Set pdfkit options
#     pdf_options = {
#         'enable-local-file-access': None,
#         'keep-relative-links': None,
#         'javascript-delay': '1000',
#         'page-width': '1000px',
#         'page-height': '2700px',
#         'margin-bottom': '0px',
#         'margin-left': '0px',
#         'margin-right': '0px',
#         'margin-top': '0px',
#     }
#     # Generate PDF file from HTML data
#     pdf_data = pdfkit.from_string(html, options=pdf_options)
#     return pdf_data


def generate_pdf(html) -> bytes:
    """
    Generates a PDF from HTML data.

    Args:
        html - A string of HTML data to be converted to PDF.

    Returns:
        A PDF file.

    """
    # Generate PDF file from HTML data
    working_dir = pathlib.Path(__file__).parent.resolve()
    html = weasyprint.HTML(string=html)
    css_roboto = weasyprint.CSS(open(f'{working_dir}/static/css/roboto.css'))
    css_idocs = weasyprint.CSS(open(f'{working_dir}/static/css/idocs.stylesheet.css'))
    css_pillar = weasyprint.CSS(open(f'{working_dir}/static/css/pillar-1.css'))
    css_custom = weasyprint.CSS(open(f'{working_dir}/static/css/custom.css'))
    pdf_data = html.write_pdf(stylesheets=[css_roboto, css_idocs, css_pillar, css_custom])
    return pdf_data
