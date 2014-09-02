import yaml

from collections import UserDict

DEFAULT_MARGOT_CONFIG = './etc/margot.yml'


class YAMLConfig(UserDict):
    def __init__(self, yaml_str):
        config_dict = yaml.load(yaml_str)
        UserDict.__init__(self, config_dict)

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            data = f.read()
        return cls(data)


class MargotConfig(YAMLConfig):
    @classmethod
    def from_default_location(cls):
        return cls.from_file(DEFAULT_MARGOT_CONFIG)
