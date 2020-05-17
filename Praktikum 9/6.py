class simpulbiner(object):
    def __init__(self, data):
        self.data=data
        self.kiri=None
        self.kanan=None

    def __str__(self):
        return str(self.data)

A=simpulbiner('Ambarawa')
B=simpulbiner('Bantul')
C=simpulbiner('Cimahi')
D=simpulbiner('Denpasar')
E=simpulbiner('Enrekang')
F=simpulbiner('Flores')
G=simpulbiner('Garut')
H=simpulbiner('Halmahera Timur')
I=simpulbiner('Indramayu')
J=simpulbiner('Jakarta')

A.kiri=B
A.kanan=C
B.kiri=D
B.kanan=E
C.kiri=F
C.kanan=G
E.kiri=H
G.kiri=J
G.kanan=I

def size(node):
    if node is None: 
        return 0
    else: 
        return size(node.kiri) + 1 + size(node.kanan)

print('Ukuran dari Binary Tree adalah', size(A))
