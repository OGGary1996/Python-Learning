# 元组 Tuple 是有序的，但不可修改的序列
# 与 List 类似，但是一旦创建，则不可修改内容
# 在Java中，使用 List.of("...") 实现不可修改的列表

# 元组的创建
# 1. 使用 () 创建
tuple_1 = (1,2,3)
print(tuple_1)
# 2. 使用 tuple() 方法转换得到
list_1 = [1,2,3,4,5]
tuple_2 = tuple(list_1)
print(tuple_2)
# 3. 省略()
tuple_3 = 1,2,3
print(tuple_3)
# 注意：由于可以省略() 在创建单个元素的元组时，需要补充 ,
tuple_4 = (1,)
print(tuple_4)
tuple_5 = (1) # 实际上是一个 int
print(f"Type of tuple_5: {type(tuple_5)}")

# 访问与切片
# 索引访问，与List完全相同
tuple_fruits = ('Apple', 'Banana', 'Orange', 'Pear', 'Grape', 'Strawberry', 'Mango')
print(tuple_fruits[-1])
# 切片,与List完全相同
print(tuple_fruits[1:4])
print(tuple_fruits[::-1])
# 遍历：
for fruit in tuple_fruits:
    print(fruit)

# 元组的不可变性：
# tuple_fruits[0] = 'Pineapple' # TypeError: 'tuple' object does not support item assignment
# 但是如果元组中的元素类型本身是可修改的，则可以修改
tuple_fruits = ('Apple', ['Banana', 'Orange'], 'Pear', 'Grape', 'Strawberry', 'Mango')
tuple_fruits[1].append('Kiwi')
print(tuple_fruits)

# 基本操作方法
print(f'length of tuple_fruits: {len(tuple_fruits)}')
print(f'index of Pear: {tuple_fruits.index("Pear")}')
print(f'count of Orange: {tuple_fruits.count("Orange")}')
# 成员判断
print(f'Pear in tuple_fruits? -> {"Pear" in tuple_fruits}')
print(f'Pineapple is not in tuple_fruits? -> {"Pineapple" not in tuple_fruits}')
# 拼接和重复
print(tuple_fruits + ('Watermelon',))
print(tuple_fruits * 2)

# 元组的应用场景
# 1. 解包：将元组拆开
# Java中没有解包语法，只能逐个获取对象属性
person = ('Tom', 20, 'Male')
name, age, gender = person
print(name, age, gender)
# 2. 也可以用于函数中用于返回多个变量
# Java中则需要自己组织返回结果的对象
def get_uer_info():
    return 'Tom', 20, 'Male'
user_name, user_age, user_gender = get_uer_info()
print(user_name, user_age, user_gender)
# 3. 交换变量
# Java中需要使用临时变量
user_1 = 'Tom'
user_2 = 'Jerry'
user_1, user_2 = user_2, user_1
print(user_1, user_2)