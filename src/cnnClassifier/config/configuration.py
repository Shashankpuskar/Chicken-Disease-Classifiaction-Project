from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig
from box import ConfigBox

# This code contains some error which will be resolved later
# class ConfigurationManager:
#     def __init__(self,
#                 config_filepath = CONFIG_FILE_PATH,
#                 params_filepath = PARAMS_FILE_PATH):
        
#         self.config = config_filepath
#         self.params = params_filepath
        
#         create_directories([self.config.artifacts_root])
        
        
#     def get_data_ingestion_config(self) -> DataIngestionConfig:
#         config = self.config.data_ingestion
        
#         create_directories([config.root_dir])
        
#         data_ingestion_config = DataIngestionConfig(
#             root_dir=config.root_dir,
#             source_URL=config.source_URL,
#             local_data_file=config.local_data_file,
#             unzip_dir=config.unzip_dir
#         )
        
#         return data_ingestion_config

# This is corrected code
class ConfigurationManager:
    def __init__(self, 
                 config_filepath: Path = CONFIG_FILE_PATH, 
                 params_filepath: Path = PARAMS_FILE_PATH):
        
        # Ensure config_filepath is a Path object
        self.config_filepath = Path(config_filepath)

        # Read and parse the YAML file
        self.config = self.read_yaml(self.config_filepath)
        self.params = params_filepath  # Handle params similarly if needed

        # Ensure artifacts_root exists before creating directories
        if hasattr(self.config, "artifacts_root"):
            create_directories([self.config.artifacts_root])
        else:
            raise AttributeError("Missing 'artifacts_root' in config file")
        
    @staticmethod
    def read_yaml(path_to_yaml: Path) -> ConfigBox:
        """Reads a YAML file and returns a ConfigBox object."""
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file) or {}
        return ConfigBox(content)  # Allows dot notation access
        
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
            artifacts_root=self.config.artifacts_root
        )
        
        return data_ingestion_config