class p:

    def d(self):
        print("1\n1\t1")
class q:
    def i(self):
        print("2\n2\n2")

class c(p,q):
    def s(self):
        print("3\n3")

o=c()
o.i()
o.d()
