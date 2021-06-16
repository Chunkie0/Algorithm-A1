def bubble_sort(name):
    letters = list(name)

    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(letters)-1):
            if ord(letters[i]) > ord(letters[i+1]):
                letters[i], letters[i+1] = letters[i+1], letters[i]
                not_sorted = True
    return "".join(letters).strip()

print(bubble_sort("davis dambis"))