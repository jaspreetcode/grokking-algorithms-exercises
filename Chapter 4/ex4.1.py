# Ex 4.1. Write out code for the earlier sum function.

def sum(li):
    if li == []:
        return 0
    else:
        return li[-1] + sum(li[:-1]);

print(sum([1, 2, 3, 4, 5])) 