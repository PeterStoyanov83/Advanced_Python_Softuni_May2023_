def naughty_or_nice_list(kids_list, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []

    for command in args:
        number, status = command.split('-')
        number = int(number)
        for i, kid in enumerate(kids_list):
            if kid[0] == number:
                kids_list.pop(i)
                if status == "Naughty":
                    naughty.append(kid[1])
                else:
                    nice.append(kid[1])
                break

    for name, status in kwargs.items():
        for i, kid in enumerate(kids_list):
            if kid[1] == name:
                kids_list.pop(i)
                if status == "Naughty":
                    naughty.append(name)
                else:
                    nice.append(name)
                break

    for kid in kids_list:
        not_found.append(kid[1])

    result = ""
    if nice:
        result += "Nice: " + ", ".join(nice) + "\n"
    if naughty:
        result += "Naughty: " + ", ".join(naughty) + "\n"
    if not_found:
        result += "Not found: " + ", ".join(not_found) + "\n"
    return result.strip()


