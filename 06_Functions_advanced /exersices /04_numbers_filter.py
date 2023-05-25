def even_odd_filter(**kwargs):
    result = {}
    for key, values in kwargs.items():
        if key == 'odd':
            result[key] = [num for num in values if num % 2 != 0]
        elif key == 'even':
            result[key] = [num for num in values if num % 2 == 0]

    result = dict(sorted(result.items(), key=lambda item: len(item[1]), reverse=True))

    return result
