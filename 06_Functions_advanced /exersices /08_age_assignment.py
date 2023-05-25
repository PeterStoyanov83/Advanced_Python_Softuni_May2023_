def age_assignment(*args, **kwargs):
    names_ages = {name: kwargs.get(name[0]) for name in args}

    sorted_names_ages = sorted(names_ages.items(), key=lambda x: x[0])

    return "\n".join([f"{name} is {age} years old." for name, age in sorted_names_ages])
