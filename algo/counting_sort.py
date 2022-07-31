# Counting sort in Python programming

def countingSort(array):
    N = len(array)
    maxE = max(array)
    output = [0] * (N)

    # Initialize count array
    count = [0] * (maxE+1)

    # Store the count of each elements in count array
    for i in range(N):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, maxE+1):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = N - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, N):
        array[i] = output[i]
