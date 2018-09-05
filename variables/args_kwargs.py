def my_method(arg1,arg2):
    return arg1+arg2

my_method(5,6)


def addition_simplified(*args):
    return sum(args)


print(addition_simplified(3,4,5,6))


def what_are_kwarkgs(*args,**kwargs):
    print(args)
    print(kwargs)

what_are_kwarkgs(12,34,56, name = 'Jose', location='UK')