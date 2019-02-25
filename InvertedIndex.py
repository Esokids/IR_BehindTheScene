def selection_sort(lists):
    for i in range(len(lists)):
        # Find the minimum element in remaining
        min_position = i
        for j in range(i + 1, len(lists)):
            if lists[min_position] > lists[j]:
                min_position = j
        # Swap the found minimum element with min_position
        temp = lists[i]
        lists[i] = lists[min_position]
        lists[min_position] = temp
    return lists


if __name__ == '__main__':
    print(selection_sort(['a', 'b', 'c', 'd', 'e', 'f', '0', '1']))
