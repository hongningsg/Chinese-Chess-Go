# light-weight version of pytorch_transformers.configuration_utils.PretrainedConfig

import os
import json
import copy
import logging

from model_v2.config import CONFIG_FILE_NAME

logger = logging.getLogger(__name__)


import json

from xiangqi_zero.model.utils.model_config import BasicConfig
from xiangqi_zero.env.common import *


class ModelConfigDualRes(BasicConfig):

    def __init__(self, **kwargs):
        super(ModelConfigDualRes, self).__init__(**kwargs)
        model_config_json = kwargs.get('model_config_json')
        if model_config_json is not None:
            with open(model_config_json, "r", encoding='utf-8') as reader:
                json_config = json.loads(reader.read())
            for key, value in json_config.items():
                self.__dict__[key] = value
        else:
            self.num_res_blocks = kwargs.get('num_res_blocks', 39)  # 19 or 39 in the paper


class BasicConfig(object):

    def __init__(self, **kwargs):
        pass

    def save_config(self, save_directory):
        """ Save a configuration object to the directory `save_directory`, so that it
            can be re-loaded using the :func:`BasicConfig.load_config` class method.
        """
        assert os.path.isdir(save_directory), "Saving path should be a directory where the model and configuration can be saved"

        output_config_file = os.path.join(save_directory, CONFIG_FILE_NAME)

        self.to_json_file(output_config_file)

    @classmethod
    def load_config(cls, load_directory, **kwargs):

        assert os.path.isdir(load_directory)
        input_config_file = os.path.join(load_directory, CONFIG_FILE_NAME)

        # Load config
        config = cls.from_json_file(input_config_file)

        # Update config with kwargs if needed
        to_remove = []
        for key, value in kwargs.items():
            if hasattr(config, key):
                setattr(config, key, value)
                to_remove.append(key)
        for key in to_remove:
            kwargs.pop(key, None)
        logger.info("Model config %s", config)

        return config

    @classmethod
    def from_dict(cls, json_object):
        """Constructs a `Config` from a Python dictionary of parameters."""
        config = cls(vocab_size_or_config_json_file=-1)
        for key, value in json_object.items():
            config.__dict__[key] = value
        return config

    def __repr__(self):
        return str(self.to_json_string())

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @classmethod
    def from_json_file(cls, json_file):
        """Constructs a `BertConfig` from a json file of parameters."""
        with open(json_file, "r", encoding='utf-8') as reader:
            text = reader.read()
        return cls.from_dict(json.loads(text))

    def to_dict(self):
        """Serializes this instance to a Python dictionary."""
        output = copy.deepcopy(self.__dict__)
        return output

    def to_json_string(self):
        """Serializes this instance to a JSON string."""
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"

    def to_json_file(self, json_file_path):
        """ Save this instance to a json file."""
        with open(json_file_path, "w", encoding='utf-8') as writer:
            writer.write(self.to_json_string())
