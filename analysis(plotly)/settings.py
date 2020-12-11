# 数据集文件名
dataset_file = "dataset_file.csv"

# plotly 账号
username = ""
api_key = ""

# Mapbox access token
mapbox_access_token = "pk.eyJ1IjoieXhsNzYiLCJhIjoiY2p4Z3lndzAxMDhyZTN4bXZlZXl4YzAyeSJ9.9gwBwf3n51J8ZXL-M7Nz8A"

# csv文件标题
csv_title = [
    "loc",
    "status",
    "year",
    "sex",
    "collect",
    "spend",
    "cost",
    "avg",
    "country1",
    "country2",
    "type1",
    "type2",
    "type3",
]

# 广播数量范围
status_range = (0, 500, 1000, 1500, 2000)

# 注册时间范围
reg_year_range = (
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
)

# 电影地区范围
country_range = (
    "中国大陆",
    "美国",
    "香港",
    "台湾",
    "日本",
    "韩国",
    "英国",
    "法国",
    "德国",
    "意大利",
    "西班牙",
    "印度",
    "泰国",
    "俄罗斯",
    "伊朗",
    "加拿大",
    "澳大利亚",
    "爱尔兰",
    "瑞典",
    "巴西",
    "丹麦",
)

# 电影类型范围
genre_range = (
    "剧情",
    "喜剧",
    "动作",
    "爱情",
    "科幻",
    "动画",
    "悬疑",
    "惊悚",
    "恐怖",
    "犯罪",
    "同性",
    "音乐",
    "歌舞",
    "传记",
    "历史",
    "战争",
    "西部",
    "奇幻",
    "冒险",
    "灾难",
    "武侠",
    "情色",
    "家庭",
    "短片",
    "纪录片",
)

