numbers = [1, 2, 3, 4, 5, 6]
def is_even(x):
    return x%2==0 
    

a=list(filter(is_even, numbers))
print(a)
