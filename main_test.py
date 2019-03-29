from test import Pointer

p=Pointer(10,10)

print(p.x)
print(p.y)
print(p.move_right())
print(p.x)
p.move_left()
p.move_left()
print(p.x)