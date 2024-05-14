def first_missing_positive():
    """Find smallest missing positive integer"""
    pass


def bubble_sort(data):
    length = len(data)
    while True:
        swapped = False
        i = 1

        while i < length:
            if data[i - 1] > data[i]:
                temp = data[i]
                data[i] = data[i - 1]
                data[i - 1] = temp
                swapped = True
            i += 1

        length -= 1

        if not swapped:
            break
    return data


def selection_sort(arr):
    # set start index of unsorted sublist
    start_idx = 0

    while start_idx < len(arr) - 1:
        # set min number index to be first element of unsorted sublist
        min_num_idx = start_idx

        # set start index to be compared
        idx = start_idx + 1
        while idx < len(arr):
            # if current element with idx is less than element at start_idx,
            # then replace min index with current index
            if arr[idx] < arr[start_idx]:
                min_num_idx = idx
            idx += 1

        ## replace between element start_idx with element at min_num_idx
        temp = arr[min_num_idx]
        arr[min_num_idx] = arr[start_idx]
        arr[start_idx] = temp

        start_idx += 1

    return arr


def insertion_sort(arr):
    # loop through array...I mean list
    for i in range(1, len(arr)):
        # set max number sorted index to current i
        # (no need to set j = 0 because we know first element is considered sorted)
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            move_this_num = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = move_this_num
            j -= 1
    return arr


def main():
    print(insertion_sort([4, 5, 1]))


if __name__ == "__main__":
    main()
