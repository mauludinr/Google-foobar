def ke_basis_10(bil_basis_b,basis):
    basis_b = str(bil_basis_b)[::-1]
    pjg = len(basis_b)
    hasil = 0
    for i in range(pjg):
        hasil+=int(basis_b[i])*(basis**i)
    return hasil

def ke_basis_b(n,b):
        s = ''
        if int(n) < b:
            return str(n)
        while n != 0:
            s = str(int(n)%b) + s
            n = int(n)//b
        return s  

def solution(n, b):
    k = len(n)
    m = n
    mini_id = []
    while m not in mini_id:
        mini_id.append(m)
        s = sorted(m)
        x_descend = ''.join(s[::-1])
        y_ascend = ''.join(s)        
        if b == 10:
            int_m = int(x_descend) - int(y_ascend)
            m = str(int_m)
        else:
            int_m_10 = int(ke_basis_10(x_descend, b)) - int(ke_basis_10(y_ascend, b))
            m = ke_basis_b(str(int_m_10), b)
        
        m =  (k - len(m)) * '0' + m
    return len(mini_id) - mini_id.index(m)
