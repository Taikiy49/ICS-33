class X:
    def only_x(self):
        print('only X')
    def both(self):
        print('both X')
class Y:
    def only_y(self):
        print('only Y')
    def both(self):
        print('both Y')
class Z(X, Y):
    def only_x(self):
        super().only_x()
    def only_y(self):
        super().only_y()
    def both(self):
        super().both()

z = Z()
(z.both()) # output: both X
# reasonable theory is that X is listed first in Z's bases, so it wins!

class W:
    def foo(self):
        print('W foo')
class W(X):
    def foo(self):
        print('X foo')
        super().foo()
class Y(W):
    def foo(self):
        print('Y.foo')
        super().foo()
class Z(X, Y):
    def print(self):
        print('Z foo')
        super().foo()

print(X().foo())
