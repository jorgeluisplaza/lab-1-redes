import numpy as np
import scipy
import matplotlib
import scipy.io.wavfile as wav
import matplotlib.pyplot as plotFunction
from scipy.fftpack import fft as fourier
from scipy.fftpack import ifft as inverseFourier 

# Se lee el archivo de audio handel y se guarda
# fs es la frecuencia
# data es el valor de la amplitudes
(fs, data) = wav.read('handel.wav')

# Se genera los valores de las amplitudes en el tiempo
ejeX = np.linspace(0, len(data)/fs, num=len(data))

# Se realiza grafico amplitud vs tiempo
plotFunction.title('Grafico del audio en el tiempo')
plotFunction.ylabel('Amplitud')
plotFunction.xlabel('Tiempo (s)')
plotFunction.plot(ejeX, data)
plotFunction.show()

#Calculo de la tranformada de fourier
fourierTransform = fourier(data)

#Calculo de la inversa de la transformada
inverseFourierTransform = inverseFourier(fourierTransform)

# Se grafica la transformada de fourier
plotFunction.ylabel('frecuencia (w)')
plotFunction.xlabel('Tiempo (s)')
plotFunction.title('Grafico en el dominio de la frecuencia')
plotFunction.plot(ejeX, fourierTransform)
plotFunction.show()

#Se grafica la inversa de la transformada
plotFunction.plot(ejeX, inverseFourierTransform)
plotFunction.title('Grafico del audio en el tiempo')
plotFunction.ylabel('Amplitud')
plotFunction.xlabel('Tiempo (s)')
plotFunction.show()

# Cambio a formato de 16 bits
inverseFourierTransform = np.asarray(inverseFourierTransform, dtype=np.int16)

# Guardar archivo de la tranformada inversa
wav.write('inverse-handel.wav', fs, inverseFourierTransform)