def mov(b):
    m = []
    for p, piece in enumerate( b ):
        j = p + (piece * 2)
        m2 = p + (piece)
        if ( piece == 0 ):
            continue
        if (not (( j < 0 ) or ( j >= len(b)))):
            if (b[j] == 0):
                t = list(b)
                t[p] = 0
                t[j] = piece
                m.append(t)
        if (not ((m2 < 0) or ( m2 >= len(b)))):
            if ( b[m2] == 0):
                t = list(b)
                t[p] = 0
                t[m2] = piece
                m.append(t)
    return m

def evaluate( c, tar ):
    next = []
    for a in c:
        n = mov(a[-1])
        for q in n:
            t = list(a)
            t.append(q)
            if ( q == tar ):
                return t
            next.append(t)
    return next

def arr(start):
    temp=[[start]]
    end = list(start)
    end.reverse()
    while(temp[-1] != end):
        temp = evaluate(temp, end)
    return temp
a= [1, 1, 1, 0, -1, -1, -1]
print(arr(a))