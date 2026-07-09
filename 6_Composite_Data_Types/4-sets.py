# 集合是不可变且无序的，可以看作是隐藏了key的字典
# 通常用于去重，集合运算（交集，并集，差集）
# 元素必须要为Hashable可哈希类型，因为集合基于HashTable

# 集合的创建
# 直接使用{}
set_1 = {'a', 'b', 'c'}
print(set_1)
# 通过set()方法
list_1 = [1,2,3,4,5]
set_2 = set(list_1)
print(set_2)
# 注意：创建空set不能使用 {}，此时创建的是空字典
set_3 = {} # 实际上是空字典
print(f'type of set_3: {type(set_3)}')
set_4 = set()
print(f'type of set_4: {type(set_4)}')

# 集合的基本操作
set_fruits = {'apple', 'banana', 'orange', 'pear', 'grape', 'strawberry', 'mango'}
# 1. 新增元素
# 由于无序性，不能使用append()和insert()等基于索引的方法
set_fruits.add('kiwi')
set_fruits.add('apple') # 元素重复添加也只会替换
print(set_fruits)
# 2. 删除元素
set_fruits.remove('apple') # 如果元素不存在会报错
set_fruits.discard('pen') # 如果元素不存在不会报错
ele_deleted = set_fruits.pop() # 随机删除
print(ele_deleted)
print(set_fruits)
# 3. 长度和成员判断
print(len(set_fruits))
print('apple' in set_fruits)

# 集合运算
set_1 = {1,2,3}
set_2 = {3,4,5}
# 并集 | : 合并两个集合，不重复
set_union = set_1 | set_2
print(set_union)
set_union_2 = set_1.union(set_2)
print(set_union_2)
# 交集 & ： 取相同的元素
set_intersection = set_1 & set_2
print(set_intersection)
set_intersection_2 = set_1.intersection(set_2)
print(set_intersection_2)
# 差集 ^ : 去掉相同的元素再合并
set_difference = set_1 ^ set_2
print(set_difference)
set_difference_2 = set_1.difference(set_2)
print(set_difference_2)

# 子集与超集判断
set_3 = {1,2}
set_4 = {1,2,3}
print(set_3.issubset(set_4)) # 是否为子集
print(set_4.issuperset(set_3)) # 是否为超集
print(set_3.isdisjoint(set_4)) # 是否无交集

# 集合推导式
# 快速创建集合
set_5 = {x for x in range(10)}
print(set_5)
set_5_square = {x**2 for x in range(10)}
print(set_5_square)
set_5_even = {x for x in range(10) if x % 2 == 0}
print(set_5_even)
# 快速获取质数
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True
set_primes = {x for x in range(2,100) if is_prime(x)}
print(set_primes)
# java 中需要使用Stream
# List<Integer> primeSet = IntStream.range(2,100)
#                                   .map(x -> x*2)
#                                   .boxed()
#                                   .collect(Collectors.toSet())