import make_warnings

def sun(c,d):
    print(d,c)

class Test_aa():
    def test_a(self):
        a = 1
        b = 2
        assert a == b,sun(a,b)