favorite_languages = {
    "jen":"python",
    "search":"c",
    "edward":"ruby",
    "phil":"python",
}

for key,value in favorite_languages.items():
    print(key+" favorite languages is "+value)
#遍历字典中的 键
for name in favorite_languages.keys():
    print(name.title())
#遍历字典中的 值
for value in favorite_languages.values():
    print(value)

#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name)

print("\n")
#剔除列表中的重复项
for language in set(favorite_languages.values()):

    print(language)