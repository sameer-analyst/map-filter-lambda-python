# Higher Order Functions in Python
def apply_fun(fun,value):
    return fun(value)

result = apply_fun(lambda x:x*3,3)
print(result)

def greet(fun):
    return fun("Sameer")

def say_hello(name):
    return f"Hello {name}"

print(greet(say_hello))