def cari(maks_node, converter):
    prev_node = -1
    current_node = maks_node
    subtree = maks_node

    if current_node == converter:
        return prev_node

    prev_node = current_node

    while subtree > 1:
        subtree = subtree >> 1

        left = current_node - subtree - 1
        right = current_node - 1

        if converter == left or converter == right:
            return prev_node

        if converter < left:
            current_node = left
        elif converter > left:
            current_node = right

        prev_node = current_node

    return -1

def solution(h, q):
    maks_node = 2**h-1
    hasil = []
    for c in q:
      hasil.append(cari(maks_node,c))
    return hasil
