import json
import sys


def get_config():
    path = "{path}/config/default.json".format(path=sys.path[4])
    with open(path) as f:
        config = json.load(f)
        # print(config)
        return config