# 纬度
loc_lat = {
    "北京": 39.894910,
    "天津": 39.085294,
    "重庆": 29.563761,
    "上海": 31.230378,
    "广州": 23.129162,
    "深圳": 22.543099,
    "东莞": 23.020536,
    "佛山": 23.021548,
    "珠海": 22.270715,
    "中山": 22.517645,
    "汕头": 23.354091,
    "惠州": 23.111847,
    "江门": 22.578738,
    "开平": 22.38025,
    "台山": 22.254284,
    "恩平": 22.176793,
    "湛江": 21.270707,
    "雷州": 20.924519,
    "揭阳": 23.549993,
    "肇庆": 23.047191,
    "茂名": 21.662999,
    "信宜": 22.358592,
    "韶关": 24.810403,
    "乐昌": 25.131541,
    "南雄": 25.112129,
    "潮州": 23.65695,
    "梅州": 24.288615,
    "兴宁": 24.1429,
    "河源": 23.743538,
    "清远": 23.681763,
    "英德": 24.19012,
    "连州": 23.719071,
    "汕尾": 22.786211,
    "阳江": 21.857958,
    "阳春": 22.165583,
    "云浮": 22.915094,
    "南京": 32.060255,
    "苏州": 31.298886,
    "昆山": 31.341479,
    "常熟": 31.649566,
    "张家港": 31.446084,
    "太仓": 31.441361,
    "无锡": 31.491169,
    "江阴": 31.889641,
    "宜兴": 31.362399,
    "常州": 31.810689,
    "徐州": 34.205768,
    "南通": 31.980171,
    "启东": 31.811591,
    "海门": 31.883544,
    "扬州": 32.39421,
    "高邮": 32.788889,
    "盐城": 33.347382,
    "东台": 32.765772,
    "大丰": 33.241831,
    "连云港": 34.596653,
    "镇江": 32.187849,
    "丹阳": 32.034448,
    "句容": 31.944999,
    "泰州": 32.455778,
    "靖江": 31.99775,
    "泰兴": 32.13105,
    "兴化": 32.904425,
    "淮安": 33.610353,
    "宿迁": 33.963232,
    "杭州": 30.274084,
    "临安": 30.237881,
    "富阳": 30.053477,
    "建德": 29.361498,
    "温州": 27.994267,
    "乐清": 28.108603,
    "瑞安": 27.766022,
    "宁波": 29.874556,
    "慈溪": 30.171619,
    "余姚": 30.043739,
    "奉化": 29.704064,
    "嘉兴": 30.746129,
    "桐乡": 30.540365,
    "海宁": 30.510659,
    "平湖": 30.6055,
    "台州": 28.656386,
    "温岭": 28.394813,
    "金华": 29.079059,
    "东阳": 29.28787,
    "永康": 28.914364,
    "兰溪": 29.209004,
    "义乌": 29.306841,
    "绍兴": 30.029752,
    "诸暨": 29.715452,
    "上虞": 30.010773,
    "湖州": 30.894348,
    "丽水": 28.46763,
    "龙泉": 28.47033,
    "舟山": 29.985295,
    "衢州": 28.970079,
    "江山": 28.711919,
    "成都": 30.572269,
    "都江堰": 30.998301,
    "崇州": 30.638921,
    "邛崃": 30.410275,
    "绵阳": 31.46745,
    "江油": 31.778025,
    "南充": 30.837793,
    "阆中": 31.558357,
    "德阳": 31.126855,
    "什邡": 31.10632,
    "达州": 31.209571,
    "乐山": 29.552106,
    "峨眉山": 29.568777,
    "宜宾": 28.751768,
    "泸州": 28.871811,
    "遂宁": 30.532847,
    "内江": 29.580228,
    "自贡": 29.33903,
    "广安": 30.455961,
    "眉山": 30.075439,
    "广元": 32.435435,
    "凉山": 27.88161,
    "巴中": 31.867903,
    "资阳": 30.128901,
    "攀枝花": 26.582347,
    "雅安": 29.980537,
    "阿坝": 31.899413,
    "济南": 36.651216,
    "章丘": 36.714252,
    "青岛": 36.067082,
    "即墨": 36.388599,
    "胶南": 35.875137,
    "平度": 36.798875,
    "烟台": 37.463822,
    "龙口": 37.649458,
    "蓬莱": 37.793492,
    "莱州": 37.180703,
    "海阳": 36.78421,
    "临沂": 35.104672,
    "潍坊": 36.706774,
    "青州": 36.680221,
    "诸城": 35.993683,
    "昌邑": 36.840528,
    "济宁": 35.414921,
    "曲阜": 35.588929,
    "邹城": 35.407158,
    "淄博": 36.813487,
    "泰安": 36.200252,
    "滨州": 37.38199,
    "德州": 37.434092,
    "禹城": 36.913845,
    "威海": 37.513068,
    "荣成": 37.16516,
    "文登": 37.203333,
    "乳山": 36.89397,
    "聊城": 36.456703,
    "菏泽": 35.23375,
    "枣庄": 34.810487,
    "日照": 35.416377,
    "东营": 37.434751,
    "莱芜": 36.213813,
    "郑州": 34.746599,
    "巩义": 34.723912,
    "新郑": 34.395562,
    "洛阳": 34.619682,
    "新乡": 35.303004,
    "辉县": 35.437625,
    "南阳": 32.990833,
    "安阳": 36.097577,
    "信阳": 32.146983,
    "平顶山": 33.766169,
    "汝州": 34.158356,
    "商丘": 34.414172,
    "许昌": 34.035506,
    "禹州": 34.14659,
    "周口": 33.626149,
    "焦作": 35.215892,
    "济源": 35.067243,
    "孟州": 34.907235,
    "开封": 34.797239,
    "驻马店": 33.011529,
    "濮阳": 35.761829,
    "漯河": 33.581412,
    "三门峡": 34.772493,
    "鹤壁": 35.747225,
    "武汉": 30.593098,
    "宜昌": 30.691967,
    "枝江": 30.43449,
    "宜都": 30.387128,
    "当阳": 30.833375,
    "襄阳": 32.008986,
    "老河口": 32.384311,
    "荆州": 30.335165,
    "洪湖": 29.825625,
    "十堰": 32.629397,
    "丹江口": 32.540157,
    "黄石": 30.199652,
    "大冶": 30.135161,
    "黄冈": 30.453905,
    "麻城": 31.158456,
    "孝感": 30.924568,
    "恩施": 30.272156,
    "利川": 30.279972,
    "咸宁": 29.841443,
    "赤壁": 29.722659,
    "荆门": 31.035423,
    "钟祥": 31.167503,
    "鄂州": 30.39194,
    "随州": 31.690215,
    "广水": 31.451131,
    "天门": 30.661214,
    "潜江": 30.402109,
    "神农架林区": 31.744897,
    "长沙": 28.228209,
    "衡阳": 26.89323,
    "耒阳": 26.422275,
    "常宁": 26.409654,
    "株洲": 27.82755,
    "邵阳": 27.238892,
    "城步": 26.363575,
    "郴州": 25.770509,
    "岳阳": 29.357104,
    "汨罗": 28.803828,
    "常德": 29.031673,
    "湘潭": 27.829738,
    "湘乡": 27.730646,
    "韶山": 27.903446,
    "怀化": 27.554978,
    "娄底": 27.700062,
    "冷水江": 27.685923,
    "永州": 26.420394,
    "益阳": 28.55386,
    "湘西": 28.311947,
    "吉首": 28.315052,
    "张家界": 29.117096,
    "福州": 26.074507,
    "福清": 26.071038,
    "长乐": 25.9605,
    "厦门": 24.479833,
    "泉州": 24.874132,
    "南安": 24.91467,
    "安溪县": 25.055955,
    "惠安县": 25.030781,
    "德化县": 25.491494,
    "漳州": 24.512948,
    "龙海": 24.446706,
    "莆田": 25.454084,
    "三明": 26.263406,
    "永安": 25.972389,
    "宁德": 26.665617,
    "福安": 27.101071,
    "南平": 26.641768,
    "武夷山": 27.75538,
    "邵武": 27.340327,
    "建瓯": 27.022727,
    "建阳": 27.326124,
    "龙岩": 25.075123,
    "漳平": 25.290185,
    "西安": 34.341568,
    "汉中": 33.06748,
    "咸阳": 34.329605,
    "兴平": 34.30225,
    "渭南": 34.499995,
    "韩城": 35.476788,
    "华阴": 34.566096,
    "宝鸡": 34.361979,
    "榆林": 38.28539,
    "延安": 36.585455,
    "安康": 32.684714,
    "商洛": 33.870422,
    "铜川": 34.896756,
    "沈阳": 41.805698,
    "新民": 41.992853,
    "大连": 38.914003,
    "瓦房店": 39.685108,
    "普兰店": 39.406854,
    "庄河": 39.680811,
    "鞍山": 41.108647,
    "海城": 40.832018,
    "岫岩": 40.28825,
    "锦州": 41.095119,
    "凌海": 41.17404,
    "丹东": 40.000499,
    "东港": 39.88031,
    "抚顺": 41.880872,
    "营口": 40.667012,
    "大石桥": 40.88172,
    "盖州": 40.394901,
    "朝阳": 41.585133,
    "盘锦": 41.119997,
    "葫芦岛": 40.711052,
    "兴城": 40.618559,
    "辽阳": 41.267244,
    "灯塔": 41.427201,
    "铁岭": 42.223769,
    "开原": 42.545563,
    "本溪": 41.294175,
    "阜新": 42.021619,
    "石家庄": 38.042307,
    "辛集": 37.944758,
    "保定": 38.873891,
    "涿州": 39.48421,
    "高碑店": 39.323332,
    "安国": 38.40963,
    "唐山": 39.630867,
    "遵化": 40.198446,
    "邯郸": 36.625657,
    "武安": 36.654066,
    "秦皇岛": 39.935385,
    "邢台": 37.070589,
    "沙河": 36.855693,
    "南宫": 37.213214,
    "沧州": 38.304477,
    "泊头": 38.073902,
    "黄骅": 38.372395,
    "廊坊": 39.538047,
    "三河": 40.013125,
    "霸州": 39.110119,
    "张家口": 40.824418,
    "衡水": 37.73892,
    "承德": 40.954071,
    "合肥": 31.820586,
    "芜湖": 31.352859,
    "阜阳": 32.890124,
    "安庆": 30.543494,
    "桐城": 31.03325,
    "蚌埠": 32.916287,
    "六安": 31.733699,
    "淮南": 32.625478,
    "马鞍山": 31.670452,
    "滁州": 32.301556,
    "天长": 32.686325,
    "宿州": 33.646373,
    "宣城": 30.940718,
    "亳州": 33.844582,
    "淮北": 33.955844,
    "黄山": 29.714655,
    "铜陵": 30.945429,
    "池州": 30.6648,
    "巢湖": 31.687172,
    "南昌": 28.682892,
    "赣州": 25.831829,
    "九江": 29.705077,
    "上饶": 28.454863,
    "德兴": 28.449285,
    "吉安": 27.113443,
    "井冈山": 27.104924,
    "抚州": 27.949217,
    "宜春": 27.815619,
    "丰城": 28.142302,
    "樟树": 28.049726,
    "高安": 28.426871,
    "景德镇": 29.268835,
    "萍乡": 27.622768,
    "新余": 27.817808,
    "鹰潭": 28.260189,
    "哈尔滨": 45.803775,
    "五常": 45.766868,
    "尚志": 45.769981,
    "大庆": 46.589309,
    "齐齐哈尔": 47.354348,
    "牡丹江": 44.551655,
    "绥芬河": 44.410252,
    "海林": 44.574342,
    "宁安": 44.341501,
    "穆棱": 44.523369,
    "佳木斯": 46.799922,
    "富锦": 47.250108,
    "绥化": 46.653845,
    "海伦": 47.456257,
    "鸡西": 45.295075,
    "双鸭山": 46.646508,
    "黑河": 50.245329,
    "五大连池": 48.540306,
    "鹤岗": 47.349916,
    "伊春": 47.727536,
    "铁力": 46.983316,
    "七台河": 45.771726,
    "大兴安岭": 52.335206,
    "南宁": 22.817002,
    "桂林": 25.273566,
    "柳州": 24.325502,
    "玉林": 22.636379,
    "北流": 22.706207,
    "北海": 21.481254,
    "梧州": 23.476962,
    "岑溪": 22.91835,
    "贵港": 23.11153,
    "钦州": 21.979933,
    "百色": 23.902333,
    "河池": 24.692931,
    "宜州": 24.259526,
    "贺州": 24.403582,
    "防城港": 21.68686,
    "东兴": 21.547822,
    "来宾": 23.750306,
    "崇左": 22.376532,
    "凭祥": 22.094485,
    "长春": 43.817071,
    "榆树": 44.798106,
    "德惠": 44.534016,
    "九台": 44.157031,
    "蛟河": 43.723713,
    "四平": 43.166419,
    "公主岭": 43.503352,
    "延边": 42.891253,
    "延吉": 42.906368,
    "敦化": 43.372413,
    "图们": 42.968044,
    "松原": 45.141789,
    "通化": 41.728401,
    "梅河口": 42.531391,
    "白城": 45.619641,
    "大安": 45.526635,
    "白山": 41.939994,
    "临江": 41.811979,
    "辽源": 42.887918,
    "太原": 37.87059,
    "临汾": 36.088005,
    "大宁": 36.4674,
    "侯马": 35.625949,
    "运城": 35.026412,
    "永济": 35.012363,
    "晋中": 37.687024,
    "介休": 37.024684,
    "大同": 40.076762,
    "大同县": 40.040295,
    "长治": 36.195386,
    "吕梁": 37.518314,
    "孝义": 37.141857,
    "汾阳": 37.279502,
    "晋城": 35.490701,
    "高平": 35.784643,
    "忻州": 38.416663,
    "原平": 38.731402,
    "阳泉": 37.856971,
    "朔州": 39.331595,
    "昆明": 24.880095,
    "安宁": 24.92614,
    "大理": 25.606486,
    "曲靖": 25.489999,
    "宣威": 26.21959,
    "个旧": 23.37291,
    "玉溪": 24.352036,
    "丽江": 26.855047,
    "昭通": 27.338257,
    "德宏": 24.433353,
    "西双版纳": 22.007351,
    "景洪": 22.012668,
    "保山": 25.112046,
    "楚雄": 25.045532,
    "普洱": 22.825065,
    "临沧": 23.877573,
    "迪庆": 27.818882,
    "怒江": 25.852547,
    "贵阳": 26.647661,
    "清镇": 26.556079,
    "遵义": 27.725654,
    "仁怀": 27.800339,
    "赤水": 28.589557,
    "凯里": 26.582676,
    "毕节": 27.302589,
    "安顺": 26.253072,
    "六盘水": 26.592666,
    "都匀": 26.305805,
    "铜仁": 27.731514,
    "兴义": 25.090127,
    "呼和浩特": 40.842585,
    "包头": 40.657449,
    "赤峰": 42.257817,
    "呼伦贝尔": 49.211574,
    "满洲里": 49.59011,
    "牙克石": 49.285568,
    "扎兰屯": 48.013733,
    "额尔古纳": 50.243102,
    "鄂尔多斯": 39.608266,
    "通辽": 43.65289,
    "巴彦淖尔": 40.743213,
    "兴安盟": 46.077561,
    "乌兰浩特": 46.061341,
    "阿尔山": 47.173362,
    "乌兰察布": 40.994785,
    "丰镇": 41.037857,
    "乌海": 39.655388,
    "阿拉善盟": 38.851892,
    "乌鲁木齐": 43.825592,
    "伊宁": 43.907003,
    "巴音郭楞": 41.764115,
    "库尔勒": 41.78196,
    "喀什": 39.4704,
    "石河子": 44.302,
    "克拉玛依": 45.579888,
    "阿克苏": 41.168779,
    "哈密": 42.818501,
    "阿勒泰": 47.844924,
    "塔城": 46.745364,
    "博尔塔拉": 44.905588,
    "吐鲁番": 42.951382,
    "和田": 37.114157,
    "克孜勒苏": 39.714526,
    "阿图什": 39.7161,
    "阿拉尔": 40.541914,
    "图木舒克": 39.864867,
    "五家渠": 44.161854,
    "兰州": 36.061089,
    "天水": 34.580863,
    "酒泉": 39.73241,
    "庆阳": 35.709077,
    "白银": 36.544756,
    "平凉": 35.543051,
    "张掖": 38.925875,
    "武威": 37.928264,
    "陇南": 33.400684,
    "定西": 35.580662,
    "临夏": 35.601182,
    "嘉峪关": 39.77313,
    "金昌": 38.520089,
    "甘南": 34.983385,
    "海口": 20.044001,
    "三亚": 18.252847,
    "琼海": 19.258341,
    "文昌": 19.493407,
    "万宁": 18.795143,
    "儋州": 19.521134,
    "保亭": 18.63913,
    "三沙": 16.831839,
    "陵水": 18.506048,
    "乐东": 18.750259,
    "五指山": 18.89757,
    "白沙": 19.368292,
    "琼中": 19.033369,
    "银川": 38.487193,
    "灵武": 38.102655,
    "吴忠": 37.99746,
    "青铜峡": 38.021302,
    "石嘴山": 38.983236,
    "中卫": 37.499972,
    "固原": 36.015855,
    "西宁": 36.617144,
    "海南": 20.017377,
    "海西": 37.377139,
    "海东": 36.502039,
    "玉树": 33.011674,
    "果洛": 34.471431,
    "拉萨": 29.645554,
    "日喀则": 29.266869,
    "林芝": 29.648943,
    "山南": 29.237137,
    "阿里": 32.501111,
    "昌都": 31.140969,
    "那曲": 31.476202,
    "台北": 30.597507,
    "台中": 26.085552,
    "高雄": 21.940174,
    "台南": 38.959846,
    "桃园县": 31.856173,
    "新竹": 49.215767,
    "屏東": 24.303391,
    "基隆": 28.863703,
}

