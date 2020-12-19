def get_and_save_middle(data, filename):
    middle = data[len(data) // 3:2 * len(data) // 3]
    save_to_file(middle, filename)
    return middle


def save_to_file(data, filename):
    pass


print(get_and_save_middle('ghghhg', 'file.txt'))

