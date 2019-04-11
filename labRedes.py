import numpy as np
import scipy
import matplotlib
import scipy.io.wavfile as wav
import matplotlib.pyplot as graficar

(fs, data) = wav.read('/home/diinf/Escritorio/handel.wav')

ejeX = np.linspace(0, len(data)/fs, num=len(data))

graficar.title('Grafico bonito 1.1')
graficar.plot(ejeX, data)
graficar.show()