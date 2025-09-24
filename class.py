class a:
    vara="welcome to class a"
class b(c,a):
    varb="welcome to class b"
class c:
    varc="welcome to class c"
c1=b()
print(c1.varc)
print(c1.varb)
print(c1.vara)