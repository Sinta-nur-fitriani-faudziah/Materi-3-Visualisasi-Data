import numpy as np
import matplotlib.pyplot as plt

# Diberikan
h0 = 75  # ketinggian awal dalam meter
g = 9.8   # percepatan gravitasi dalam m/s^2
v0 = 0    # kecepatan awal (tidak ada kecepatan awal karena benda jatuh bebas)

# 1. Menghitung waktu yang diperlukan untuk mencapai tanah
t_total = np.sqrt(2 * h0 / g)
print(f"Waktu yang diperlukan untuk mencapai tanah: {t_total:.2f} detik")

# Membuat array waktu dari 0 hingga t_total dengan 1000 titik
t = np.linspace(0, t_total, 1000)

# 2. Kecepatan sebagai fungsi waktu (v(t) = g * t)
v_t = g * t

# 3. Posisi sebagai fungsi waktu (h(t) = h0 - 1/2 * g * t^2)
h_t = h0 - 0.5 * g * t**2

# Membuat grafik kecepatan sebagai fungsi waktu
plt.figure(figsize=(10, 5))

# Grafik kecepatan
plt.subplot(1, 2, 1)
plt.plot(t, v_t, label="Kecepatan")
plt.title('Grafik Kecepatan Benda Jatuh')
plt.xlabel('Waktu (detik)')
plt.ylabel('Kecepatan (m/s)')
plt.grid(True)

# Grafik posisi (ketinggian)
plt.subplot(1, 2, 2)
plt.plot(t, h_t, label="Ketinggian", color='r')
plt.title('Grafik Posisi Benda Jatuh')
plt.xlabel('Waktu (detik)')
plt.ylabel('Ketinggian (m)')
plt.grid(True)

# Menampilkan kedua grafik
plt.tight_layout()
plt.show()
