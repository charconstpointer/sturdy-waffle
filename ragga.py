def merge_sort(source):
    if len(source) > 1:
        middle = len(source) // 2
        left = source[:middle]
        right = source[middle:]
        left = merge_sort(left)
        right = merge_sort(right)
        s = merge(left, right)
        return s
    return source


def merge(left, right):
    i, j, = 0, 0
    s = []
    while i <= len(left) - 1 and j <= len(right) - 1:
        if left[i] <= right[j]:
            s.append(left[i])
            i += 1
        else:
            s.append(right[j])
            j += 1
    while i <= len(left) - 1:
        s.append(left[i])
        i += 1
    while j <= len(right) - 1:
        s.append(right[j])
        j += 1
    print('-> ', s)
    return s


def main():
    data = [9, 7, 5, 3, 2, 4, 6, 8, 0]
    print(merge_sort(data))


if __name__ == '__main__':
    main()
