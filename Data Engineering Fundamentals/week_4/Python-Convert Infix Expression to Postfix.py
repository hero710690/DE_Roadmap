
def infix_to_postfix(infix):
    stack = []
    output = []
    symbol = {"+":1, "-":1, "*":2, "/":2, "^":3}

    for char in infix:
        if char.isalpha() or char.isdigit():
            output.append(char)
        elif char=='(':
            stack.append(char)
        elif char==')':
            while len(stack)>0 and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else: 
            while len(stack)>0 and stack[-1] != '(' and symbol[char]<= symbol[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)

if __name__ == '__main__':
    infix =  "A+B*C"
    postfix = infix_to_postfix(infix) #A B C * +