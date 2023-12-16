def solution(lines):
    a, b, c = lines
    a = set(range(a[0], a[1]+1))
    b = set(range(b[0], b[1]+1))
    c = set(range(c[0], c[1]+1))
    print(a & b)
    print(b & c)
    print(c & a)
    print(a & b & c)
    
    ab = len(a & b) -1 if len(a & b) != 0 else 0
    bc = len(b & c) -1 if len(b & c) != 0 else 0
    ca = len(c & a) -1 if len(c & a) != 0 else 0
    abc = len(a & b & c) -1 if len(a & b & c) != 0 else 0
    
    result = ab + bc + ca - 2*abc
    return result