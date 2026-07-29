# 字典是带有key的set，每一个key和value一一对应，无序且不能重复
# 在 Python3.6 版本之后，实际顺序为插入时的顺序

# 创建字典
# 直接使用{}
dict_1 = {1:'a', 2:'b', 3:'c'}
print(dict_1)
dict_2 = {'name':'Tom', 'age':20, 'gender':'Male'}
print(dict_2)
# 使用 dict() 构造函数
dict_3 = dict(name='Jerry', age=21, gender='Female')
print(dict_3)
# 从列表或者元组转换
pair = [('name','Tom'), ('age',20), ('gender','Male')]
dict_4 = dict(pair)
print(dict_4)
# 使用字典推导式快速创建
dict_5 = {x : x**2 for x in range(1,11)}
print(dict_5)

# 访问
person = {'name':'Tom', 'age':20, 'gender':'Male'}
print(person['name'])
# 如果key不存在会报错，可以使用 .get() 方法，不存在会返回None或者默认值
print(person.get('name'))
print(person.get('name', 'Not Found'))

# 修改和新增
# 在Java中使用 put() 方法
person['age'] = 30
print(person)
# 如果key存在，则修改
person.update({'age':28})
print(person)
# 如果key不存在，则新增
person['city'] = 'Beijing'
print(person)
person.update({'city':'Shanghai'})
print(person)

# 删除
# 在java中使用 remove()
item = person.pop('gender')
print(item)
print(person)

# 获取keys, values, items
# 在java中为 keySet(), values(). entrySet()
print(person.keys())
print(type(person.keys()))
print(person.values())
print(type(person.values()))
print(person.items())
print(type(person.items()))

# 遍历字典
# 通过 keys
for key in person.keys():
    print(key, person[key])
# 对应Java中的：
# for (String key : person.keySet()) {
#   System.out.println(key + " = " + person.get(key));
# }
# 通过 values
for value in person.values():
    print(value)
# 对应Java中的：
# for (Object value : person.values()) {
#   System.out.println(value);
# }
# 通过 items
for key, value in person.items():
    print(key, value)
# 对应Java中的:
# for (Map.Entry<String, Object> entry : person.entrySet()) {
#   System.out.println(entry.getKey() + " = " + entry.getValue());
# }