import collections

import yaml

class Config:
    def __init__(self, path, entries):
        self.__dict__ = entries
        self.path = path

    @staticmethod
    def load(path):
        with open(path) as configFile:
            data = yaml.load(configFile, Loader=SafeLoader)
            return Config(path, data)

    def save(self, path=""):
        if path is "":
            path = self.path
        with open(path, 'w') as out:
            yaml.dump(self.__dict__, out, Dumper=SafeDumper)

def construct_yaml_map(self, node):
    data = collections.OrderedDict()
    yield data
    value = self.construct_mapping(node)
    data.update(value)

def construct_mapping(self, node, deep=False):
    if isinstance(node, yaml.MappingNode):
        self.flatten_mapping(node)
    else:
        msg = 'expected a mapping node, but found %s' % node.id
        raise yaml.constructor.ConstructError(None,
                                              None,
                                              msg,
                                              node.start_mark)

    mapping = collections.OrderedDict()
    for key_node, value_node in node.value:
        key = self.construct_object(key_node, deep=deep)
        try:
            hash(key)
        except TypeError as err:
            raise yaml.constructor.ConstructError(
                'while constructing a mapping', node.start_mark,
                'found unacceptable key (%s)' % err, key_node.start_mark)
        value = self.construct_object(value_node, deep=deep)
        mapping[key] = value
    return mapping

class Loader(yaml.Loader):
    def __init__(self, *args, **kwargs):
        yaml.Loader.__init__(self, *args, **kwargs)

        self.add_constructor(
            'tag:yaml.org,2002:map', type(self).construct_yaml_map)
        self.add_constructor(
            'tag:yaml.org,2002:omap', type(self).construct_yaml_map)

    construct_yaml_map = construct_yaml_map
    construct_mapping = construct_mapping

class SafeLoader(yaml.SafeLoader):
    def __init__(self, *args, **kwargs):
        yaml.SafeLoader.__init__(self, *args, **kwargs)

        self.add_constructor(
            'tag:yaml.org,2002:map', type(self).construct_yaml_map)
        self.add_constructor(
            'tag:yaml.org,2002:omap', type(self).construct_yaml_map)

    construct_yaml_map = construct_yaml_map
    construct_mapping = construct_mapping

def represent_ordereddict(self, data):
    return self.represent_mapping('tag:yaml.org,2002:map', data.items())

class Dumper(yaml.Dumper):
    def __init__(self, *args, **kwargs):
        yaml.Dumper.__init__(self, *args, **kwargs)
        self.add_representer(collections.OrderedDict, type(self).represent_ordereddict)

    represent_ordereddict = represent_ordereddict

class SafeDumper(yaml.SafeDumper):
    def __init__(self, *args, **kwargs):
        yaml.SafeDumper.__init__(self, *args, **kwargs)
        self.add_representer(collections.OrderedDict, type(self).represent_ordereddict)

    represent_ordereddict = represent_ordereddict
