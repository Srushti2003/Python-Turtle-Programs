import turtle as t
side = int(input("Enter side length: "))
def tri(side):
    for i in range(21):
        t.forward(side)
        t.left(120)
        side-=10
tri(side)
t.done()
