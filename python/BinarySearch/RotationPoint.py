# Given a list of rotated sorted words in a list.
# Find the rotation point

def find_rotation_point(words):
    # Find the rotation point in the list
    end = len(words) - 1
    if words[0] <= words[end]:
        return -1

    return find_pivot(words, 0, end)


def find_pivot(words, start, end):
    if (end - start) == 1:
        return end

    mid = (start + end) // 2
    if words[start] <= words[mid]:
        return find_pivot(words, mid, end)
    else:
        return find_pivot(words, start, mid)
