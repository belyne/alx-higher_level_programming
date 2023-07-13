#!/usr/bin/python3
def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization."""
    if isinstance(obj, dict):
        return {k: class_to_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, bool):
        return obj
    else:
        attributes = {}
        for attr in dir(obj):
            if not attr.startswith('__'):
                value = getattr(obj, attr)
                if not callable(value):
                    attributes[attr] = class_to_json(value)
        return attributes
