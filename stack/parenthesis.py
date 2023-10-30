def parenthesis(str):
    stack=[]
    for x in str:
        if x == '{' or x=="[" or x =="(":
            stack.append(x)
        else:
            if not stack:
                return False
            elif ismatching(stack[-1],x)==False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
def ismatching(a,b):
    if (a=='{' and b=='}')  or    (a=='[' and b==']' ) or (a=='(' and b==')'):
        return True
    else:
        return False
str="{{(}}"            
print(parenthesis(str))   
