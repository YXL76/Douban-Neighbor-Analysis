import csv
import requests
from json import loads
from time import sleep
from bs4 import BeautifulSoup

from settings import (
    user_agent,
    cookie,
    target_user,
    uid_file,
    dataset_file,
    csv_title,
)

session = requests.Session()

# target_user 为目标用户的 uid
url = "https://www.douban.com/people/" + target_user + "/rev_contacts"
# 查看豆瓣的友邻页面需要登陆账号，所以使用 cookie 模拟登录
headers = {
    "User-Agent": user_agent,
    "Cookie": cookie,
}


# 获取观影信息
def get_movie_info(nuid=""):
    nurl = (
        "https://m.douban.com/rexxar/api/v2/user/"
        + nuid
        + "/collection_stats?type=movie&for_mobile=1&ck=5Kvd"
    )
    nreferer = "https://m.douban.com/people/" + nuid + "/movie_charts"
    nheaders = {
        "Referer": nreferer,
        "User-Agent": user_agent,
    }
    nresponse = session.get(url=nurl, headers=nheaders)
    # 返回的数据为 json 格式，使用 loads 解析
    ndecoded = loads(nresponse.text)
    nrow = []
    # print(decoded)
    # 观影数
    try:
        nrow.append(ndecoded["total_collections"])
    except:
        nrow.append("")
    # 观看时间
    try:
        nrow.append(int(ndecoded["total_spent"]))
    except:
        nrow.append("")
    # 消费
    try:
        nrow.append(int(ndecoded["total_cost"]))
    except:
        nrow.append("")
    # 平均每周观看时间
    try:
        nrow.append(round(ndecoded["weekly_avg"], 1))
    except:
        nrow.append("")
    # 以下两项为最常观看地区
    try:
        nrow.append(ndecoded["countries"][0]["name"])
    except:
        nrow.append("")
    try:
        nrow.append(ndecoded["countries"][1]["name"])
    except:
        nrow.append("")
    # 以下三项为最常观看类型
    try:
        nrow.append(ndecoded["genres"][0]["name"])
    except:
        nrow.append("")
    try:
        nrow.append(ndecoded["genres"][1]["name"])
    except:
        nrow.append("")
    try:
        nrow.append(ndecoded["genres"][2]["name"])
    except:
        nrow.append("")
    # print(row)
    return nrow


# 获取账户信息
def get_user_info(nuid=""):
    nurl = (
        "https://m.douban.com/rexxar/api/v2/user/"
        + nuid
        + "/archives_summary?for_mobile=1&ck=5Kvd"
    )
    nreferer = "https://m.douban.com/people/" + nuid + "/subject_profile"
    nheaders = {
        "Referer": nreferer,
        "User-Agent": user_agent,
    }
    nresponse = session.get(url=nurl, headers=nheaders)
    # 返回的数据为 json 格式，使用 loads 解析
    ndecoded = loads(nresponse.text)
    # print(decoded)
    nrow = []
    # 用户所在地区
    try:
        nrow.append(ndecoded["user"]["loc"]["name"])
    except:
        nrow.append("")
    # 用户广播数
    try:
        nrow.append(ndecoded["user"]["statuses_count"])
    except:
        nrow.append("")
    # 用户注册时间
    try:
        nrow.append(ndecoded["user"]["reg_time"][:4])
    except:
        nrow.append("")
    # 用户性别
    try:
        nrow.append(ndecoded["user"]["gender"])
    except:
        nrow.append("")
    # print(row)
    return nrow


def get_info(nuid=""):
    nrow = []
    nrow += get_user_info(nuid)
    nrow += get_movie_info(nuid)
    print(nrow)
    return nrow


# 读取本地 uid 文件，获取所有友邻数据，写入数据集
def read_uid_file():
    with open(uid_file) as infile:
        with open(dataset_file, "w", encoding="utf-8", newline="") as outfile:
            csv_file = csv.writer(outfile, dialect="excel")
            csv_file.writerow(csv_title)
            for line in infile:
                uid = line[:-1]
                # print(uid)
                csv_file.writerow(get_info(uid))
                sleep(2)


# 爬取所有友邻列表页面，获取所有友邻的 uid ，保存至本地
def write_uid_file(num):
    with open(uid_file, "w") as file:
        # 每页显示最多 70 个友邻
        for i in range(0, num, 70):
            current_url = url + "?start=" + str(i)
            # print(current_url)
            response = session.get(url=current_url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            peoples = soup.select("#content > div > div.article > dl > dt > a")
            for people in peoples:
                uid = (BeautifulSoup(str(people), "lxml").a["href"])[30:-1]
                print(uid)
                file.write(uid + "\n")


# 从爬取的页面中获取用户的友邻总数
def get_num(soup):
    # css 选择器
    num = soup.select("#db-usr-profile > div.info > h1")
    num = BeautifulSoup(str(num[0]), "lxml").string
    print(num)
    # 数字从倒数第二个字符开始
    length = len(num) - 2
    while "0" <= num[length] <= "9":
        length -= 1
    num = int(num[length + 1 : len(num) - 1])
    print(num)
    return num


def get_neighbors():
    response = session.get(url=url, headers=headers)
    if response.status_code != 200:
        print("获取失败，请检查cookie, uid")
        return False
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup)
    print("获取成功")
    write_uid_file(get_num(soup))
    return True


if __name__ == "__main__":
    if get_neighbors():
        read_uid_file()
