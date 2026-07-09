# 列表的创建
# 与java的区别：ArrayList<Integer> nums = new ArrayList<>();
#   1. 不需要提前声明元素类型和个数
#   2. java需要对象实例化操作
# 直接创建
list1 = []
print(list1)
print(type(list1))
list2 = [1, 2, 3, True, False, 'hello']
print(list2)
# list() 函数创建方法
list3 = list('12345678') # 类型转换：str-->list
print(list3)

print('-'*20)

# 列表的索引
# 1. 超出索引会报 index error
# 2. -1 同样表示最后一个索引
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[0])
print(fruits[-1])
# 列表的切片 [start:end:step]
# 1. 同样是左闭右开
# 2. step 可以为负数，表示倒序
# 3. java 没有切片，需要手动遍历或者使用stream流处理
print(fruits[1:3])
print(fruits[::-1])
print(fruits[::2])

print('-'*20)

# 列表的加法和乘法
# 注意：列表的加法和乘法都不是针对单个元素的运算，而是整体扩容
print(list3 + list2)
print(list3 * 3)

print('-'*20)

# 修改与添加
# 修改元素，直接通过索引修改
fruits[0] = 'pear'
print(fruits)
# 新增元素
# 1. 通过 append() 在末尾添加
# 2. 通过 insert(index, obj) 在指定位置添加
# 3. 在java中使用 .add()
fruits.append('grape')
fruits.insert(0, 'watermelon')
print(fruits)
# 合并多个列表
# 1. 直接使用 +
# 2. a.extend(b)，注意extend表示原地追加，直接将b追加到a中，a直接被修改，返回值为None
# 3. java中使用 list1.addAll(list2)
list4 = list2+list3
print(list4)
list5 = list2.extend(list3)
print(list2)
# 删除元素
# 1. 使用 remove() 删除指定元素
# 2. 使用 pop() 删除指定的索引位置的元素，有返回值
# 3. 使用 del 删除指定索引位置的元素
# 4. 使用 clear 清空列表
fruits_2 = fruits.copy() # 复制列表，浅复制（不复制内存地址，2中引用），不影响原列表
fruits_2.remove('watermelon')
print(fruits_2)
element_pop = fruits_2.pop(0) # 弹出列表中的第一个元素，返回值
print(element_pop)
del fruits_2[0] # 删除列表中的第一个元素
print(fruits_2)
fruits_2.clear() # 清空列表
print(fruits_2)

print('-'*20)

# 常用操作和函数
# 统计与查找
nums = [1,2,2,2,3,4,5,5,6]
print("Element 2 show %d times." %nums.count(2))
print("Element 2 first show in the list at %s." %nums.index(2))
# 排序和反转
# 注意：排序和反转都是原地反转，直接修改列表
nums.sort()
print(nums)
nums.reverse()
print(nums)
# 长度和成员判断
print(len(nums))
print(2 in nums)
# 复制列表
# 1. 使用 copy 浅拷贝，不复制内存地址，不影响原列表
nums_copy = nums.copy()
print(nums_copy)
# 2. 直接使用切片
nums_copy_2 = nums[:]
print(nums_copy_2)

# 嵌套列表/多维列表
# 在DA中通常使用Series和DataFrame，而非原生多维列表
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1]) # 访问第一行第二个元素

# 列表推导式 List Comprehension
# Python中提供了简洁的语法来生成列表
# [表达式 for 变量 in 可迭代对象 if 条件]
# 生成一个0-9的元素
list_nums = [x for x in range(10)]
print(list_nums)
# 生成0-9的平方
list_squares = [x**2 for x in range(10)]
print(list_squares)
# 生成0-9的偶数
list_evens = [x for x in range(10) if x%2==0]
print(list_evens)
# java中没有对应的语法，但是可以配合Stream处理
# List<Integer> list_evens = IntStream.range(0,10)
#                                     .filter(x -> x % 2 == 0)
#                                     .boxed()
#                                     .collect(Collectors.toList());

# 生成2-100的质数
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True
list_primes = [x for x in range(2,100) if is_prime(x)]
print(list_primes)