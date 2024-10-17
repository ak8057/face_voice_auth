import librosa
import numpy as np

def extract_features(file_name):
    y, sr = librosa.load(file_name)
    y = librosa.util.normalize(y)  
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40) 
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    mel = librosa.feature.melspectrogram(y=y, sr=sr)

    mfcc_mean = np.mean(mfcc.T, axis=0)
    mfcc_std = np.std(mfcc.T, axis=0)
    chroma_mean = np.mean(chroma.T, axis=0)
    chroma_std = np.std(chroma.T, axis=0)
    mel_mean = np.mean(mel.T, axis=0)
    mel_std = np.std(mel.T, axis=0)

    return np.hstack((mfcc_mean, mfcc_std, chroma_mean, chroma_std, mel_mean, mel_std))
