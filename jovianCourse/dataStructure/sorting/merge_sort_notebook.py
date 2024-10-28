from entities.notebook import Notebook

# you're working on a new feature on Jovian called "Top Notebooks of the Week".
# write a function to sort a list of notebooks in decreasing order of likes.
# keep in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible.

nb0 = Notebook('pytorch-basics', 'daniel', 373)
nb1 = Notebook('linear-regression', 'eric', 532)
nb2 = Notebook('logistic-regression', 'valerie', 31)
nb3 = Notebook('feedforward-nn', 'john', 94)
nb4 = Notebook('cifar10-cnn', 'zachary', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'valentine', 80)
nb7 = Notebook('python-fundamentals', 'henry', 136)
nb8 = Notebook('python-functions', 'daniel', 74)
nb9 = Notebook('python-numpy', 'tanya', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]


def merge(left_sorted, right_sorted):
    merged = []
    left_pointer, right_pointer = 0, 0

    while left_pointer < len(left_sorted) and right_pointer < len(right_sorted):
        if left_sorted[left_pointer].likes >= right_sorted[right_pointer].likes:
            merged.append(left_sorted[left_pointer])
            left_pointer += 1
        else:
            merged.append(right_sorted[right_pointer])
            right_pointer += 1

    left_tail = left_sorted[left_pointer:]
    right_tail = right_sorted[right_pointer:]

    return merged + left_tail + right_tail


def merge_sort(notebooks):
    # terminating condition (list of 0 or 1 elements)
    if len(notebooks) <= 1:
        return notebooks

    mid = len(notebooks) // 2

    left = notebooks[:mid]
    right = notebooks[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    sorted_result = merge(left_sorted, right_sorted)

    return sorted_result


notebooks = merge_sort(notebooks)

for notebook in notebooks:
    print(notebook)