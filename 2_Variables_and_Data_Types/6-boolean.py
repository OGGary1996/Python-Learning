is_activate = True
is_deleted = False

print("is_activate:", is_activate)
print("type of is_activate:", type(is_activate))
print("is_deleted:", is_deleted)
print("type of is_deleted:", type(is_deleted))

# boolean类型本质上也是数字类型，在运算时，True会被当作1，False会被当作0
print(is_activate*2)
print(type(is_activate*2))
