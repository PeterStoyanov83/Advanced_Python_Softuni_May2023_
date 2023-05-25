def fill_the_box(height, length, width, *args):
    total_volume = height * length * width
    remaining_volume = total_volume

    for arg in args:
        if arg == "Finish":
            break

        remaining_volume -= arg

    if remaining_volume > 0:
        return f"There is free space in the box. You could put {remaining_volume} more cubes."

    else:
        return f"No more free space! You have {abs(remaining_volume)} more cubes."
