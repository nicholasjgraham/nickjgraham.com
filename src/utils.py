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
        data = data.replace(key, f"<a href=\"{value}\">{key}</a>", 1)
    # Return the updated data
    return data
