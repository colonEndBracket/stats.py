import sys
import math

def mean(data):
    return sum(data)/len(data)

def median(data):
    index = len(data) // 2
    if len(data) % 2:
        return sorted(data)[index]
    return sum(sorted(data)[index - 1:index +1]) / 2

def fileToDataSet(filename):
    f = open(filename,"r")
    data = f.readlines()
    f.close()
    data = [float(val) for val in data]
    return data

def variance(data):
    sumOfSquares = sum([i**2 for i in data])
    squareOfSums = sum(data)**2
    n = len(data)
    return (sumOfSquares - (squareOfSums)/n)/(n-1)

def standardDev(data):
    return math.sqrt(variance(data))

if __name__ == '__main__':
    filename="statdata.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    q = fileToDataSet(filename)
    print("DATA:\t",sorted(q))
    print("sum\t=> %.3f" % sum(q))
    print("mean\t=> %.3f" % mean(q))
    print("median\t=> %.3f" % median(q))
    print("var\t=> %.3f" % variance(q))
    print("dev\t=> %.3f" % standardDev(q))
