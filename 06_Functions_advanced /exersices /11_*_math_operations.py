def math_operations(*args, **kwargs):
    operations = ["a", "s", "d", "m"]

    for i, number in enumerate(args):
        operation = operations[i % 4]

        if operation == "a":
            kwargs[operation] += number
        elif operation == "s":
            kwargs[operation] -= number
        elif operation == "d":
            if number != 0:
                kwargs[operation] /= number
        elif operation == "m":
            kwargs[operation] *= number

    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join([f"{k}: {v:.1f}" for k, v in sorted_kwargs])