# 经度
loc_lon = {
    "北京": 116.322056,
    "天津": 117.201538,
    "重庆": 106.550464,
    "上海": 121.473658,
    "广州": 113.264434,
    "深圳": 114.057868,
    "东莞": 113.751765,
    "佛山": 113.121416,
    "珠海": 113.576726,
    "中山": 113.392782,
    "汕头": 116.681972,
    "惠州": 114.416196,
    "江门": 113.081901,
    "开平": 112.700382,
    "台山": 112.798444,
    "恩平": 112.298865,
    "湛江": 110.359377,
    "雷州": 110.074096,
    "揭阳": 116.372831,
    "肇庆": 112.465091,
    "茂名": 110.925456,
    "信宜": 110.941963,
    "韶关": 113.597522,
    "乐昌": 113.346339,
    "南雄": 114.305285,
    "潮州": 116.622603,
    "梅州": 116.122238,
    "兴宁": 115.74182,
    "河源": 114.700447,
    "清远": 113.056031,
    "英德": 113.404718,
    "连州": 113.030321,
    "汕尾": 115.375278,
    "阳江": 111.982232,
    "阳春": 111.781667,
    "云浮": 112.044491,
    "南京": 118.796877,
    "苏州": 120.585315,
    "昆山": 120.974177,
    "常熟": 120.757951,
    "张家港": 120.768611,
    "太仓": 121.125358,
    "无锡": 120.31191,
    "江阴": 120.239272,
    "宜兴": 119.804423,
    "常州": 119.973987,
    "徐州": 117.284124,
    "南通": 120.894291,
    "启东": 121.65841,
    "海门": 121.123088,
    "扬州": 119.412966,
    "高邮": 119.442153,
    "盐城": 120.163561,
    "东台": 120.67086,
    "大丰": 120.686455,
    "连云港": 119.221611,
    "镇江": 119.425836,
    "丹阳": 119.603928,
    "句容": 119.168695,
    "泰州": 119.923116,
    "靖江": 120.265519,
    "泰兴": 119.92869,
    "兴化": 119.813436,
    "淮安": 119.015285,
    "宿迁": 118.275198,
    "杭州": 120.15507,
    "临安": 119.718891,
    "富阳": 119.923046,
    "建德": 119.23174,
    "温州": 120.699366,
    "乐清": 120.962254,
    "瑞安": 120.670928,
    "宁波": 121.550357,
    "慈溪": 121.260696,
    "余姚": 121.158368,
    "奉化": 121.420307,
    "嘉兴": 120.755486,
    "桐乡": 120.946602,
    "海宁": 120.680757,
    "平湖": 121.104062,
    "台州": 121.420757,
    "温岭": 121.391137,
    "金华": 119.647444,
    "东阳": 120.20354,
    "永康": 120.00237,
    "兰溪": 119.468317,
    "义乌": 120.075058,
    "绍兴": 120.580232,
    "诸暨": 120.247219,
    "上虞": 120.879182,
    "湖州": 120.086823,
    "丽水": 119.922796,
    "龙泉": 119.92579,
    "舟山": 122.207215,
    "衢州": 118.859457,
    "江山": 118.615602,
    "成都": 104.066541,
    "都江堰": 103.622689,
    "崇州": 103.660172,
    "邛崃": 103.464156,
    "绵阳": 104.679114,
    "江油": 104.745877,
    "南充": 106.110698,
    "阆中": 106.005047,
    "德阳": 104.397894,
    "什邡": 104.16573,
    "达州": 107.468023,
    "乐山": 103.765568,
    "峨眉山": 103.44706,
    "宜宾": 104.643215,
    "泸州": 105.442258,
    "遂宁": 105.592898,
    "内江": 105.058433,
    "自贡": 104.778442,
    "广安": 106.633212,
    "眉山": 103.848538,
    "广元": 105.843357,
    "凉山": 102.267335,
    "巴中": 106.747477,
    "资阳": 104.627636,
    "攀枝花": 101.718637,
    "雅安": 103.013261,
    "阿坝": 102.224653,
    "济南": 117.119999,
    "章丘": 117.533386,
    "青岛": 120.382639,
    "即墨": 120.453079,
    "胶南": 119.995514,
    "平度": 119.966661,
    "烟台": 121.447935,
    "龙口": 120.33355,
    "蓬莱": 120.757579,
    "莱州": 119.940154,
    "海阳": 121.149774,
    "临沂": 118.356448,
    "潍坊": 119.161755,
    "青州": 118.495978,
    "诸城": 119.424955,
    "昌邑": 119.402132,
    "济宁": 116.587098,
    "曲阜": 116.999748,
    "邹城": 116.967364,
    "淄博": 118.054927,
    "泰安": 117.087614,
    "滨州": 117.970703,
    "德州": 116.357464,
    "禹城": 116.653458,
    "威海": 122.120419,
    "荣成": 122.486658,
    "文登": 122.122944,
    "乳山": 121.54909,
    "聊城": 115.985371,
    "菏泽": 115.480656,
    "枣庄": 117.323725,
    "日照": 119.526888,
    "东营": 118.674767,
    "莱芜": 117.676723,
    "郑州": 113.625368,
    "巩义": 112.973372,
    "新郑": 113.740529,
    "洛阳": 112.45404,
    "新乡": 113.9268,
    "辉县": 113.773625,
    "南阳": 112.528321,
    "安阳": 114.392392,
    "信阳": 114.091023,
    "平顶山": 113.192661,
    "汝州": 112.839682,
    "商丘": 115.65637,
    "许昌": 113.85264,
    "禹州": 113.488505,
    "周口": 114.696951,
    "焦作": 113.241823,
    "济源": 112.601918,
    "孟州": 112.788658,
    "开封": 114.307581,
    "驻马店": 114.022298,
    "濮阳": 115.029215,
    "漯河": 114.016539,
    "三门峡": 111.200135,
    "鹤壁": 114.297272,
    "武汉": 114.305392,
    "宜昌": 111.286471,
    "枝江": 111.745082,
    "宜都": 111.449611,
    "当阳": 111.813143,
    "襄阳": 112.122414,
    "老河口": 111.672378,
    "荆州": 112.239741,
    "洪湖": 113.46875,
    "十堰": 110.79799,
    "丹江口": 111.513127,
    "黄石": 115.03852,
    "大冶": 114.980946,
    "黄冈": 114.872316,
    "麻城": 115.00442,
    "孝感": 113.916902,
    "恩施": 109.488172,
    "利川": 108.941379,
    "咸宁": 114.322492,
    "赤壁": 113.895547,
    "荆门": 112.199265,
    "钟祥": 112.586503,
    "鄂州": 114.894843,
    "随州": 113.382458,
    "广水": 113.972992,
    "天门": 113.175786,
    "潜江": 112.900079,
    "神农架林区": 110.675757,
    "长沙": 112.938814,
    "衡阳": 112.571997,
    "耒阳": 112.859795,
    "常宁": 112.406944,
    "株洲": 113.134002,
    "邵阳": 111.467791,
    "城步": 110.313225,
    "郴州": 113.014717,
    "岳阳": 113.128958,
    "汨罗": 113.084977,
    "常德": 111.698497,
    "湘潭": 112.944049,
    "湘乡": 112.52788,
    "韶山": 112.489801,
    "怀化": 109.998488,
    "娄底": 111.993497,
    "冷水江": 111.435092,
    "永州": 111.613445,
    "益阳": 112.35518,
    "湘西": 109.739172,
    "吉首": 109.718908,
    "张家界": 110.479191,
    "福州": 119.296494,
    "福清": 119.356275,
    "长乐": 119.5045,
    "厦门": 118.089425,
    "泉州": 118.675675,
    "南安": 118.50366,
    "安溪县": 118.186289,
    "惠安县": 118.796605,
    "德化县": 118.241094,
    "漳州": 117.647481,
    "龙海": 117.818197,
    "莆田": 119.007777,
    "三明": 117.638678,
    "永安": 117.378321,
    "宁德": 119.547932,
    "福安": 119.643429,
    "南平": 118.177708,
    "武夷山": 118.03688,
    "邵武": 117.492534,
    "建瓯": 118.304988,
    "建阳": 118.121833,
    "龙岩": 117.017536,
    "漳平": 117.419998,
    "西安": 108.940174,
    "汉中": 107.023323,
    "咸阳": 108.708991,
    "兴平": 108.468957,
    "渭南": 109.509786,
    "韩城": 110.442847,
    "华阴": 110.092301,
    "宝鸡": 107.237974,
    "榆林": 109.734589,
    "延安": 109.489727,
    "安康": 109.029022,
    "商洛": 109.940477,
    "铜川": 108.945233,
    "沈阳": 123.431474,
    "新民": 122.833155,
    "大连": 121.614682,
    "瓦房店": 121.993874,
    "普兰店": 121.974823,
    "庄河": 122.967328,
    "鞍山": 122.994329,
    "海城": 122.76299,
    "岫岩": 123.300667,
    "锦州": 121.127003,
    "凌海": 121.367298,
    "丹东": 124.354706,
    "东港": 124.151665,
    "抚顺": 123.957208,
    "营口": 122.235417,
    "大石桥": 122.341931,
    "盖州": 122.342192,
    "朝阳": 120.471504,
    "盘锦": 122.070714,
    "葫芦岛": 120.836932,
    "兴城": 120.760582,
    "辽阳": 123.236944,
    "灯塔": 123.327989,
    "铁岭": 123.726166,
    "开原": 124.034672,
    "本溪": 123.766485,
    "阜新": 121.670323,
    "石家庄": 114.51486,
    "辛集": 115.207701,
    "保定": 115.464806,
    "涿州": 116.01122,
    "高碑店": 115.880174,
    "安国": 115.329809,
    "唐山": 118.180193,
    "遵化": 117.948571,
    "邯郸": 114.538961,
    "武安": 114.134526,
    "秦皇岛": 119.600492,
    "邢台": 114.504844,
    "沙河": 114.496412,
    "南宫": 115.678558,
    "沧州": 116.838834,
    "泊头": 116.594292,
    "黄骅": 117.364605,
    "廊坊": 116.683752,
    "三河": 116.817363,
    "霸州": 116.387298,
    "张家口": 114.887543,
    "衡水": 115.670177,
    "承德": 117.96241,
    "合肥": 117.227239,
    "芜湖": 118.432941,
    "阜阳": 115.814204,
    "安庆": 117.063754,
    "桐城": 117.008099,
    "蚌埠": 117.389719,
    "六安": 116.521854,
    "淮南": 116.999932,
    "马鞍山": 118.506759,
    "滁州": 118.317106,
    "天长": 119.018127,
    "宿州": 116.964356,
    "宣城": 118.758816,
    "亳州": 115.778676,
    "淮北": 116.798265,
    "黄山": 118.337481,
    "铜陵": 117.812079,
    "池州": 117.491568,
    "巢湖": 117.351898,
    "南昌": 115.858197,
    "赣州": 114.935029,
    "九江": 116.00193,
    "上饶": 117.943433,
    "德兴": 117.940394,
    "吉安": 114.992509,
    "井冈山": 115.032138,
    "抚州": 116.358181,
    "宜春": 114.416778,
    "丰城": 115.771882,
    "樟树": 115.539708,
    "高安": 115.385422,
    "景德镇": 117.178419,
    "萍乡": 113.854556,
    "新余": 114.917346,
    "鹰潭": 117.069202,
    "哈尔滨": 126.534967,
    "五常": 126.613361,
    "尚志": 126.621361,
    "大庆": 125.103784,
    "齐齐哈尔": 123.918186,
    "牡丹江": 129.633163,
    "绥芬河": 131.147027,
    "海林": 129.399234,
    "宁安": 129.470989,
    "穆棱": 130.262283,
    "佳木斯": 130.318917,
    "富锦": 132.037686,
    "绥化": 126.968887,
    "海伦": 126.944605,
    "鸡西": 130.969333,
    "双鸭山": 131.159133,
    "黑河": 127.52856,
    "五大连池": 126.217017,
    "鹤岗": 130.297964,
    "伊春": 128.841147,
    "铁力": 128.018,
    "七台河": 131.003138,
    "大兴安岭": 124.71108,
    "南宁": 108.366543,
    "桂林": 110.290194,
    "柳州": 109.415953,
    "玉林": 110.164756,
    "北流": 110.35505,
    "北海": 109.119927,
    "梧州": 111.279115,
    "岑溪": 110.994913,
    "贵港": 109.598926,
    "钦州": 108.654146,
    "百色": 106.618201,
    "河池": 108.085261,
    "宜州": 108.599997,
    "贺州": 111.566694,
    "防城港": 108.353846,
    "东兴": 107.971826,
    "来宾": 109.221465,
    "崇左": 107.364711,
    "凭祥": 106.766293,
    "长春": 125.323544,
    "榆树": 126.534958,
    "德惠": 125.708664,
    "九台": 125.84728,
    "蛟河": 127.344501,
    "四平": 124.350398,
    "公主岭": 124.829026,
    "延边": 129.508946,
    "延吉": 129.509369,
    "敦化": 128.232013,
    "图们": 129.84371,
    "松原": 124.825117,
    "通化": 125.939697,
    "梅河口": 125.687039,
    "白城": 122.839024,
    "大安": 124.273046,
    "白山": 126.423587,
    "临江": 126.918087,
    "辽源": 125.143532,
    "太原": 112.548879,
    "临汾": 111.518976,
    "大宁": 110.7566,
    "侯马": 111.38059,
    "运城": 111.007528,
    "永济": 110.99813,
    "晋中": 112.752694,
    "介休": 111.905576,
    "大同": 113.300129,
    "大同县": 113.61244,
    "长治": 113.116255,
    "吕梁": 111.144319,
    "孝义": 111.7785,
    "汾阳": 111.78445,
    "晋城": 112.851831,
    "高平": 112.949732,
    "忻州": 112.734174,
    "原平": 112.711059,
    "阳泉": 113.580519,
    "朔州": 112.432825,
    "昆明": 102.832891,
    "安宁": 102.45548,
    "大理": 100.267638,
    "曲靖": 103.796167,
    "宣威": 104.12557,
    "个旧": 103.15404,
    "玉溪": 102.546543,
    "丽江": 100.22775,
    "昭通": 103.717465,
    "德宏": 98.584895,
    "西双版纳": 100.797777,
    "景洪": 100.808095,
    "保山": 99.161761,
    "楚雄": 101.528068,
    "普洱": 100.966512,
    "临沧": 100.079583,
    "迪庆": 99.702234,
    "怒江": 98.853097,
    "贵阳": 106.630153,
    "清镇": 106.470715,
    "遵义": 106.927389,
    "仁怀": 106.409374,
    "赤水": 105.698132,
    "凯里": 107.97599,
    "毕节": 105.283992,
    "安顺": 105.947593,
    "六盘水": 104.830359,
    "都匀": 107.515768,
    "铜仁": 109.189598,
    "兴义": 104.918194,
    "呼和浩特": 111.74918,
    "包头": 109.840347,
    "赤峰": 118.886856,
    "呼伦贝尔": 119.765744,
    "满洲里": 117.459644,
    "牙克石": 120.71177,
    "扎兰屯": 122.737467,
    "额尔古纳": 120.180506,
    "鄂尔多斯": 109.781327,
    "通辽": 122.243444,
    "巴彦淖尔": 107.387657,
    "兴安盟": 122.067042,
    "乌兰浩特": 122.136802,
    "阿尔山": 119.945586,
    "乌兰察布": 113.132585,
    "丰镇": 113.110717,
    "乌海": 106.794249,
    "阿拉善盟": 105.728969,
    "乌鲁木齐": 87.616848,
    "伊宁": 81.322694,
    "巴音郭楞": 86.145298,
    "库尔勒": 86.2129,
    "喀什": 75.989755,
    "石河子": 86.035478,
    "克拉玛依": 84.889207,
    "阿克苏": 80.260605,
    "哈密": 93.514916,
    "阿勒泰": 88.141253,
    "塔城": 82.980316,
    "博尔塔拉": 82.066159,
    "吐鲁番": 89.189651,
    "和田": 79.922211,
    "克孜勒苏": 76.167819,
    "阿图什": 76.168392,
    "阿拉尔": 81.285884,
    "图木舒克": 79.069332,
    "五家渠": 87.523308,
    "兰州": 103.834303,
    "天水": 105.724947,
    "酒泉": 98.494483,
    "庆阳": 107.643631,
    "白银": 104.138559,
    "平凉": 106.66524,
    "张掖": 100.449818,
    "武威": 102.638011,
    "陇南": 104.921841,
    "定西": 104.626282,
    "临夏": 103.210538,
    "嘉峪关": 98.289152,
    "金昌": 102.188043,
    "甘南": 102.911027,
    "海口": 110.198293,
    "三亚": 109.511909,
    "琼海": 110.474648,
    "文昌": 109.856655,
    "万宁": 110.391073,
    "儋州": 109.580811,
    "保亭": 109.70259,
    "三沙": 112.338695,
    "陵水": 110.037503,
    "乐东": 109.173054,
    "五指山": 109.707867,
    "白沙": 108.789941,
    "琼中": 109.838389,
    "银川": 106.230909,
    "灵武": 106.340054,
    "吴忠": 106.198393,
    "青铜峡": 106.078818,
    "石嘴山": 106.383303,
    "中卫": 105.196902,
    "固原": 106.24261,
    "西宁": 101.778228,
    "海南": 110.349228,
    "海西": 97.369751,
    "海东": 102.104287,
    "玉树": 97.091934,
    "果洛": 100.244808,
    "拉萨": 91.140856,
    "日喀则": 88.880583,
    "林芝": 94.361558,
    "山南": 91.773134,
    "阿里": 80.105804,
    "昌都": 97.17202,
    "那曲": 92.051239,
    "台北": 114.277985,
    "台中": 119.330345,
    "高雄": 111.585587,
    "台南": 121.353897,
    "桃园县": 118.591385,
    "新竹": 119.760742,
    "屏東": 109.438957,
    "基隆": 88.906326,
}
