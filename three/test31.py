travels = ["xm","bj","frans","janpan","england"]

print("这是原始的排列顺序")
print(travels)
print("使用sorted方法临时改变顺序")
print(sorted(travels))
print("这是原始的排列顺序")
print(travels)

print("使用sorted 按与字母相反的顺序打印")
print(sorted(travels,reverse=True))
print("这是原始的排列顺序")
print(travels)


travels.reverse()
print(travels)

print("使用reserve方法将列表恢复为原始")
travels.reverse()
print(travels)

travels.sort()
print(travels)

travels.sort(reverse=True)
print(travels)

print(len(travels))