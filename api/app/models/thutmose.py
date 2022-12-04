from nemo.collections import nlp as nemo_nlp
from nemo.collections.nlp.data.text_normalization_as_tagging.utils import spoken_preprocessing
from .base import Model

class ThutmoseITNModel(Model):
  def __init__(self):
    self.model = nemo_nlp.models.ThutmoseTaggerModel.from_pretrained('itn_en_thutmose_bert')

  def infer(self, text):
    # The code is from NeMo reposistory.
    lines = [text]
    batch, all_preds = [], []
    for i, line in enumerate(lines):
        s = spoken_preprocessing(line)  # this is the same input transformation as in corpus preparation.
        batch.append(s.strip())
    outputs = self.model._infer(batch)
    for x in outputs:
        all_preds.append(x)

    if len(all_preds) != len(lines):
        raise ValueError(
            "number of input lines and predictions is different: predictions="
            + str(len(all_preds))
            + "; lines="
            + str(len(lines))
        )

    for i in range(len(all_preds)):
      all_preds[i] = all_preds[i].split('\t')[0].strip()
    return all_preds[0]