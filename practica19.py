'''
Practica 19
Generar un programa que obtenga una señal de audio mediante el micrófono o un archivo de audio (mp3, wav, etc) y 
permitir al usuario seleccionar el intervalo de frecuencias que desea escuchar, esto es, 
aplicar un filtro en un cierto intervalo de frecuencias, permitir escuchar el resultado y guardar el resultado en un archivo
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import math
import contextlib

fname = 'test.wav'
outname = 'filtered.wav'

cutOffFrequency = 400.0


def running_mean(x, windowSize):
 cumsum = np.cumsum(np.insert(x, 0, 0))
 return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize


def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

 if sample_width == 1:
  dtype = np.uint8 
 elif sample_width == 2:
  dtype = np.int16 
 else:
  raise ValueError("Only supports 8 and 16 bit audio formats.")

  channels = np.fromstring(raw_bytes, dtype=dtype)

 if interleaved:

  channels.shape = (n_frames, n_channels)
  channels = channels.T
 else:

  channels.shape = (n_channels, n_frames)

 return channels

 with contextlib.closing(wave.open(fname,'rb')) as spf:
  sampleRate = spf.getframerate()
  ampWidth = spf.getsampwidth()
  nChannels = spf.getnchannels()
  nFrames = spf.getnframes()

# Extraemos audios
  signal = spf.readframes(nFrames*nChannels)
  spf.close()
  channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)


  freqRatio = (cutOffFrequency/sampleRate)
  N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)


  filtered = running_mean(channels[0], N).astype(channels.dtype)

  wav_file = wave.open(outname, "w")
  wav_file.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
  wav_file.writeframes(filtered.tobytes('C'))
  wav_file.close()