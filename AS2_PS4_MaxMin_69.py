import os
import math
output_file = "outputPS4.txt"
input_file = "inputPS4.txt"
output_handle = open(output_file, "w")

def find_critical_point(array):
    """This function find the maxima OR minima in the array. If the values are strictly increasing or strictly
    decreasing then return the minimum value."""
    def checkUnimodal(A, low, high):
        global minimum
        if low == high:
            if A[low] < minimum:
                minimum = A[low]
        elif high == low + 1:
            if A[low] < minimum:
                minimum = min(A[low],A[high])
        else:
            mid = math.floor((high + low) / 2)
            if A[mid] < A[mid-1] and A[mid] < A[mid+1]:
                minimum = A[mid]
            elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                high = mid
                checkUnimodal(A, low, high)
            else:
                low = mid
                checkUnimodal(A, low, high)
    lenght = len(array)
    if lenght >= 3:
        global minimum
        minimum = min(array[0], array[-1])
        checkUnimodal(array, 0, lenght-1)
        if minimum == array[0]:
            print(f"increasing {minimum}")
        elif minimum == array[-1]:
            print(f"decreasing {minimum}")
        else:
            print(f"minimum {minimum}")
    else:
        print("Insufficient Data points")



def find_maxima_point(array):
    """This function find the maxima OR minima in the array. If the values are strictly increasing or strictly
    decreasing then return the minimum value."""
    def checkUnimodal(A, low, high):
        if low == high:
            print(A[low])
        elif high == low + 1:
            print(max(A[low],A[high]))
        else:
            mid = math.floor((high + low) / 2)
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                print(A[mid])
            elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                low = mid
                checkUnimodal(A, low, high)
            else:
                high = mid
                checkUnimodal(A, low, high)
    lenght = len(array)
    if lenght >= 3:
        checkUnimodal(array, 0, lenght-1)
    else:
        print("Insufficient Data points")


def main():
    """This is the main function which reads the inputPS4.txt and  find the maxima OR minima in the array"""
    if not os.path.exists(input_file):
        print("inputPS9.txt file not found.")
        exit(1)

    with open(input_file, "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            "promptPS9.txt is empty"
            exit(1)

    for line in lines:
        line.strip()
        list_of_integers = list(map(int, line.split()))
        find_critical_point(list_of_integers)


if __name__ == "__main__":
    main()
