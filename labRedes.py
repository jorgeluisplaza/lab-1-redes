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
audioTime = np.linspace(0, len(data)/fs, num=len(data))

# Se realiza grafico amplitud vs tiempo
plotFunction.figure("Amplitud en el tiempo Original", [7.3, 4.5])
plotFunction.title('Grafico del audio original en el tiempo')
plotFunction.ylabel('Amplitud')
plotFunction.xlabel('Tiempo (s)')
plotFunction.plot(audioTime, data)
#plotFunction.show()

# Calculo de la tranformada de fourier
fourierTransform = fourier(data)

# Calculo de las frecuencias (Eje X)
freqs = frequency(len(data))

# Calculo de la inversa de la transformada
inverseFourierTransform = inverseFourier(fourierTransform)

# Se grafica la transformada de fourier
plotFunction.figure("Transformada de Fourier", [7.0, 4.9])
plotFunction.ylim([0, max(fourierTransform) + 10000000])
plotFunction.xlim([0, max(freqs)])
plotFunction.xlabel('Frecuencia (Hz)')
plotFunction.ylabel('F(w)')
plotFunction.title('Grafico en el dominio de la frecuencia')
plotFunction.plot(freqs, fourierTransform)
#plotFunction.show()

#print(freqs.sort())

# Se grafica la inversa de la transformada
plotFunction.figure("Inversa de la Transformada", [7.2, 4.5])
plotFunction.plot(audioTime, inverseFourierTransform)
plotFunction.title('Grafico del audio inverso en el tiempo')
plotFunction.ylabel('Amplitud')
plotFunction.xlabel('Tiempo (s)')

# Cambio a formato de 16 bits
inverseFourierTransform = np.asarray(inverseFourierTransform, dtype=np.int16)

# Guardar archivo de la tranformada inversa
wav.write('inverse-handel.wav', fs, inverseFourierTransform)

#Funcion que trunca un valor con respecto a un porcentaje
def truncate(value, percent):
	return value - percent * value

#Se copia la lista de frecuencias
freqsAux = freqs.copy()

#Se copia la lista de la transformada
fourierTransformAux = fourierTransform.copy()

#Se ordena de menor a mayor
fourierTransformAux.sort()

#Se obtiene el valor maximo
maxValue = fourierTransformAux[-1]

#Para obtener el segundo peak alto del grafico
secondPeakValue = 0

#Se recorre las frecuencias
for index, i in enumerate(freqsAux):
	#Se mira entre los valores 0.1 y 0.2 (Donde se encuentra el segundo peak)
	if(i > 0.1 and i < 0.2):
		if fourierTransform[index] > secondPeakValue:
			#Se guarda el valor mas alto
			secondPeakValue = fourierTransform[index]

#Se truncan los valores de la transfomada de fourier con respecto a un 75%
#Se guarda en la lista truncateValues
truncatesValues = []
for i in fourierTransform:
	#Si son los valores maximos no se trunca
	if(i == maxValue or i == secondPeakValue):
		truncatesValues.append(i)
	else:
		#Se trunca los valores
		i = truncate(i, 0.75)
		truncatesValues.append(i)
	
#Se aplica la transformada de Fourier a los valores truncados
truncateInverseFourier = inverseFourier(truncatesValues)

#Se convierte a formato de 16 bits
inverseTruncateFourier = np.asarray(truncateInverseFourier, dtype=np.int16)

#Se grafica los valores obtenidos
plotFunction.figure("Transformada truncada de Fourier", [7.0, 4.9])
plotFunction.ylim([0, max(truncatesValues) + 10000000])
plotFunction.xlim([0, max(freqs)])
plotFunction.xlabel('Frecuencia (Hz)')
plotFunction.ylabel('F(w)')
plotFunction.title('Grafico en el dominio de la frecuencia')
plotFunction.plot(freqs, truncatesValues)

#Se guarda el audio truncado
wav.write('truncate-handel.wav', fs, inverseTruncateFourier)

#Se muestran los graficos
plotFunction.show()