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

# Calculo de la tranformada de fourier
fourierTransform = fourier(data)

# Calculo de las frecuencias (Eje X)
freqs = frequency(len(data), 1.0 /fs)

# Calculo de la inversa de la transformada
inverseFourierTransform = inverseFourier(fourierTransform)

# Se grafica la transformada de fourier
plotFunction.figure("Transformada de Fourier", [7.0, 4.9])
plotFunction.xlabel('Frecuencia (Hz)')
plotFunction.ylabel('F(w)')
plotFunction.title('Grafico en el dominio de la frecuencia')
plotFunction.plot(freqs, fourierTransform)

# Se grafica la inversa de la transformada
plotFunction.figure("Inversa de la Transformada", [7.2, 4.5])
plotFunction.plot(audioTime, inverseFourierTransform)
plotFunction.title('Grafico del audio con su transformada inversa en el tiempo')
plotFunction.ylabel('Amplitud')
plotFunction.xlabel('Tiempo (s)')

# Cambio a formato de 16 bits
inverseFourierTransform = np.asarray(inverseFourierTransform, dtype=np.int16)

# Guardar archivo de la tranformada inversa
wav.write('inverse-handel.wav', fs, inverseFourierTransform)

#Funcion que trunca un valor con respecto a un porcentaje
def truncate(value, percent):
	return (value - (percent * value))

#Se copia la lista de frecuencias
freqsAux = freqs.copy()

#Se copia la lista de la transformada
fourierTransformAux = fourierTransform.copy()

#Se ordena de menor a mayor
fourierTransformAux.sort()

#Se obtiene el valor maximo
maxValue = fourierTransformAux[-1]

#Se obtiene el valor maximo perteneciente a las frecuencias negativas
maxValueNegative = fourierTransformAux[-2]

#Para obtener el segundo peak alto del grafico
secondPeakValue = 0

#Para obtener el segundo peak alto del grafico del lado negativo
secondPeakValueNegative = 0

#Se recorre las frecuencias
for index, i in enumerate(freqsAux):
	#Se mira entre los valores 0.1 y 0.2 (Donde se encuentra el segundo peak)
	if(i > 1000 and i < 1500):
		if fourierTransform[index] > secondPeakValue:
			#Se guarda el valor mas alto
			secondPeakValue = fourierTransform[index]
	if(i > -1500 and i < -1000):
		if(fourierTransform[index] > secondPeakValueNegative):
			secondPeakValueNegative = fourierTransform[index]

#Se truncan los valores de la transfomada de fourier con respecto a un 75%
#Se guarda en la lista truncateValues
truncatesValues = []
for i in fourierTransform:
	#Si son los valores maximos no se trunca
	if(i == maxValue or i == secondPeakValue or i == maxValueNegative or i == secondPeakValueNegative):
		truncatesValues.append(i)
	else:
		#Se trunca los valores
		i = truncate(i, 0.5)
		truncatesValues.append(i)
	
#Se aplica la transformada de Fourier a los valores truncados
truncateInverseFourier = inverseFourier(truncatesValues)

#Se convierte a formato de 16 bits
inverseTruncateFourier = np.asarray(truncateInverseFourier, dtype=np.int16)

#Se grafica los valores obtenidos
plotFunction.figure("Transformada de Fourier valores truncados", [7.0, 4.9])
plotFunction.xlabel('Frecuencia (Hz)')
plotFunction.ylabel('F(w)')
plotFunction.title('Transformada de Fourier valores truncados')
plotFunction.plot(freqs, truncatesValues)

# Se grafica en el dominio del tiempo
plotFunction.figure("Grafico en el dominio del tiempo truncado", [7.0, 5.3])
plotFunction.xlabel('Frecuencia (Hz)')
plotFunction.ylabel('F(w)')
plotFunction.title('Grafico en el dominio del tiempo truncado')
plotFunction.plot(audioTime, inverseTruncateFourier)

#Se guarda el audio truncado
wav.write('truncate-handel.wav', fs, inverseTruncateFourier)

#Se muestran los graficos
plotFunction.show()