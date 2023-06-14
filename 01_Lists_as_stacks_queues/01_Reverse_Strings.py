text = input()

stack = []
for char in text:
    stack.append(char)

reversed_text = ""
while stack:
    reversed_text += stack.pop()

print(reversed_text)


text = input()          #reading the input

stack = []              #creating the stack variable as a list

for char in text:
    stack.append(char)  #cycling thorugh each character and putting it in the stack list

reversed_text = ""      #creating the variable for reversed text

while stack:
    reversed_text += stack.pop()    #filling up the reversed variable by taking out each time the last char from the
                                    # stack and putting it in the output variable

print(reversed_text)    #print the output