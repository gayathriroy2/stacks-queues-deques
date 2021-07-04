def Createstack():
    stack=[]
    return stack
def reverse(string):
    stack=Createstack()
    for i in string:
        stack.append(i)
    string=""
    for i in range(len(stack)):
        string+=stack.pop()
    print(string)
reverse("gayathri")
