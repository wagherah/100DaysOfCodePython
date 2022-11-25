# we can pass any number of positional arguments to a function
# e.g

def func(*args):
    # arguments are dealt as tuple here
    print(args)

# passing maximum number of positional arguments
func(1,2,3,4,5,6,7,8)

# Likewise we can pass any number of keyword arguments to a function
# e.g

def func2(**kwargs):
    # arguments are dealt as dictionary here
    print(kwargs)

func2(a=5, b=6, c=7, d=8)
