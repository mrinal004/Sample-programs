def balancedBrackets(expr):
    stack=[]
    for i in range(len(stack)):
        if (expr[i]=='(' or '{' or '['):
            stack.append(expr[i])
            continue
        if len(stack)==0:
            return False
        if expr[i]==')':
            x=stack.pop()
            if (x=='{' or '['):
                return False
        elif expr[i]=='}':
            x=stack.pop()
            if x=='('or '[':
                return False
        elif expr[i]==']':
            x=stack.pop()
            if x=='(' or '{':
                return False
    if len(stack):
        return True
    else:
        return False 
if __name__=='__main__':
    expr='{()}[]'
    if (balancedBrackets(expr)):
        print('Balanced')
    else:
        print('unbalanced')
           