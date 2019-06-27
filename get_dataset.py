import csv
import requests
from json import loads
from time import sleep

from settings import user_agent, uid_file, dataset_file

session = requests.Session()


def get_book_info(uid=''):
    url = 'https://m.douban.com/rexxar/api/v2/user/' + uid + '/collection_stats?type=book&for_mobile=1'
    referer = 'https://m.douban.com/people/' + uid + '/book_charts'
    headers = {
        'Referer': referer,
        'User-Agent': user_agent,
    }
    response = session.get(url=url, headers=headers)
    row = []
    decoded = loads(response.text)
    # print(decoded)
    try:
        row.append(decoded['total_collections'])
    except:
        row.append('')
    try:
        row.append(int(decoded['total_spent']))
    except:
        row.append('')
    try:
        row.append(int(decoded['total_page']))
    except:
        row.append('')
    try:
        row.append(round(decoded['monthly_avg'], 1))
    except:
        row.append('')
    # print(row)
    return row


def get_movie_info(uid=''):
    url = 'https://m.douban.com/rexxar/api/v2/user/' + uid + '/collection_stats?type=movie&for_mobile=1&ck=5Kvd'
    referer = 'https://m.douban.com/people/' + uid + '/movie_charts'
    headers = {
        'Referer': referer,
        'User-Agent': user_agent,
    }
    response = session.get(url=url, headers=headers)
    row = []
    decoded = loads(response.text)
    # print(decoded)
    try:
        row.append(decoded['total_collections'])
    except:
        row.append('')
    try:
        row.append(int(decoded['total_spent']))
    except:
        row.append('')
    try:
        row.append(int(decoded['total_cost']))
    except:
        row.append('')
    try:
        row.append(round(decoded['weekly_avg'], 1))
    except:
        row.append('')
    # print(row)
    return row


def get_user_info(uid=''):
    url = 'https://m.douban.com/rexxar/api/v2/user/' + uid + '/archives_summary?for_mobile=1&ck=5Kvd'
    referer = 'https://m.douban.com/people/' + uid + '/subject_profile'
    headers = {
        'Referer': referer,
        'User-Agent': user_agent,
    }
    response = session.get(url=url, headers=headers)
    decoded = loads(response.text)
    # print(decoded)
    row = []
    try:
        row.append(decoded['user']['followers_count'])
    except:
        row.append('')
    try:
        row.append(decoded['user']['loc']['name'])
    except:
        row.append('')
    try:
        row.append(decoded['user']['statuses_count'])
    except:
        row.append('')
    try:
        row.append(decoded['user']['reg_time'][:4])
    except:
        row.append('')
    try:
        row.append(decoded['user']['gender'])
    except:
        row.append('')
    # print(row)
    return row


def write_to_file(uid=''):
    row = []
    row += get_user_info(uid)
    row += get_movie_info(uid)
    row += get_book_info(uid)
    print(row)
    return row


def read_from_file():
    infile = open(uid_file)
    outfile = open(dataset_file, 'w', encoding='utf-8', newline='')
    csv_file = csv.writer(outfile, dialect='excel')
    line = 'temporary'
    while line:
        line = infile.readline()
        uid = line[:-1]
        # print(uid)
        csv_file.writerow(write_to_file(uid))
        sleep(1)
    infile.close()
    outfile.close()


if __name__ == '__main__':
    read_from_file()
