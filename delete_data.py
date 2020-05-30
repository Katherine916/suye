# -*- coding: utf-8 -*-

# 导入 requests
import requests
import json
from urllib import parse

check_user = parse.quote('[{"field":"create_user_name","op":"eq","values":"世茂生产测试账号"}]')


# 查询的sit接口
check_url = "http://web.pscc.shimaogroup.com:8080/data/{}?pageNo=1&pageSize=999999&params="+check_user
# 删除的sit接口
delete_url = 'http://web.pscc.shimaogroup.com:8080/data/{}'



allapi_dict = {

    'label': 'label',                                            #标签
    'image': 'image',                                            #影像
    'ticket':'ticket',                                           #单证
    'configDataMapping':'configDataMapping',                     #识别规则
    'configDataMappingItem':'configDataMappingItem',             #识别规则细则
    'ticketInvoice':'ticketInvoice',                             #增值税发票
    'ticketTrain':'ticketTrain',
    'ticketMany':'ticketMany',
    'ticketAttachment':'ticketAttachment',
    'ticketTaxi':'ticketTaxi'
}


api_dict = {

    'image': 'image'                                       #影像
    # 'ticket':'ticket',                                       #单证
    # 'ticketInvoice':'ticketInvoice',                         #增值税发票
    # 'ticketTrain':'ticketTrain',
    # 'ticketMany':'ticketMany',
    # 'ticketAttachment':'ticketAttachment',
    # 'ticketTaxi':'ticketTaxi',
    #'baseBill':'baseBill',
    #'salesBill':'salesBill'

}


checkdata = []
def check_func(api_type):
    new_check_url = check_url.format(api_dict.get(api_type))
    response = requests.get(new_check_url)
    # 查询数据
    if response.status_code == 200:
    #获取到查询结果的数据json解码后赋值给 result
        result = json.loads(response.text)
    #获取到字典中key为 list的值
        lists = result["list"]
    for list in lists:
        mylist = list["id"]
        checkdata.append(mylist)
    return checkdata


# 删除查询到的列表数据
def delete_func(delete_list,api_type):

    new_delete_url = delete_url.format(api_dict.get(api_type))
    for data in delete_list:
        requests.delete(url=new_delete_url, params={"ids[]": data})


if __name__ == '__main__':

    i=400;
    while i>0:
     for myname in api_dict:

      delete_func(check_func(myname),myname)

      i=i-1;
      print(str(i)+"删除结束！！！！！！！")
