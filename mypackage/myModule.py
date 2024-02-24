def top_n(array, n):
    """
    This function takes an array of integers and returns the top n elements of the array in descending order
    :param array:
    :param n:
    :return: array of top n integers
    """
    for i in range(n):
        for j in range(len(array) - 1 - j):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    # last two
    top_n = array[-n:]

    #descending
    return top_n[::-1]