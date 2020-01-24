import os
from pocketsphinx import LiveSpeech

model_path = "isolated_words_spa"

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, "words1.cd_semi_200"),
    lm=os.path.join(model_path, 'words1.lm.DMP'),
    dic=os.path.join(model_path, 'words1.dic')
)

for phrase in speech:
    print(phrase)
