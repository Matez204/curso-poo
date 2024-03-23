class A:
    def hablar(self):
        print("Hola desde A")

class F:
    def hablar(self):
        print("Hola desde F")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(F):
    def hablar(self):
        print("Hola desde C")

class D(C,B):
    pass

"""
    <A>   <F>
     |     |
    <B>   <C>
     |     |
     \    /
      <D>
 self.mro() esta funcion sirve para ver el orden gerarquico de las clases hereciadas
"""
d=D()

d.hablar()
B.hablar(d)