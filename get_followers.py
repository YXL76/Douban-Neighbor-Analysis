import requests
from bs4 import BeautifulSoup

from settings import user_agent
from settings import cookie
from settings import target_user
from settings import uid_file

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
    num = int(num[length + 1:len(num) - 1])
    print(num)
    return num


def write_to_file(num):
    with open(uid_file, "w") as file:
        for i in range(0, num, 70):
            current_url = url + '?start=' + str(i)
            # print(current_url)
            response = session.get(url=current_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            peoples = soup.select('#content > div > div.article > dl > dt > a')
            for people in peoples:
                # print(BeautifulSoup(str(people), 'lxml').a['href'])
                # 将各个友邻的主页地址写入文件
                uid = (BeautifulSoup(str(people), 'lxml').a['href'])[30:-1]
                print(uid)
                file.write(uid + '\n')


def get_followers():
    response = session.get(url=url, headers=headers)
    if response.status_code != 200:
        print('获取失败')
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    num = get_num(soup)
    # print(num)
    write_to_file(num)
    print('获取成功')


if __name__ == '__main__':
    get_followers()
