"""
File: predict.py 
-------------------
This file contains a useful function that takes in a
raw audio waveform and returns a Numpy ndarray that can be
inputted into the trained model. 
"""

def get_prediction_array(audio_file): 
	y, sr = librosa.load(audio_file)
    time = np.arange(0, len(y)) / sr
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                    fmax=8000)
    return S


def get_entire_prediction(audio_file, model_name):
	"""
	Takes in an audio file and a model and returns
	the model's prediction of that audio file. 
	"""
	mel_spec = get_prediction_array(audio_file)
	model_name.predict(mel_spec)