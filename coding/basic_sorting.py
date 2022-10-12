"""
Sorting

> https://www.geeksforgeeks.org/analysis-of-different-sorting-techniques/
> https://realpython.com/sorting-algorithms-python/
> https://www.geeksforgeeks.org/selection-sort/
> https://www.geeksforgeeks.org/python-program-for-heap-sort/
"""
from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    # stmt: This will take the code you want to measure the execution time
    # setup: This will have setup details that need to be executed before stmt
    # number: The stmt will execute as per the number is given here.
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


"""
Comparison based sorting

Bubble Sort
Time complexity O(n2)
Space complexity O(n)
"""
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

"""
Insertion Sort
The insertion sort algorithm works exactly like the example with the deck of cards.
Time complexity O(n2)
Space complexity O(n)
"""
def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array

"""
Selection Sort
"""
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return array

"""
Merge Sort
merge() has a linear runtime. This leads to a runtime complexity of O(n).
The second step splits the input array recursively and calls merge() for each half.
Since the array is halved until a single element remains, the total number of
halving operations performed by this function is log2n. Since merge() is called
for each half, we get a total runtime of O(nlog2n).
Pros:
Cons: Both bubble sort and insertion sort beat merge sort when sorting a ten-element list.
merge sort use much more memory than bubble sort and insertion sort, which are both able
to sort the list in place. Due to this limitation, you may not want to use merge sort 
to sort large lists in memory-constrained hardware.
Time Complexity Average: O(n*log n)
Space Complexity: O(n)
> https://www.programiz.com/dsa/merge-sort
"""
def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

# Solution 2
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

"""
Quicksort
Time Complexity Average: O(n*log n)
Space Complexity: O(log n)
> https://www.programiz.com/dsa/quick-sort
"""
from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

# Quick Sort Solution 2
# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      array[i], array[j] = array[j], array[i]

  # swap the pivot element with the greater element specified by i
  array[i + 1], array[high] = array[high], array[i + 1]

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:
    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)

"""
Timsort
the complexity of Timsort is O(n log2n)
Timsort performs exceptionally well on already-sorted or close-to-sorted lists,
leading to a best-case scenario of O(n).
In this case, Timsort clearly beats merge sort and matches the best-case scenario for Quicksort.
But the worst case for Timsort is also O(n log2n), which surpasses Quicksort's O(n2).
"""
def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    # Loop from the element indicated by
    # `left` until the element indicated by `right`
    for i in range(left + 1, right + 1):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if the `key_item` is smaller than its adjacent values.
        while j >= left and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition `j` to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, position
        # the `key_item` in its correct location
        array[j + 1] = key_item

    return array

def timsort(array):
    min_run = 32
    n = len(array)

    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `min_run` size.
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    # Now you can start merging the sorted slices.
    # Start from `min_run`, doubling the size on
    # each iteration until you surpass the length of
    # the array.
    size = min_run
    while size < n:
        # Determine the arrays that will
        # be merged together
        for start in range(0, n, size * 2):
            # Compute the `midpoint` (where the first array ends
            # and the second starts) and the `endpoint` (where
            # the second array ends)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            # Merge the two subarrays.
            # The `left` array should go from `start` to
            # `midpoint + 1`, while the `right` array should
            # go from `midpoint + 1` to `end + 1`.
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            # Finally, put the merged array back into
            # your array
            array[start:start + len(merged_array)] = merged_array

        # Each iteration should double the size of your arrays
        size *= 2

    return array

"""
Heapsort
The time complexity of heapify is O(log(n)).
Time complexity of createAndBuildHeap() is O(n).
And, hence the overall time complexity of Heap Sort is O(n*log(n)).
Space Complexity: O(1)
> https://www.programiz.com/dsa/heap-sort
"""
def heapify(arr, n, i):
    # 1. Find largest among root and children
    
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[l] > arr[i]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    # 2. If root is not largest, swap with largest and continue heapifying
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap
        # 3. Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapsort(arr):
    n = len(arr)
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0) # Heapify root element

"""
Non-comparison based sorting

Radix Sort
Counting sort is a linear time sorting algorithm that sort in O(n+k) time when elements are in the range from 1 to k.
> https://www.geeksforgeeks.org/radix-sort/
"""
# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radix_sort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10

"""
Counting Sort
Time Complexity: O(n+k) 
Auxiliary Space: O(n+k)
> https://www.geeksforgeeks.org/counting-sort/
"""
# Python program for counting sort
# The main function that sort the given string arr[] in 
# alphabetical order
def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
  
    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
  
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
  
    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
  
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
  
    return arr

"""
Bucket Sort
Average	O(n)
Space Complexity: O(n+k)
> https://www.programiz.com/dsa/bucket-sort
> https://www.geeksforgeeks.org/bucket-sort-2/
"""
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up: 
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up     
    return b     
              
def bucket_sort(x):
    arr = []
    slot_num = 10 # 10 means 10 slots, each
                  # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])
          
    # Put array elements in different buckets 
    for j in x:
        index_b = int(slot_num * j) 
        arr[index_b].append(j)
      
    # Sort individual buckets 
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
          
    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


ARRAY_LENGTH = 10000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999

    # array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="sorted", array=array)

    # Call each of the functions
    run_sorting_algorithm(algorithm="bubble_sort", array=array)
# Algorithm: bubble_sort. Minimum execution time: 73.21720498399998

    run_sorting_algorithm(algorithm="selection_sort", array=array)
# Algorithm: selection_sort. Minimum execution time: 31.74471645899996

    run_sorting_algorithm(algorithm="insertion_sort", array=array)
# Algorithm: insertion_sort. Minimum execution time: 56.71029764299999

    run_sorting_algorithm(algorithm="merge_sort", array=array)
# Algorithm: merge_sort. Minimum execution time: 0.6195857160000173

    run_sorting_algorithm(algorithm="heapsort", array=array)
# Algorithm: heapsort. Minimum execution time: 0.48962458400001196

    run_sorting_algorithm(algorithm="quicksort", array=array)
# Algorithm: quicksort. Minimum execution time: 0.11675417600002902

    run_sorting_algorithm(algorithm="timsort", array=array)
# Algorithm: timsort. Minimum execution time: 0.39657199999999193

    run_sorting_algorithm(algorithm="radix_sort", array=array)
# Algorithm: radix_sort. Minimum execution time: 0.15927529199996115

    run_sorting_algorithm(algorithm="count_sort", array=array)
# Algorithm: count_sort. Minimum execution time: 0.04350587499999392

    # run_sorting_algorithm(algorithm="bucket_sort", array=array)
# Algorithm: bucket_sort. Minimum execution time: 0.1
