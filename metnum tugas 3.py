import numpy as np
import time

# Fungsi untuk menghitung integral menggunakan metode Riemann
def riemann_integral(f, a, b, N):
    dx = (b - a) / N
    total_area = 0
    for i in range(N):
        xi = a + i * dx
        total_area += f(xi) * dx
    return total_area

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Tempat untuk menyimpan hasil
results = []

for N in N_values:
    start_time = time.time()
    pi_approx = riemann_integral(f, 0, 1, N)
    end_time = time.time()
    
    # Hitung galat RMS
    rms_error = np.sqrt((pi_approx - pi_reference) ** 2)
    
    # Ukur waktu eksekusi
    execution_time = end_time - start_time
    
    # Simpan hasil
    results.append((N, pi_approx, rms_error, execution_time))

# Cetak hasil
for result in results:
    N, pi_approx, rms_error, execution_time = result
    print(f"N = {N}, pi_approx = {pi_approx}, RMS error = {rms_error}, Execution time = {execution_time} seconds")
