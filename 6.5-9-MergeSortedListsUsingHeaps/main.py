# CLRS 3rd edition - Solution of 6.5-9
# Give an O(n lg k)-time algorithm to merge k sorted lists into one sorted list,
# where n is the total number of elements in all the input lists. (Hint: Use a min-
# heap for k-way merging.)

import heap as h


# compare two pairs of type (value,list_index)
# we are comparing depending on value
# since we use min-heap in our main algorithm, we use is lower or equal as comparing function
def pair_compare(p1,p2):
    return p1[0] <= p2[0]


def merge_sorted_lists(lists):
    lists = list(filter(lambda lst: len(lst) > 0, lists))

    lowest_from_each = []
    for i in range(0, len(lists)):
        lowest_from_each.append((lists[i][0], i))
        del lists[i][0]

    the_heap = h.Heap(elems=lowest_from_each, is_greater_or_equal_than_function=pair_compare)
    merged_lists = []
    while not the_heap.is_empty():
        value, index_of_list = the_heap.extract_max()
        merged_lists.append(value)
        if len(lists[index_of_list]) > 0:
            the_heap.insert((lists[index_of_list][0],index_of_list))
            del lists[index_of_list][0]

    return merged_lists
