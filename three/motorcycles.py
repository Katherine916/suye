# 修改列表中的某元素
motorcycles = ["honda","yamah","suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)

# append() 在列表末尾添加元素
motorcycles.append("ducatiss")
print(motorcycles)

#insert() 在列表中插入数据

motorcycles.insert(0,"first")
print(motorcycles)

#del 删除列表中的元素  删除后无法再使用
del motorcycles[0]
print(motorcycles)

#pop() 删除末尾元素，删除后还能接着使用被删除的元素
pop_motorcycles = motorcycles.pop()
print(motorcycles)
print(pop_motorcycles)

#remove()  不知道删除元素的位置，但是知道删除元素的值 可用此方法,删除后还可以使用这个值（只能删除第一个指定的值，如果有多个 需要用循环）
motorcycles.remove("yamah")
print(motorcycles)