from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def solve(n):

            if n <= 1:
                return n
            else:
                solution = solve(n-2) + solve(n-1)
                return solution

def paraFibo(n, function):

    # 8 process, 20 numbers


    time1 = time.time()

    with function(max_workers=8) as executor:

        solutions = list(executor.map(solve, range(n)))

    time2 = time.time()
    actual_time = time2 - time1

    for index in range(n):
        print(f" Fibonacci N.{index}: {solutions[index]} \n")

    print(f"Seconds: {actual_time}")

    return None

if __name__ == "__main__":
    paraFibo(20, ThreadPoolExecutor)
    paraFibo(20, ProcessPoolExecutor)

    