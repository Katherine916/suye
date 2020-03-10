cars = ["bmw","audi","toyota","subaru"]
# sort() 列表按字母顺序排列,永久性排序
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#sorted() 临时性排序

print(sorted(cars))
print(cars)

#reverse()  反转列表元素的排列顺序 永久改变顺序，但是可以再次调用改为原来的顺序
cars.reverse()
print(cars)
cars.reverse()
print(cars)
#len()确定列表的长度
print(len(cars))