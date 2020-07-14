# -*- coding: utf-8 -*-

# 导入 requests
import requests
import json
from urllib import parse

check_user = parse.quote('[{"field":"create_user_name","op":"eq","values":"益海嘉里测试账号FAT"}]')

#无条件删除
# check_user = parse.quote('[]')

# 查询/删除的FAT接口
check_url = "http://elephant-image-fat.phoenix-t.xforceplus.com/data/{}?pageNo=1&pageSize=9999&params=" + check_user
delete_url = 'http://elephant-image-fat.phoenix-t.xforceplus.com/data/{}'

# 查询/删除的SIT接口
# check_url = "http://elephant-image-sit.phoenix-t.xforceplus.com/data/{}?pageNo=1&pageSize=9999&params=" + check_user
# delete_url = 'http://elephant-image-sit.phoenix-t.xforceplus.com/data/{}'

# #查询/删除的UAT接口
# check_url = "http://web.pscc-uat.shimaogroup.com/data/{}?pageNo=1&pageSize=9999&params="+check_user
# delete_url = 'http://web.pscc-uat.shimaogroup.com//data/{}'

#益海嘉里
# check_url = "https://fsscscpuat-image.wilmar.cn/data/{}?pageNo=1&pageSize=9999&params="+ check_user
# delete_url = 'https://fsscscpuat-image.wilmar.cn/data/{}'




checkdata = []


def check_func(api_type):
    new_check_url = check_url.format(api_dict.get(api_type))
    response = requests.get(new_check_url)
    # 查询数据
    if response.status_code == 200:
        # 获取到查询结果的数据json解码后赋值给 result
        result = json.loads(response.text)
        # 获取到字典中key为 list的值
        lists = result["list"]
    for list in lists:
        mylist = list["id"]
        checkdata.append(mylist)
    return checkdata


# 删除查询到的列表数据
def delete_func(delete_list, api_type):
    new_delete_url = delete_url.format(api_dict.get(api_type))
    for data in delete_list:
        requests.delete(url=new_delete_url, params={"ids[]": data})


if __name__ == '__main__':

    for myname in api_dict:
        delete_func(check_func(myname), myname)
print("删除结束！！！！！！！")
