from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def paraFibo(n):

    # 8 process, 10 000 numbers

    solutions = {}

    for number in range(n+1):
        solutions[number] = -1

    def solve(n):

        if solutions[n] != -1:
            return solutions[n]

        else:

            if n <= 1:
                solutions[n] = n
                return n
            else:
                solution = solve(n-2) + solve(n-1)
                solutions[n] = solution
                return solution

    with ThreadPoolExecutor(max_workers=8) as executor:

        executor.map(solve, range(10000))

    solve(n)

    for index in range(n+1):
        print(f" Fibonacci N.{index}: {solutions[index]} \n")

    return None

paraFibo(10000)

    