import threading

def parallelFibonacci(n):

    #n = 10000, 8 threads, chunk = 1250


    solutions = {}

    for number in range(n+1):
        solutions[number] = -1

    def solve(n):
        if solutions[n] != -1:
            return solutions[n]
        else:

            if n == 0:
                solutions[n] = 0
                return 0
            elif n == 1:
                solutions[n] = 1
                return 1
            else:
                solved = solve(n-2) + solve(n-1)
                solutions[n] = solved
                return solved

    def parallel_solve(c):

        low = c*1250
        high = (c+1)*1250

        for i in range(low, high):
            solve(i)


    

    threads = [None] * 8

    for index, i in enumerate(threads):
        threads[index] = threading.Thread(target=parallel_solve, args=((index),))
        threads[index].start()

    for index, i in enumerate(threads):
            threads[index].join()

    return solve(n)

print(parallelFibonacci(10000))