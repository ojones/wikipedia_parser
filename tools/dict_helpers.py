__author__ = 'oswaldjones'


def normalize_dict_keys(data_dict):

    normalized = {}

    if data_dict:
        for key in data_dict:
            normalized[key.lower()] = data_dict[key]

    return normalized


def convert_to_dict(key_value_list):

    converted = {}

    if key_value_list:
        for pair in key_value_list:
            if len(pair) == 2:
                converted[pair[0]] = pair[1]

    return normalize_dict_keys(converted)
