from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger
from pathlib import Path

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager(
            config_filepath=Path("/Users/vanisuryavanshi/Text-Summarizer/config/config.yaml"),
            params_filepath=Path("/Users/vanisuryavanshi/Text-Summarizer/params.yaml")
        )
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.convert()