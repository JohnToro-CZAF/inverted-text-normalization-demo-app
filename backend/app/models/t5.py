from nemo_text_processing.text_normalization.data_loader_utils import post_process_punct
from .nn_wfst.electronic.normalize import ElectronicNormalizer
from .nn_wfst.whitelist.normalize import WhitelistNormalizer

from nemo.collections.nlp.data.text_normalization import constants
from nemo.collections.nlp.models import DuplexTextNormalizationModel
from nemo.utils import logging
from omegaconf import DictConfig, OmegaConf

from .helpers import DECODER_MODEL, TAGGER_MODEL, instantiate_model_and_trainer
from .base import Model

class T5ITNModel(Model):
  def __init__(self, cfg: DictConfig) -> str:
    logging.debug(f'Config Params: {OmegaConf.to_yaml(cfg)}')
    self.lang = cfg.lang
    self.tagger_trainer, self.tagger_model = instantiate_model_and_trainer(cfg, TAGGER_MODEL, False)
    self.decoder_trainer, self.decoder_model = instantiate_model_and_trainer(cfg, DECODER_MODEL, False)
    self.decoder_model.max_sequence_len = 512
    self.tagger_model.max_sequence_len = 512
    self.tn_model = DuplexTextNormalizationModel(self.tagger_model, self.decoder_model, self.lang)
    if self.lang == constants.ENGLISH:
      self.normalizer_electronic = ElectronicNormalizer(input_case="cased", lang=self.lang, deterministic=True)
      self.normalizer_whitelist = WhitelistNormalizer(input_case="cased", lang=self.lang, deterministic=True)

  def infer(self, test_input):
    if self.lang == constants.ENGLISH:
      new_input = self.normalizer_electronic.normalize(test_input, verbose=False)
      test_input = post_process_punct(input=test_input, normalized_text=new_input)
      new_input = self.normalizer_whitelist.normalize(test_input, verbose=False)
      test_input = post_process_punct(input=test_input, normalized_text=new_input)
      inputs = []
      directions = []
      inputs.append(test_input)
      directions.append(constants.DIRECTIONS_TO_MODE["itn"])
      output = self.tn_model._infer(inputs, directions)[-1]
      print(output)
      return output[0]
    else:
      raise NotImplementedError