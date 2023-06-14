stack_parent = []  # create the stack for the parantecies finder

text = input() #the text we take from the console by user

for index in range(len(text)):              #create the for loop to get through everu index
    if text[index] == '(':                  #check if index is a (
        stack_parent.append(index)          #then put it in the stack variable

#this cycle will fill up the stack with the text between the ()

    elif text[index] == ')':                    #check for the closing )
        start_position = stack_parent.pop()     #if the inxex is ) remove it from the stack and define the index in text
                                                #as start position
        end_position = index + 1                #define the next index as the ending of the end position
    print(text[start_position:end_position])    #print the text that was between the two intexes with "()"


