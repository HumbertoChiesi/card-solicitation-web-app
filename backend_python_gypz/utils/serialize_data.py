import json

from utils.encoder import Encoder


def serialize_data(data, is_list):
    if is_list:
        return json.loads(json.dumps(list(data), cls=Encoder))
    else:
        return json.loads(json.dumps(data, cls=Encoder))
