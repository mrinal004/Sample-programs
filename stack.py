from sys import maxsize
def stack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print(item,'pushed to stack')
def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize -1)
    return stack.pop()
def peek(stack):
    if (isEmpty(stack)):return str(-maxsize -1)
    return stack[len(stack)-1]
stack=stack()
push(stack,10)
push(stack,20)
push(stack,30)
push(stack,40)
for i in range(len(stack)):
    print(pop(stack),'removed from stack')
res=peek(stack)
print(res)