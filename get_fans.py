import requests
from time import sleep
from bs4 import BeautifulSoup

from settings import user_agent, cookie, target_user, uid_file

session = requests.Session()
url = 'https://www.douban.com/people/' + target_user + '/rev_contacts'
headers = {
    'User-Agent': user_agent,
    'Cookie': cookie,
}


# 获取友邻数
def get_num(soup):
    num = soup.select('#db-usr-profile > div.info > h1')
    num = BeautifulSoup(str(num[0]), 'lxml').string
    length = len(num) - 2
    while '0' < num[length] < '9':
        length -= 1
    return int(num[length + 1:len(num) - 1])


def write_to_file(num):
    file = open(uid_file, "w")
    # 遍历所有友邻页面
    for i in range(0, num, 70):
        current_url = url + '?start=' + str(i)
        # print(current_url)
        response = session.get(url=current_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, 'lxml')
        peoples = soup.select('#content > div > div.article > dl > dt > a')
        for people in peoples:
            # print(BeautifulSoup(str(people), 'lxml').a['href'])
            # 将各个友邻的主页地址写入文件
            file.write((BeautifulSoup(str(people), 'lxml').a['href'])[30:-1] + '\n')
    file.close()


def get_fans():
    # 目标用户友邻列表
    response = session.get(url=url, headers=headers)
    if response.status_code != 200:
        print('获取失败')
        return False
    sleep(1)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    num = get_num(soup)
    # print(num)
    write_to_file(num)
    print('获取成功')
    return True


if __name__ == '__main__':
    get_fans()
