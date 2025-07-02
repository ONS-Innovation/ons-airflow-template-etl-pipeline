def transform_data(data):
    """
    Transforms the extracted data by applying necessary transformations.

    Args:
        data (list): A list of dictionaries representing the extracted data.

    Returns:
        list: A list of transformed data.
    """
    # Example transformation: multiply 'value' by 2
    return [{"id": item["id"], "value": item["value"] * 2} for item in data]
