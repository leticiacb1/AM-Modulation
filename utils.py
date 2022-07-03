from scipy import signal as sg
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window

import sounddevice as sd
import soundfile as sf

import time
import sys

from settings import *

#####################
  # Filtro
#####################

def filtro(y, samplerate, cutoff_hz):
  # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
  nyq_rate = samplerate/2
  width = 5.0/nyq_rate
  ripple_db = 60.0 #dB
  N , beta = sg.kaiserord(ripple_db, width)
  taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
  yFiltrado = sg.lfilter(taps, 1.0, y)
  return yFiltrado

def LPF(signal, cutoff_hz, fs):
  # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
  nyq_rate = fs/2
  width = 5.0/nyq_rate
  ripple_db = 60.0 #dB
  N , beta = sg.kaiserord(ripple_db, width)
  taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
  return( sg.lfilter(taps, 1.0, signal))

#####################
  # Fourier
#####################
def calcFFT(signal, fs):
  N  = len(signal)                                                 # N = Number of points in the output window. (sample)
  W = window.hamming(N)                                            # W = The window, with the maximum value normalized to 1.         
  T  = 1/fs                                                        # T = 1/taxa de amostragem = s/amostras --> 1 amostra é transmitida em x segundos
  xf = np.linspace(0.0, 1.0/(2.0*T), N//2)                         
  yf = fft(signal*W)
  return(xf, np.abs(yf[0:N//2]))

def plotFFT(signal, fs, title, numberSubplots, numCol, encoder = False, xlim  =False, noXlim = False):
  x,y = calcFFT(signal, fs)
  
  # plt.figure(figsize=(15,12))
  plt.subplot(1,numCol,numberSubplots)
  plt.title(title)
  plt.plot(x, np.abs(y))
  plt.xlabel('Frequencia')
  plt.ylabel("Amplitude")
  plt.ylim(0,350)
  plt.grid(True)
  
  if(xlim and not noXlim):
    plt.xlim(0,5000)
  elif(not noXlim):
    plt.xlim(10000, 16000)

#########################
  # Funções de uso geral
#########################

def playAudio(audio):
  print("     >> REPRODUZINDO AUDIO")
  sd.play(audio)
  sd.wait()

def selectOption():
  option = input('     >> Digite opcao desejada:\t')

  return option

def warning():
  for i in range(5,-1,-1):
    print("     >> A gravação começará em: {} s".format(i), end='\r')
    sys.stdout.flush()
    time.sleep(1)

def recording():

  print("     >> INICIANDO GRAVACAO           ")
  audio_modularizedted = sd.rec(int(DURATION*FS))
  sd.wait()
  print("     >> FIM DE TRANSMISSAO           ")

  return audio_modularizedted

def generateCarrier(signal):
  sample = len(signal)
  duration = len(signal) / FS
  
  list_time = np.linspace(0, duration, sample) 
  carrier  = 1*np.sin(2 * np.pi * FREQ_CARRIER * list_time)

  return list_time, carrier

def modularization(carrier, audio_filtred):
  return carrier*audio_filtred

def filter(signal):
    audio_filtred = filtro(signal, FS, FREQ_CUTOFF)

    print("     >> AUDIO FILTRADO:           ")
    return audio_filtred

########################
  # Prints no terminal
########################

class Display():
  def __init__(self, tipo):
      self.tipo = tipo

  def showOptions(self):
      print('\n')
      print("     ------------------------------")
      print("     -------- SELECT OPTION -------")
      print("     ------------------------------")
      print('\n')

      print('     (1) Gravar um audio (Até 5s)')
      print('     ------------------------------')
      if(self.tipo == 'ENCODER'):
        print('     (2) Enviar existente')
      else:
        print('     (2) Ler arquivo existente')
      print('     ------------------------------')
      print()

  def text(self, text):
    print('\n')
    print("     ------------------------------")
    print(f"            {text}                  ")
    print("     ------------------------------")
    print('\n')

  
  def tecla(self, key):
      if(self.tipo == 'ENCODER'):
          print('\n')
          print("     ----------------------------------")
          print(f"         GERANDO SOM DA TECLA : {key}") 
          print("     ----------------------------------")
          print('\n')
      else:
          print('\n')
          print("     ---------------------------------")
          print(f"           TECLA PRESSIONADA : {key} ")
          print("     ---------------------------------")
          print('\n')

