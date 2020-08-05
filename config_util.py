import configparser
from collections import defaultdict


class SingletonMetaClass(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance"):
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class ConfigUtil(metaclass=SingletonMetaClass):
    """
    配置文件读取工具类
    """
    def __init__(self, file_paths: list):
        """
        根据提供的配置文件路径列表，实例化配置文件对象
        :param file_paths: [("config_key": "path"),]
        """
        self.config_container = defaultdict(dict)
        for item in file_paths:
            if isinstance(item, tuple):
                config = configparser.ConfigParser()
                config.read(item[1])
                self.config_container[item[0]] = config

    def get_config(self, config_key, section, key):
        if config_key not in self.config_container:
            raise Exception(f"没有找到key为{config_key}的配置文件")

        if section not in self.config_container[config_key]:
            raise Exception(f"配置文件[{config_key}]中没有找到{section}的分组")

        if key not in self.config_container[config_key][section]:
            raise Exception(f"配置文件[{config_key}]中没有找到{key}的配置")

        return self.config_container[config_key][section][key]
