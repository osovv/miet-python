import concurrent.futures
import time


N = 5000

ps = [i for i in range(N)]
qs = [N - j for j in range(N)]


def get_elem(i, j):
  # time.sleep(0.005)
  return 1 / (1 + (qs[j] - ps[i]) ** 2)

def build_matrix_sequential(n):
    return [[get_elem(i ,j) for j in range(n)] for i in range(n)]


def build_matrix_parallel(n):
    def build_row(i):
        return [get_elem(i, j) for j in range(n)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        matrix = list(executor.map(build_row, range(n)))

    return matrix


start_time = time.time()
build_matrix_sequential(N)
sequential_time = time.time() - start_time

start_time = time.time()
build_matrix_parallel(N)
parallel_time = time.time() - start_time

print(f"Sequential execution time: {sequential_time} seconds")
print(f"Parallel execution time: {parallel_time} seconds")
