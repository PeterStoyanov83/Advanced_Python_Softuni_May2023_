def evaluate_expression(expression):
    tokens = expression.split()
    numbers = []

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            numbers.append(int(token))
        else:
            operator = token
            result = numbers[0]
            for num in numbers[1:]:
                if operator == "+":
                    result += num
                elif operator == "-":
                    result -= num
                elif operator == "*":
                    result *= num
                elif operator == "/":
                    result //= num
            numbers = [result]

    return numbers[0]

expression = input()
result = evaluate_expression(expression)
print(result)
