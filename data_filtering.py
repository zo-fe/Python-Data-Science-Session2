def filter_integers(data_list):
    return [item for item in data_list if isinstance(item, int)]

mixed_data = [1, "hello", 3.5, 7, "world", 42, 8.9, 15]

filtered_integers = filter_integers(mixed_data)

print("Filtered integers:", filtered_integers)
