# BASIC ARITHMETIC FUNCTION.

def calculate(a,o,b):
    if o=="+":
        return a+b
    elif o=="-":
        return a-b
    elif o=="*":
        return a*b
    elif o=="/":
        return a/b
result=calculate(2,"+",2)
print(result)


# DEFAULT AND KEYWORD ARGUMENTS. 

def greet(a, b="HI "):
    return b+ a
result=greet("Shahid")
result2= greet("Shahid", " ASSLAM ALIKUM ")
print(result,"\n",result2)
