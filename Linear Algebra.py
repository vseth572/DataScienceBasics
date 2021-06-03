l1 = [1,2,3]
l2 = [3,4,5]
print(l1+l2)

def vector_add(v,w):
    return [v_i + w_i
            for v_i,w_i in zip(v,w)]

print(vector_add(l1,l2))

# vector_sum = partial(reduce, vector_add)

def scalar_multiply(c,v):
    """c is a number and v is a vector"""
    return [c*i for i in v]

l = [1,1,1]
print(scalar_multiply(20,l))

def dot(v,w):
    return sum(x*y for x,y in zip(v,w))

print(dot(l1,l2))