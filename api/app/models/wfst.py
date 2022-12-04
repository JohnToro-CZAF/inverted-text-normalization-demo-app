from nemo_text_processing.inverse_text_normalization.inverse_normalize import InverseNormalizer
from .base import Model

class WFSTITNModel(Model):
  def __init__(self):
    self.model = InverseNormalizer(lang='en')

  def infer(self, text):
    return self.model.inverse_normalize(text, verbose=True)