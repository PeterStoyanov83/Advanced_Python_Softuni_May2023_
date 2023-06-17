def gather_credits(*args):
    needed_credits = args[0]
    courses = args[1:]
    enrolled_courses = []
    gathered_credits = 0

    for course, credits in courses:
        if course not in enrolled_courses and gathered_credits < needed_credits:
            enrolled_courses.append(course)
            gathered_credits += credits

    if gathered_credits >= needed_credits:
        enrolled_courses.sort()
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(enrolled_courses)}"
    else:
        credits_shortage = needed_credits - gathered_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
