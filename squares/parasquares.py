import threading

# n = 10 000, 8 hilos, chunk = 10 000 / 8 = 1250

def powerOfSquare(n):

    numbers = [None] * 10000

    def computeSquare(i):
        numbers[i] = i * i

    def printNumbers(array):
        for index, _ in enumerate(array):
            print( array[index])

    threads = [None] * 8

    def rangeCompute(c):    
        low = c*1250
        high = (c+1)*1250

        for number in range(low, high):
            computeSquare(number)


    for index, _ in enumerate(threads):
        threads[index] = threading.Thread(target=rangeCompute, args=(index,))
        threads[index].start()

    for index, _ in enumerate(threads):
        threads[index].join()


    printNumbers(numbers)

    return None

powerOfSquare(10000)