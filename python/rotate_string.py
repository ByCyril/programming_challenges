def rotate(original, rotated):

    head = rotated[:2]
    lower_body = rotated[2:]

    tail = rotated[len(rotated) - 2:]
    upper_body = rotated[:len(rotated) - 2]

    if lower_body + head == original or tail + upper_body == original:
        return 1
    else:
        return 0


res = rotate('wlrbbmqbhcdar', 'owkkyhiddqscd')

print(res)
