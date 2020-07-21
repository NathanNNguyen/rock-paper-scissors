def partition(numbers):
    # this function breaks 'numbers' into left, pivot and right
    left = []
    pivot = numbers[0]
    right = []

    # partition the numbers correctly into left and right arrays
    for num in numbers[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right

def quicksort(numbers):
    # base case
    # what is the easiest way to sort?
    # make them a single item array
    if len(numbers) <= 1:
        return numbers

    # divide
    # figure out how to properly split our data
    left, pivot, right = partition(numbers)

    sorted_arr = quicksort(left), [pivot] + quicksort(right)

    return sorted_arr