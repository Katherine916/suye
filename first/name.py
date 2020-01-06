name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

print("\nLanguages:\nPython\nC\nJava")
#换行
print("\n\tLanguages:\n\tPython\n\tC\n\tJava")

"""
去除有空白的字符串
lstrip()    去除开头有空白的字符串
rstrip()    去除结尾有空白的字符串
strip()     去除首尾有空白的字符串

使用此方法只是暂时删除了空格，若要永久删除，需要将结果存到变量中
"""

favorite_lanauge = " Python "
print(favorite_lanauge)
print(favorite_lanauge.lstrip())
print(favorite_lanauge.rstrip())
print(favorite_lanauge.strip())




