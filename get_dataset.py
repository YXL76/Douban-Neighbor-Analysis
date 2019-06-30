import csv
import requests
from json import loads
from time import sleep

from settings import user_agent
from settings import uid_file
from settings import dataset_file
from settings import csv_title

session = requests.Session()


def get_movie_info(nuid=''):
    nurl = 'https://m.douban.com/rexxar/api/v2/user/' + nuid + '/collection_stats?type=movie&for_mobile=1&ck=5Kvd'
    nreferer = 'https://m.douban.com/people/' + nuid + '/movie_charts'
    nheaders = {
        'Referer': nreferer,
        'User-Agent': user_agent,
    }
    nresponse = session.get(url=nurl, headers=nheaders)
    nrow = []
    ndecoded = loads(nresponse.text)
    # print(decoded)
    try:
        nrow.append(ndecoded['total_collections'])
    except:
        nrow.append('')
    try:
        nrow.append(int(ndecoded['total_spent']))
    except:
        nrow.append('')
    try:
        nrow.append(int(ndecoded['total_cost']))
    except:
        nrow.append('')
    try:
        nrow.append(round(ndecoded['weekly_avg'], 1))
    except:
        nrow.append('')
    try:
        nrow.append(ndecoded['countries'][0]['name'])
    except:
        nrow.append('')
    try:
        nrow.append(ndecoded['countries'][1]['name'])
    except:
        nrow.append('')
    try:
        nrow.append(ndecoded['genres'][0]['name'])
    except:
        nrow.append('')
    try:
        nrow.append(ndecoded['genres'][1]['name'])
    except:
        nrow.append('')
    try:
        nrow.append(ndecoded['genres'][2]['name'])
    except:
        nrow.append('')
    # print(row)
    return nrow


def get_user_info(nuid=''):
    nurl = 'https://m.douban.com/rexxar/api/v2/user/' + nuid + '/archives_summary?for_mobile=1&ck=5Kvd'
    nreferer = 'https://m.douban.com/people/' + nuid + '/subject_profile'
    nheaders = {
        'Referer': nreferer,
        'User-Agent': user_agent,
    }
    nresponse = session.get(url=nurl, headers=nheaders)
    ndecoded = loads(nresponse.text)
    # print(decoded)
    nrow = []
    try:
        nrow.append(ndecoded['user']['loc']['name'])
    except:
        nrow.append('')
    try:
        nrow.append(ndecoded['user']['statuses_count'])
    except:
        nrow.append('')
    try:
        nrow.append(ndecoded['user']['reg_time'][:4])
    except:
        nrow.append('')
    try:
        nrow.append(ndecoded['user']['gender'])
    except:
        nrow.append('')
    # print(row)
    return nrow


def get_info(nuid=''):
    nrow = []
    nrow += get_user_info(nuid)
    nrow += get_movie_info(nuid)
    print(nrow)
    return nrow


def read_uid_file():
    with open(uid_file) as infile:
        with open(dataset_file, 'w', encoding='utf-8', newline='') as outfile:
            csv_file = csv.writer(outfile, dialect='excel')
            csv_file.writerow(csv_title)
            for line in infile:
                uid = line[:-1]
                # print(uid)
                csv_file.writerow(get_info(uid))
                sleep(2)


if __name__ == '__main__':
    read_uid_file()
