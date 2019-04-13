import numpy as np
import scipy
import matplotlib
import scipy.io.wavfile as wav
import matplotlib.pyplot as plotFunction
from scipy.fftpack import fft as fourier
from scipy.fftpack import ifft as inverseFourier 
from scipy.fftpack import fftfreq as frequency

# Se lee el archivo de audio handel y se guarda
# fs es la frecuencia
# data es el valor de la amplitudes
(fs, data) = wav.read('handel.wav')

# Se genera los valores de tiempo entre cada amplitud
ejeX = np.linspace(0, len(data)/fs, num=len(data))

# Se realiza grafico amplitud vs tiempo
plotFunction.figure("Amplitud en el tiempo Original", [7.3, 4.5])
plotFunction.title('Grafico del audio original en el tiempo')
plotFunction.ylabel('Amplitud')
plotFunction.xlabel('Tiempo (s)')
plotFunction.plot(ejeX, data)
#plotFunction.show()

# Calculo de la tranformada de fourier
fourierTransform = fourier(data)

# Calculo de las frecuencias (Eje X)
freqs = frequency(len(data))

# Calculo de la inversa de la transformada
inverseFourierTransform = inverseFourier(fourierTransform)

# Se grafica la transformada de fourier
plotFunction.figure("Transformada de Fourier", [7.0, 4.9])
plotFunction.xlabel('Frecuencia (Hzc)')
plotFunction.ylabel('F(w)')
plotFunction.title('Grafico en el dominio de la frecuencia')
plotFunction.plot(freqs, fourierTransform)
#plotFunction.show()

# Se grafica la inversa de la transformada
plotFunction.figure("Inversa de la Transformada", [7.2, 4.5])
plotFunction.plot(ejeX, inverseFourierTransform)
plotFunction.title('Grafico del audio inverso en el tiempo')
plotFunction.ylabel('Amplitud')
plotFunction.xlabel('Tiempo (s)')

# Cambio a formato de 16 bits
inverseFourierTransform = np.asarray(inverseFourierTransform, dtype=np.int16)

# Guardar archivo de la tranformada inversa
wav.write('inverse-handel.wav', fs, inverseFourierTransform)

#Se muestran los graficos
plotFunction.show()