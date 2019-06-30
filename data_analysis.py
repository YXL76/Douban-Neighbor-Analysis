import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from settings import dataset_file
from settings import follower_range
from settings import reg_year_range
from settings import gender_range
from settings import loc_range
from settings import loc_id
from settings import loc_dic

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

follower_num = list(0 for fi in range(len(follower_range)))
loc_num = list(0 for li in range(len(loc_range)))
reg_year_num = list(0 for ri in range(len(reg_year_range)))
gender_num = list(0 for gi in range(len(gender_range)))


def draw_bar_chart(label, num):
    ind = np.arange(len(label))
    index = 0
    while index < len(ind):
        ind[index] *= 6
        index += 1
    top = int(max(num) * 1.2)

    rects = plt.bar(ind, num, 0.4, color='#FFC46C')
    plt.xlabel('range')
    plt.ylabel('numbers')
    plt.xticks(ind, label)
    plt.yticks(np.arange(0, top, int(top / 10)))
    plt.title('followers')
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 2, str(height), ha='center', va='bottom')
    plt.show()


def draw_pie_chart(label, num):
    fig1, ax = plt.subplots()
    ax.pie(num, autopct='%.1f%%', shadow=True, startangle=90)
    ax.legend(label, loc='upper right')
    ax.set_aspect('equal')
    plt.show()


def item_analysis(item, item_range, item_num):
    index = 0
    while index <= len(item_range):
        if index == len(item_range) or item < item_range[index]:
            if index > 0:
                item_num[index - 1] += 1
            break
        index += 1
    # print(item_num)


def loc_analysis(item):
    if item == '':
        loc_num[loc_id['未知']] += 1
        return
    loc = loc_dic.get(item)
    if loc is None:
        loc_num[loc_id['国外']] += 1
    else:
        loc_num[loc_id[loc]] += 1


def gender_analysis(item):
    if item == 'M':
        gender_num[0] += 1
    elif item == 'F':
        gender_num[1] += 1
    else:
        gender_num[2] += 1


def read_dataset_file():
    outfile = open(dataset_file, 'r', encoding='utf-8')
    csv_file = csv.reader(outfile)
    for item in csv_file:
        # 如果当前行为空，或者未获取都用户信息（用户已注销）
        if len(item) == 0 or item[0] == '':
            continue
        # print(item)
        item_analysis(int(item[0]), follower_range, follower_num)
        loc_analysis(item[1])
        item_analysis(int(item[3]), reg_year_range, reg_year_num)
        gender_analysis(item[4])

    label = []
    index = 1
    while index < len(follower_range):
        label.append(str(follower_range[index - 1]) + '~' + str(follower_range[index]))
        index += 1
    label.append(str(follower_range[-1]) + '+')
    # print(label)
    draw_bar_chart(label, follower_num)
    draw_bar_chart(loc_range, loc_num)
    draw_pie_chart(reg_year_range, reg_year_num)
    draw_pie_chart(gender_range, gender_num)


if __name__ == '__main__':
    read_dataset_file()
