# 回车桌面图片下载
import os
import requests
from lxml import etree

#url = "https://www.enterdesk.com/bizhi/50790.html"
url = "https://mm.enterdesk.com/bizhi/51794.html"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

response = requests.get(url, headers=headers)  # 获取网页
html_str = response.content.decode()  # 将页面内容转换成字符串
html = etree.HTML(html_str)  # 构造了一个XPath解析对象并对HTML文本进行自动修正

img_list = html.xpath("//div[@class='swiper-wrapper']/div/a/img/@src")  # 创建图片地址列表，获取图片地址
# print(img_list)   #到这里可打印一下看看获取到的图片地址列表是否正确，最后可注释掉这行
img_name = html.xpath("//h1[@class='myarc_h1']/text()")[0].replace(" ", "")  # 获取图片标题,replace替换掉标题中的空格
# print(img_name)     #到这里可打印一下看看获取到的图片名称是否正确，最后可注释掉这行
try:
    os.mkdir("{}".format(img_name))  # 在程序目录下创建一个以“图片标题”命名的文件夹用来保存这一组图片
except:
    pass

for url in img_list:
    url = url.replace("edpic_360_360", "edpic_source")  # 将小图地址替换成大图地址
    filename = url.split("/")[-1]  # 获取图片文件名，split截取从后往前到第一个反斜杠的字符串
    # print(filename)      #可打印一下文件名看是否获取成功，最后可注释掉这行
    f = requests.get(url, headers=headers)  # 获取网页地址
    with open(".\\{0}\\{1}".format(img_name, filename), "wb") as code:  # 下载文件
        code.write(f.content)
        print("【{}】高清图片下载完成。".format(filename))

print("全部图片下载完成，保存在程序目录下【{}】文件夹下".format(img_name))