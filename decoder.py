#Importe todas as bibliotecas
from scipy.io.wavfile import write

import sounddevice as sd
import soundfile as sf

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

from settings import *
from utils import *

def readAudio(option):

    if(option == '1'):

        warning()
        audio = recording()

        filename = "audio/decoder/recoder.wav"
        write(filename = filename, rate = FS, data = audio)
        audio = audio[:,0]

    elif(option == '2'):
        filename = 'audio/encoder/audioModNorma.wav'
        audio, _ = sf.read(filename)

    return audio

def plotgraphics(list_time, audio_mod, audio_demod, audio_filtred):
    plt.figure(figsize=(35,12))
    plotFFT(signal=audio_mod, fs=FS, title="FourierAudioModularRecebido", numberSubplots=1, numCol=3)
    plotFFT(signal=audio_demod, fs=FS, title="FourierAudioDEMOD", noXlim = True, numberSubplots=2, numCol=3)
    plotFFT(signal=audio_filtred, fs=FS, title="FourierAudioFiltredRecebido", noXlim = True, numberSubplots=3, numCol=3)
    plt.savefig('graphics/decoder/FourierDecoder.png')

def startDecoder():

    # Configurações
    sd.default.samplerate = FS   
    sd.default.channels = 1

    display = Display('DECODER')

    # Opcao de programa:
    display.showOptions()
    option = selectOption()
    
    # Sinal modulado recebido:
    display.text(text = 'INICIA DECODER')
    audio_mod = readAudio(option)
    playAudio(audio_mod)

    # Gera portadora:
    display.text(text = 'GERA PORTADORA')
    list_time , carrier = generateCarrier(audio_mod)

    # Desmodulação sinal recebido:
    display.text(text = 'DESMODULARIZADO ...')
    audio_demod = modularization(carrier,audio_mod)
    playAudio(audio_demod)

    # Filtra frequencias acima de 2500Hz:
    display.text(text = 'INICIA FILTRAGEM')
    audio_filtred = filter(audio_demod)

    display.text(text = 'AUDIO RECEBIDO')
    playAudio(audio_filtred)

    # Plotando gráficos:
    display.text(text = 'GERA GRÁFICOS ...')
    plotgraphics(list_time, audio_mod, audio_demod, audio_filtred)

    # Finalizando
    display.text(text = '  FINALIZANDO')

if __name__ == "__main__":
    startDecoder()