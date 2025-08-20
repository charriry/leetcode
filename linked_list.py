import numpy as np
from numba import cuda, njit, prange
import time

# ---------- 参数 ----------
N = 20480                      # 调大到 2K×2K，GPU 才有明显收益
A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)

# # ---------- 1. NumPy CPU ----------
# start = time.perf_counter()
# C_cpu = A @ B
# t_cpu = time.perf_counter() - start
# print(f"NumPy CPU: {t_cpu:.4f} s")

# # ---------- 2. Numba CPU 并行 ----------
# @njit(parallel=True, fastmath=True)
# def matmul_cpu(a, b, c):
#     m, n = a.shape
#     p = b.shape[1]
#     for i in prange(m):
#         for j in range(p):
#             s = 0.0
#             for k in range(n):
#                 s += a[i, k] * b[k, j]
#             c[i, j] = s

# C_nb_cpu = np.empty_like(A)
# matmul_cpu(A, B, C_nb_cpu)      # JIT 预热
# start = time.perf_counter()
# matmul_cpu(A, B, C_nb_cpu)
# t_nb_cpu = time.perf_counter() - start
# print(f"Numba CPU: {t_nb_cpu:.4f} s")

# ---------- 3. Numba GPU ----------
TPB = 16                        # thread per block

@cuda.jit
def matmul_gpu(a, b, c):
    row, col = cuda.grid(2)
    if row < c.shape[0] and col < c.shape[1]:
        s = 0.0
        for k in range(a.shape[1]):
            s += a[row, k] * b[k, col]
        c[row, col] = s

# 把数据拷到 GPU
dA = cuda.to_device(A)
dB = cuda.to_device(B)
dC = cuda.device_array_like(A)

# 计算网格尺寸
blocks_per_grid_x = (N + TPB - 1) // TPB
blocks_per_grid_y = (N + TPB - 1) // TPB
blocks = (blocks_per_grid_x, blocks_per_grid_y)
threads = (TPB, TPB)

# 预热
matmul_gpu[blocks, threads](dA, dB, dC)
cuda.synchronize()

start = time.perf_counter()
matmul_gpu[blocks, threads](dA, dB, dC)
cuda.synchronize()
t_gpu = time.perf_counter() - start
print(f"Numba GPU: {t_gpu:.4f} s")

# ---------- 4. 正确性检查 ----------
assert np.allclose(C_cpu, C_nb_cpu)
C_gpu = dC.copy_to_host()
assert np.allclose(C_cpu, C_gpu, atol=1e-3)

# ---------- 5. 结果 ----------
print(f"GPU vs CPU 加速比: {t_cpu / t_gpu:.1f}x")