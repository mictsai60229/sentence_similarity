from typing import List
import json
import torch
import os
import numpy as np
from allennlp.models.archival import load_archive
from allennlp.predictors import DecomposableAttentionPredictor, Predictor
from allennlp.common.checks import check_for_gpu
from allennlp.data.tokenizers import WordTokenizer



FILE_PATH = os.path.dirname(__file__)
PREDICT_MODEL_NAME = os.path.join(FILE_PATH, "esim_character", "model.tar.gz")

def GetPredictor(archive: str) -> Predictor:
    check_for_gpu(1)
    archive = load_archive(archive, cuda_device=1)
    return DecomposableAttentionPredictor.from_archive(archive, predictor_name='textual-entailment')


predictor =  GetPredictor(PREDICT_MODEL_NAME)
'''
label = predictor._model.vocab._index_to_token["labels"]
label is {0: 'entailment', 1: 'contradiction', 2: 'neutral'}

usage
predictor.predict(
  hypothesis=sentence1,
  premise=sentence2
)

Sentence should be sepearte by whitespace for each chinese character and english word.
example: 
'以 假 亂 真 → Virtual Reality 虛 擬 實 境 ( 利 用 穿 戴 式 裝 置 及 感 測 元 件 去 模 擬 雲 在 虛 擬 環 境 的 動 作 ) 寶 可 夢 → 擴 增 實 境 ( Augment Reality ) ( 將 虛 擬 的 物 件 投 影 至 現 實 的 環 境 中 ) VR 利 用 穿 戴 裝 置 ，'

'''