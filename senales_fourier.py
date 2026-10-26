
import numpy as np
import matplotlib.pyplot as plt

# 1. Configurar los parametros de la simulacion
fs = 1000  # Frecuencia de muestreo: 1000 muestras por segundo
T = 1      # Duracion de la senal: 1 segundo

# 2. Crear el eje del tiempo
t = np.arange(0, T, 1/fs)

# 3. Crear dos senales senoidales
senal1 = np.sin(2 * np.pi * 10 * t)       # Frecuencia de 10 Hz
senal2 = 0.5 * np.sin(2 * np.pi * 30 * t) # Frecuencia de 30 Hz

# 4. Combinar las dos senales
senal = senal1 + senal2

# 5. Graficar la senal en el dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(t, senal)
plt.xlim(0, 0.5)
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.title("Senal en el dominio del tiempo")
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. Aplicar la Transformada de Fourier
N = len(senal)
transformada = np.fft.rfft(senal)

# 7. Calcular las frecuencias y sus magnitudes
frecuencias = np.fft.rfftfreq(N, d=1/fs)
magnitud = (2/N) * np.abs(transformada)
magnitud[0] /= 2

# 8. Graficar el espectro de frecuencia
plt.figure(figsize=(10, 4))
plt.plot(frecuencias, magnitud)
plt.xlim(0, 60)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.title("Espectro de frecuencia - Transformada de Fourier")
plt.grid(True)
plt.tight_layout()
plt.show()
