# create inverse text normalization instance
from .models.t5 import T5ITNModel
from .models.thutmose import ThutmoseITNModel
from .models.wfst import WFSTITNModel
from omegaconf import DictConfig, OmegaConf

cfg_t5 = OmegaConf.load('app/models/conf/t5.yaml')

# Initializing all the models first.
model_thutmose = ThutmoseITNModel()
model_wfst = WFSTITNModel()
model_t5 = T5ITNModel(cfg_t5)

def get_model(model_type='thutmose'):
  if model_type == 'thutmose':
    return model_thutmose
  elif model_type == 'wfst':
    return model_wfst
  elif model_type == 't5':
    return model_t5
  else:
    raise ValueError('Invalid model type')