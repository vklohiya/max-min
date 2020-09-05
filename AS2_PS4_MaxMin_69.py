import os
import math
output_file = "outputPS4.txt"
input_file = "inputPS4.txt"
output_handle = open(output_file, "w")

def find_critical_point(array):
    """This function find the maxima OR minima in the array. If the values are strictly increasing or strictly
    decreasing then return the minimum value."""
    def checkMinima(A, low, high):
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
                checkMinima(A, low, high)
            else:
                low = mid
                checkMinima(A, low, high)

    def checkMaxima(A, low, high):
        global maxima, print_max
        if low == high:
            maxima = A[low]
        elif high == low + 1:
            maxima = max(A[low],A[high])
        else:
            mid = math.floor((high + low) / 2)
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                maxima = A[mid]
                print_max = True
            elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                low = mid
                checkMaxima(A, low, high)
            else:
                high = mid
                checkMaxima(A, low, high)

    lenght = len(array)
    if lenght >= 3:
        global minimum, maxima, print_max
        print_max = False
        nl = '\n'
        minimum = min(array[0], array[-1])
        maxima = max(array[0], array[-1])
        checkMinima(array, 0, lenght-1)
        checkMaxima(array, 0, lenght - 1)
        if print_max:
            output_handle.write(f"maxima {maxima}{nl}")
        else:
            if minimum == array[0]:
                output_handle.write(f"increasing {minimum}{nl}")
            elif minimum == array[-1]:
                output_handle.write(f"decreasing {minimum}{nl}")
            else:
                output_handle.write(f"minimum {minimum}{nl}")
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
