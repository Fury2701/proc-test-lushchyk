def validate(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Input must be a non-empty list")
    return True
