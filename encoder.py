from settings import *
from utils import *

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
import time

import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write


def readAudio(option):

    if(option == '1'):
        warning()
        audio = recording()
        audio = audio[:,0]

        filename = "audio/encoder/myrecording.wav"
        write(filename = filename, rate = FS, data = audio)

    elif(option == '2'):
        file_name = 'audio/encoder/audio5s.wav'
        audio, _ = sf.read(file_name)

        audio = audio[:,1]

    return audio
    
def normalize(audio_mod):
    max_value_audio = np.max(abs(audio_mod))
    audio_normalize = audio_mod/max_value_audio

    filename = "audio/encoder/audioModNorma.wav"
    write(filename = filename, rate = FS, data = audio_normalize)
    return audio_normalize
    
def plotgraphics(list_time, audio_original, audio_filtred, audio_mod):
    plt.figure(figsize=(15,12))
    graphicTime(list_time, [audio_original,audio_filtred,audio_mod], ["Audio Original","Audio Filtrado","Audio Modulado"])
    plotFFT(  signal=audio_original, fs=FS, title="FourierAudioOriginal", encoder=True, xlim = True, numberSubplots=1, numCol=2)
    plotFFT(  signal= audio_mod, fs=FS, title="FourierAudioNormalizado", encoder=True, numberSubplots=2, numCol=2)
    plt.savefig('graphics/encoder/FourierEncoder.png')

def graphicTime(list_time, list_y, list_title):
    plt.figure(figsize=(35,12))

    for i in range(0,3):
        plt.subplot(1,3,i+1)
        plt.plot(list_time,list_y[i])
        plt.title(list_title[i])
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid(True)
    
    plt.savefig("graphics/encoder/TimeDomain.png")

def readAudioforDecoder(audio_norm):
    for i in range(5,-1,-1):
            print("     >> A reprodução começará em: {} s".format(i), end='\r')
            sys.stdout.flush()
            time.sleep(1)
    print()     
    playAudio(audio_norm)

def startEncoder():

    # Configurações
    sd.default.samplerate = FS   
    sd.default.channels = 1
    display = Display('ENCODER')

    # Opcao de programa:
    display.showOptions()
    option = selectOption()
    
    # Sinal que sera transmitido:
    display.text(text = 'INICIA ENCODER')
    audio = readAudio(option)
    playAudio(audio)

    # Filtra sinal e reproduz sinal filtrado:
    display.text(text = 'INICIA FILTRAGEM')
    audio_filtred = filter(audio)
    playAudio(audio_filtred)

    # Gera portadora:
    display.text(text = 'GERA PORTADORA')
    list_time , carrier = generateCarrier(audio_filtred)

    # Modularizando sinal:
    display.text(text = 'MODULARIZANDO ...')
    audio_mod = modularization(carrier, audio_filtred)
    
    # Normalizando sinal:
    display.text(text = 'NORMALIZANDO ...')
    audio_norm = normalize(audio_mod)
    playAudio(audio_norm)

    # Plotando gráficos:
    display.text(text = 'GERA GRÁFICOS ...')
    plotgraphics(list_time, audio, audio_filtred, audio_mod)

    # Reproduzindo audio para decoder:
    display.text(text = 'PARA DECODER ...')
    readAudioforDecoder(audio_norm)

    # Finalizando
    display.text(text = '  FINALIZANDO')
        
if __name__ == "__main__":
    startEncoder()