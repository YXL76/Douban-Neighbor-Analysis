# Douban-Neighbor-Analysis

## 环境

### windows10 Pro 1903

- Python 3.7.3 [MSC v.1915 64 bit (AMD64)]
  - pandas 0.24.2
  - plotly 3.10.0
  - cufflinks 0.16
  - pyecharts 1.2.1

### Manjaro Linux 18.0.4 (Linux 4.19)

- Python 3.7.3 [GCC 8.2.1 20181127]
  - pandas 0.24.2
  - plotly 3.10.0
  - cufflinks 0.16
  - pyecharts 1.2.1

## 目录

.
├── analysis(plotly)
│   ├── analysis.ipynb
│   └── settings.py
├── analysis(pyecharts)
│   ├── analysis.ipynb
│   └── settings.py
├── example
│   ├── dataset_file.csv
│   ├── result(plotly)
│   ├── result(pyecharts)
│   ├── spider
│   │   └── settings.py
│   └── uid_file.txt
├── README.md
└── spider
    ├── settings.py
    ├── spider.ipynb
    └── spider.py

## 项目逻辑

### Part1 数据获取

<font color='red'> *若已有数据集可以跳过此部分，从Part2开始* </font>

- 该部分程序位于`spider`文件夹中，提供了`.py`和`.ipynb`文件

- 使用前请先设置`settings.py`中的`user_agent`，`cookie`，`target_user`

  - 获取方法

    ![](/Tutorial/Tutorial-1.png)

### Part2 数据分析

<font color='red'> *若已有数据集可以直接从此开始* </font>

- 该部分程序位于`analysis`文件夹中，提供了`.ipynb`文件，基于两种不同的包
- 由于两种包提供的图表有一定的差别，所以处理方法有些许不同，推荐使用`plotly`

#### plotly

- 需要联网，绘制地图需要`Mapbox`的`access token`，绘制图表需要`plotly `的`api key`，请在`settings.py`中设置
- 每日有使用次数限制，如果出现`TimeOut`的错误，请尝试更换网络

#### pyecharts

- 不需要联网
- 可导出文件，或直接在`notebook`中显示

## 样例

- 样例位于`example`文件夹中
- 其中的`dataset_file.csv`可直接用于数据分析，其所对应的配置文件位于`example\spider\settings.py`
- `result`文件夹中包含了把`example\dataset_file.csv`作为数据集后分别使用两种包分析得到的结果

## 相关链接

- [豆瓣](https://www.douban.com/)
- [Python Graphing Library, Plotly](https://plot.ly/python/)
- [pyecharts - A Python Echarts Plotting Library](https://pyecharts.org/#/)