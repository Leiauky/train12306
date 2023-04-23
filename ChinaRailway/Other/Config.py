import re
from requests import Session

from Other.MyError import MyError


class UserConfig(object):
    def __init__(self):
        raise MyError(error_messages='UserConfig对象不能被创建。')

    # 12306登录用户名
    USERNAME = ""
    # 12306登录密码
    PASSWORD = ""
    # 12306绑定证件号后四位
    CAST_NUM = ""


class MailConfig(object):
    def __init__(self):
        raise MyError(error_messages='MailConfig对象不能被创建。')

    # SMTP_SERVER = 'outlook.office365.com'
    SMTP_SERVER = 'outlook.office365.com'
    # USER = '***@outlook.com' 邮箱账号
    USER = ''
    # PASSWORD = '123456' 邮箱授权密码
    PASSWORD = ''
    # TO_ADDRS = ['12345****@qq.com','****@outlook.com']
    TO_ADDRS = []


class PathConfig(object):

    def __init__(self):
        raise MyError(error_messages="PathConfig对象不能被创建。")

    __ms_edge_driver_path = r'resources\EdgeDrive/msedgedriver_109.0.1518.8.exe'

    @classmethod
    def get_ms_edge_driver_path(cls) -> str:
        """
        返回Edge驱动路径
        :return:
        """
        return cls.__ms_edge_driver_path

    __stealth_min_js_path = r'resources\Js/stealth.min.js'

    @classmethod
    def get_stealth_min_js_path(cls) -> str:
        """
        返回stealth.min.js路径
        :return:
        """
        return cls.__stealth_min_js_path

    __init_dc_root_path = r'resources\Temp/html'

    @classmethod
    def get_init_dc_root_path(cls) -> str:
        """
        返回保存initDC.html的根路径
        :return:
        """
        return cls.__init_dc_root_path


class UrlConfig(object):
    """
    url
    """

    def __init__(self):
        raise MyError(error_messages="UrlConfig对象不能被创建。")

    __station_name_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'

    @classmethod
    def get_station_name_url(cls) -> str:
        """
        返回车站名称Url
        :return: 
        """
        return cls.__station_name_url

    # 12306首页Url
    __index_url = 'https://www.12306.cn/index/'

    @classmethod
    def get_index_url(cls) -> str:
        """
        返回首页Url
        :return: 
        """
        return cls.__index_url

    # 12306登录相关Url
    __login_url = 'https://kyfw.12306.cn/otn/resources/login.html'

    @classmethod
    def get_login_url(cls) -> str:
        """
        返回登录页面Url
        :return: 
        """
        return cls.__login_url

    __qr64_url = 'https://kyfw.12306.cn/passport/web/create-qr64'

    @classmethod
    def get_qr64_url(cls) -> str:
        """
        返回创建登录二维码Url
        :return: 
        """
        return cls.__qr64_url

    __check_qr_url = 'https://kyfw.12306.cn/passport/web/checkqr'

    @classmethod
    def get_check_qr_url(cls) -> str:
        """
        返回检测二维码状态Url
        :return: 
        """
        return cls.__check_qr_url

    __message_code_url = 'https://kyfw.12306.cn/passport/web/getMessageCode'

    @classmethod
    def get_message_code_url(cls) -> str:
        """
        返回请求12306发送短信验证码Url
        :return: 
        """
        return cls.__message_code_url

    __passport_login_url = 'https://kyfw.12306.cn/passport/web/login'

    @classmethod
    def get_passport_login_url(cls) -> str:
        """
        返回密码登录12306Url
        :return: 
        """
        return cls.__passport_login_url

    __uam_tk_url = 'https://kyfw.12306.cn/passport/web/auth/uamtk'

    @classmethod
    def get_uam_tk_url(cls) -> str:
        """
        返回设置cookies_uamtk并获取newapptk参数Url
        :return: 
        """
        return cls.__uam_tk_url

    __uam_auth_client_url = 'https://kyfw.12306.cn/otn/uamauthclient'

    @classmethod
    def get_uam_auth_client_url(cls) -> str:
        """
        返回设置cookies_tk参数Url
        :return: 
        """
        return cls.__uam_auth_client_url


    # 个人信息相关Url
    __passengers_query_url = 'https://kyfw.12306.cn/otn/passengers/query'
    @classmethod
    def get_passengers_query_url(cls) -> str:
        """
        返回乘车人信息Url
        :return:
        """
        return cls.__passengers_query_url

    # 信息查询
    __train_search_url = 'https://search.12306.cn/search/v1/train/search'
    @classmethod
    def get_train_search_url(cls) -> str:
        """
        返回车次基本信息Url
        :return:
        """
        return cls.__train_search_url
    # 车票查询相关Url
    __left_ticket_query_url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'

    @classmethod
    def get_left_ticket_query_url(cls) -> str:
        """
        返回车票查询Url
        :return: 
        """
        return cls.__left_ticket_query_url

    __query_ticket_price_url = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice'

    @classmethod
    def get_query_ticket_price_url(cls) -> str:
        """
        返回车票价格查询Url
        :return: 
        """
        return cls.__query_ticket_price_url

    __check_user_url = 'https://kyfw.12306.cn/otn/login/checkUser'

    @classmethod
    def get_check_user_url(cls) -> str:
        """
        返回检测用户是否登录Url
        :return: 
        """
        return cls.__check_user_url

    __submit_order_request_url = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'

    @classmethod
    def get_submit_order_request_url(cls) -> str:
        """
        返回提交预约订单Url
        :return: 
        """
        return cls.__submit_order_request_url

    # 车票预约相关Url
    __init_dc_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'

    @classmethod
    def get_init_dc_url(cls) -> str:
        """
        返回单程初始化页面Url
        :return: 
        """
        return cls.__init_dc_url

    __passenger_dtos_url = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'

    @classmethod
    def get_passenger_dtos_url(cls) -> str:
        """
        返回乘客信息Url
        :return: 
        """
        return cls.__passenger_dtos_url

    __check_order_info_url = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'

    @classmethod
    def get_check_order_info_url(cls) -> str:
        """
        返回检测订单信息Url
        :return: 
        """
        return cls.__check_order_info_url

    __queue_count_url = 'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount'

    @classmethod
    def get_queue_count_url(cls) -> str:
        """
        返回余票数量Url
        :return: 
        """
        return cls.__queue_count_url

    # 车票下单相关Url
    __confirm_single_for_queue_url = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue'

    @classmethod
    def get_confirm_single_for_queue_url(cls) -> str:
        """
        返回确认下单Url
        :return: 
        """
        return cls.__confirm_single_for_queue_url

    __query_order_wait_time_url = 'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime'

    @classmethod
    def get_query_order_wait_time_url(cls) -> str:
        """
        返回下单结果Url
        :return: 
        """
        return cls.__query_order_wait_time_url

    __result_order_for_dc_queue_url = 'https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue'

    @classmethod
    def get_result_order_for_dc_queue_url(cls) -> str:
        """
        返回订单详细信息Url
        :return: 
        """
        return cls.__result_order_for_dc_queue_url


class GlobalConfig(object):
    """
    公共配置类
    """

    def __init__(self):
        raise MyError(error_messages="GlobalConfig对象不能被创建。")

    __sm4_key = 'tiekeyuankp12306'
    __headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.12306.cn',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.95',
    }

    @classmethod
    def get_headers(cls) -> dict:
        """
        返回请求头
        :return:
        """
        return GlobalConfig.__headers

    __station_name = {'北京北': 'VAP', '北京东': 'BOP', '北京': 'BJP', '北京南': 'VNP', '北京大兴': 'IPP', '北京西': 'BXP', '北京朝阳': 'IFP',
                      '重庆北': 'CUW', '重  庆北': 'WAI', '重庆': 'CQW', '重庆南': 'CRW', '重  庆西': 'WWI', '重庆西': 'CXW',
                      '上海': 'SHH', '上海南': 'SNH', '上海虹桥': 'AOH', '上海西': 'SXH', '天津北': 'TBP', '天津': 'TJP', '天津南': 'TIP',
                      '天津西': 'TXP', '万象': 'YTM', '滨江': 'BJB', '百浪': 'BRZ', '班猫箐': 'BNM', '北营': 'BIV', '长春': 'CCT',
                      '长春南': 'CET', '长春西': 'CRT', '成  都东': 'WEI', '成都东': 'ICW', '成都南': 'CNW', '成  都': 'WBI',
                      '成都': 'CDW', '成都西': 'CMW', '陈官营': 'CAJ', '长沙': 'CSQ', '长沙南': 'CWQ', '长沙西': 'RXQ', '常庄': 'CVK',
                      '大成': 'DCT', '大拟': 'DNZ', '读书铺': 'DPM', '大王滩': 'DZZ', '大元': 'DYZ', '丰水村': 'FSJ', '福州': 'FZS',
                      '福  州': 'GAI', '福州南': 'FYS', '福州 南': 'FXS', '甘草店': 'GDJ', '钢城': 'GAK', '孤家子': 'GKT', '广南卫': 'GNM',
                      '贵阳': 'GIW', '贵  阳北': 'WNI', '贵阳北': 'KQW', '贵阳东': 'KEW', '广州北': 'GBQ', '广州东': 'GGQ', '广州': 'GZQ',
                      '广州南': 'IZQ', '广州西': 'GXQ', '哈尔滨北': 'HTB', '哈尔滨': 'HBB', '哈  尔  滨': 'BAI', '哈尔滨东': 'VBB',
                      '哈尔滨西': 'VAB', '合肥北城': 'COH', '合肥': 'HFH', '合肥南': 'ENH', '合肥 南': 'HAI', '皇姑屯': 'HTT',
                      '呼和浩特东': 'NDC', '呼和浩特': 'HHC', '海口东': 'HMQ', '海口': 'VUQ', '杭州东': 'HGH', '杭州': 'HZH', '杭州南': 'XHH',
                      '金马村': 'JMM', '济南': 'JNK', '济  南': 'EEI', '济南东': 'MDK', '济南西': 'JGK', '济  南西': 'EII', '昆明': 'KMM',
                      '昆明南': 'KOM', '历城': 'VHK', '蔺家楼': 'ULK', '龙泉寺': 'UQJ', '拉萨': 'LSO', '乐善村': 'LUM', '林盛堡': 'LBT',
                      '骆驼巷': 'LTJ', '莱芜北': 'VIK', '兰州东': 'LVJ', '兰州': 'LZJ', '兰州新区': 'LQJ', '兰州西': 'LAJ', '茂舍祖': 'MOM',
                      '南 昌': 'NOG', '南昌': 'NCG', '宁村': 'NCZ', '南昌西': 'NXG', '南京': 'NJH', '南京南': 'NKH', '那罗': 'ULZ',
                      '南宁东': 'NFZ', '南宁': 'NNZ', '南宁西': 'NXZ', '那铺': 'NPZ', '暖泉': 'NQJ', '坡底下': 'PXJ', '七甸': 'QDM',
                      '世博园': 'ZWT', '石家庄北': 'VVP', '石家庄东': 'SXP', '邵家堂': 'SJJ', '石家庄': 'SJP', '施家嘴': 'SHM', '沈阳': 'SYT',
                      '沈阳北': 'SBT', '沈阳东': 'SDT', '沈阳南': 'SOT', '水源': 'OYJ', '沈阳西': 'OOT', '桑园子': 'SAJ', '太原北': 'TBV',
                      '太原东': 'TDV', '太原南': 'TNV', '太原': 'TYV', '武汉': 'WHN', '武汉东': 'LFN', '王家湾': 'WJJ', '乌鲁木齐南': 'WMR',
                      '乌鲁木齐': 'WAR', '吴圩机场': 'WJZ', '王兆屯': 'WZB', '西安北': 'EAY', '西安': 'XAY', '西固城': 'XUJ', '西街口': 'EKM',
                      '许家台': 'XTJ', '西宁': 'XNO', '小哨': 'XAM', '雪野': 'XYK', '银川': 'YIJ', '永丰营': 'YYM', '一间堡': 'YJT',
                      '宜耐': 'YVM', '羊堡': 'ABM', '榆树台': 'YUT', '引镇': 'CAY', '朱家窑': 'ZUJ', '章丘南': 'VQK', '郑州东': 'ZAF',
                      '郑州航空港': 'ZIF', '郑州': 'ZZF', '郑州西': 'XPF', '昂昂溪': 'AAX', '阿城北': 'ABB', '阿城': 'ACB', '安达': 'ADX',
                      '安德': 'ARW', '阿尔山北': 'ARX', '阿尔山': 'ART', '安吉': 'AJU', '安靖': 'PYW', '安家': 'AJB', '安康': 'AKY',
                      '阿克苏': 'ASR', '阿克陶': 'AER', '阿拉尔': 'AOR', '阿里河': 'AHX', '阿拉山口': 'AKR', '阿勒泰': 'AUR', '安陆': 'ALN',
                      '安陆西': 'AXN', '安平': 'APT', '安庆': 'AQH', '安庆西': 'AIU', '安顺': 'ASW', '鞍山': 'AST', '安顺西': 'ASE',
                      '鞍山西': 'AXT', '安亭北': 'ASH', '安亭西': 'AXU', '安阳': 'AYF', '安阳东': 'ADF', '北安': 'BAB', '博白': 'BBZ',
                      '蚌埠南': 'BMH', '蚌埠': 'BBH', '巴楚': 'BCR', '白城': 'BCT', '北辰': 'BII', '宝坻北': 'BPP', '八达岭长城': 'VLP',
                      '保定东': 'BMP', '北戴河': 'BEP', '保定': 'BDP', '八达岭': 'ILP', '巴东': 'BBN', '八方山': 'FGQ', '柏果': 'BGM',
                      '北海': 'BHZ', '布海': 'BUT', '滨海': 'YKP', '滨海北': 'FCP', '白河': 'BEL', '滨海西': 'FHP', '毕节': 'BOE',
                      '宝鸡': 'BJY', '白涧': 'BAP', '宝鸡南': 'BBY', '北京丰台': 'FTP', '白奎堡': 'BKB', '博克图': 'BKX', '博乐': 'BER',
                      '巴林': 'BLX', '勃利': 'BLB', '白马井': 'BFQ', '八面通': 'BMB', '北票': 'BPT', '宝清': 'BUB', '宝泉岭': 'BQB',
                      '百色': 'BIZ', '白山市': 'HJL', '北台': 'BTT', '包头 东': 'FDC', '包头东': 'BDC', '包头': 'BTC', '北屯市': 'BXR',
                      '宾西北': 'BBB', '本溪': 'BXT', '步行街': 'BWW', '宾阳': 'UKZ', '白云鄂博': 'BEC', '白云北': 'BVE', '白云机场北': 'BBA',
                      '白洋淀': 'FWP', '背荫河': 'BYB', '百宜': 'FHW', '巴彦高勒': 'BAC', '鲅鱼圈': 'BYT', '白银西': 'BXJ', '白云西': 'BXE',
                      '彬州东': 'BFY', '巴中': 'IEW', '滨州': 'BIK', '亳州': 'BZH', '宾州': 'BZB', '亳州南': 'BNU', '查布嘎': 'CBC',
                      '赤壁': 'CBN', '长白山': 'CUL', '常德': 'VGQ', '承德': 'CDP', '长甸': 'CDT', '承德南': 'IVP', '曹妃甸东': 'POP',
                      '赤峰': 'CID', '曹妃甸港': 'PGP', '赤峰南': 'CFD', '嵯岗': 'CAX', '柴岗': 'CGT', '长葛北': 'CGF', '柴沟堡': 'CGV',
                      '城固': 'CGY', '成高子': 'CZB', '草海': 'WBW', '巢湖东': 'GUH', '柴河': 'CHB', '巢湖': 'CIH', '从江': 'KNW',
                      '蔡家崖': 'EBV', '长乐东': 'CIS', '长乐': 'CAS', '长临河': 'FVH', '慈利': 'CUQ', '茶陵': 'CDG', '崇礼': 'KOP',
                      '昌黎': 'CLP', '长流': 'CLA', '长乐南': 'CVS', '晨明': 'CMB', '苍南': 'CEH', '昌平北': 'VBP', '常平东': 'FQQ',
                      '昌平': 'CPP', '长庆桥': 'CQJ', '崇仁': 'CRG', '长寿北': 'COW', '潮汕': 'CBQ', '察素齐': 'CSC', '朝天': 'CTE',
                      '长汀南': 'CNS', '朝天南': 'CTY', '昌图': 'CTT', '昌图西': 'CPT', '长汀镇': 'CDB', '长武': 'CWY', '苍溪': 'CXE',
                      '辰溪': 'CXQ', '磁县': 'CIP', '楚雄': 'CUM', '曹县': 'CXK', '城西': 'CIA', '长兴南': 'CFH', '陈相屯': 'CXT',
                      '春阳': 'CAL', '潮阳': 'CNQ', '朝阳川': 'CYL', '朝阳湖': 'CYE', '滁州北': 'CUH', '常州北': 'ESH', '长治北': 'CBF',
                      '长治东': 'CUF', '长征': 'CZJ', '池州': 'IYH', '滁州': 'CXH', '郴州': 'CZQ', '沧州': 'COP', '常州': 'CZH',
                      '长治': 'CZF', '崇州': 'CZE', '崇左南': 'COZ', '崇左': 'CZZ', '郴州西': 'ICQ', '沧州西': 'CBP', '大安北': 'RNT',
                      '东安东': 'DCZ', '达坂城': 'DCR', '定边': 'DYJ', '东岔': 'DCJ', '丹东': 'DUT', '东方': 'UFQ', '丹凤': 'DGY',
                      '大丰': 'KRQ', '东方红': 'DFB', '大方南': 'DNE', '东风南': 'DPJ', '东港北': 'RGT', '东莞东': 'DMQ', '东莞南': 'DNA',
                      '大孤山': 'RMT', '东莞': 'RTQ', '东莞西': 'WGQ', '大红旗': 'DQD', '大虎山': 'DHD', '敦化': 'DHL', '敦煌': 'DHJ',
                      '德惠': 'DHT', '德惠西': 'DXT', '东京城': 'DJB', '达家沟': 'DJT', '垫江': 'DJE', '道滘': 'RRQ', '大涧': 'DFP',
                      '杜家': 'DJL', '洞井': 'FWQ', '都江堰': 'DDW', '洞口': 'DKA', '大连北': 'DFT', '德令哈': 'DHO', '达连河': 'DCB',
                      '大荔': 'DNY', '大理': 'DKM', '大连': 'DLT', '大明湖': 'JAK', '得莫利': 'DTB', '东明县': 'DNF', '定南': 'DNG',
                      '定南南': 'DIG', '大埔': 'DPI', '大庆东': 'LFX', '大庆': 'DZX', '对青山': 'DQB', '大庆西': 'RHX', '东胜': 'DOC',
                      '独山': 'RWW', '砀山南': 'PRH', '大石桥': 'DQT', '东胜西': 'DYC', '大同南': 'DMV', '大同': 'DTV', '大屯': 'DNT',
                      '大通西': 'DTO', '大武口': 'DFJ', '党武': 'DWE', '定西北': 'DNJ', '大兴机场': 'IWP', '定西': 'DSJ', '东乡': 'DXG',
                      '大兴': 'DXX', '德阳': 'DYW', '当阳': 'DYN', '丹阳': 'DYH', '大冶北': 'DBN', '大英东': 'IAW', '都匀东': 'KJW',
                      '东营': 'DPK', '大邑': 'DEE', '东营南': 'DOK', '大杨树': 'DUX', '都匀': 'RYW', '德州东': 'DIP', '定州东': 'DOP',
                      '邓州东': 'DDF', '东至': 'DCH', '达州': 'RXW', '德州': 'DZP', '定州': 'DXP', '邓州': 'DOF', '峨边': 'EBW',
                      '鄂尔多斯': 'EEC', '额济纳': 'EJC', '二连': 'RLC', '峨眉': 'EMW', '峨眉山': 'IXW', '恩施': 'ESN', '鄂州': 'ECN',
                      '防城港北': 'FBZ', '福鼎': 'FES', '肥东': 'FIH', '丰都': 'FUW', '发耳': 'FEM', '福海': 'FHR', '凤凰机场': 'FJQ',
                      '凤凰城': 'FHT', '汾河': 'FEV', '奉化': 'FHH', '富锦': 'FIB', '范家屯': 'FTT', '涪陵北': 'FEW', '风陵渡': 'FLV',
                      '涪陵': 'FLW', '富拉尔基': 'FRX', '福利区': 'FLJ', '阜宁东': 'FDU', '富宁': 'FNM', '福清': 'FQS', '福泉': 'VMW',
                      '芙蓉南': 'KCQ', '抚顺北': 'FET', '富顺': 'FSE', '佛山': 'FSQ', '扶绥': 'FSZ', '佛山西': 'FOQ', '福田': 'NZQ',
                      '凤县': 'FXY', '阜新': 'FOT', '肥西': 'FAH', '阜新南': 'FXD', '阜阳': 'FYH', '富阳': 'FYU', '扶余北': 'FBT',
                      '分宜': 'FYG', '富蕴': 'FYR', '富源': 'FYM', '抚远': 'FYB', '富裕': 'FYX', '阜阳西': 'FXU', '丰镇': 'FZC',
                      '凤州': 'FZY', '抚州': 'FZG', '方正': 'FNB', '广安南': 'VUW', '广安': 'VJW', '高安': 'GCG', '贵  安': 'WDI',
                      '贵安': 'GAE', '古北口': 'GKP', '藁城': 'GEP', '藁城南': 'GUP', '高村': 'GCV', '古东': 'GDV', '格尔木': 'GRO',
                      '贵港': 'GGZ', '甘谷': 'GGJ', '根河': 'GEX', '高花': 'HGD', '古交': 'GJV', '皋兰': 'GEJ', '桂林北': 'GBZ',
                      '高楞': 'GLB', '桂林': 'GLZ', '古莲': 'GRX', '甘洛': 'VOW', '公庙子': 'GMC', '广南县': 'GXM', '桂平': 'GAZ',
                      '共青城': 'GAG', '固始': 'GXN', '广水': 'GSN', '谷山': 'FFQ', '观沙岭': 'FKQ', '干塘': 'GNJ', '广通北': 'GPM',
                      '古田会址': 'STS', '高兴': 'VWW', '高邑': 'GIP', '巩义': 'GXF', '巩义南': 'GYF', '固原': 'GUJ', '广元': 'GYW',
                      '赣榆': 'GYU', '高邑西': 'GNP', '高州': 'GSQ', '赣州': 'GZG', '公主岭': 'GLT', '公主岭南': 'GBT', '冠豸山': 'GPS',
                      '盖州西': 'GAT', '赣州西': 'GOG', '淮安东': 'HAU', '淮安': 'AUH', '红安西': 'VXN', '淮北': 'HRH', '鹤北': 'HMB',
                      '淮滨': 'HVN', '河边': 'HBV', '湖潮东': 'HCE', '韩城': 'HCY', '合川': 'WKW', '珲春': 'HUL', '潢川': 'KCN',
                      '海城': 'HCT', '花城街': 'HCA', '黄村': 'HCP', '海城西': 'HXT', '邯郸': 'HDP', '河东机场': 'HFJ', '邯郸东': 'HPP',
                      '惠东': 'KDQ', '哈达铺': 'HDJ', '花都': 'HAA', '洪洞西': 'HTV', '横道河子': 'HDB', '霍尔果斯': 'HFR', '鹤岗': 'HGB',
                      '黄冈东': 'KAN', '红果': 'HEM', '汉沽': 'HGP', '红光镇': 'IGW', '红河': 'HHM', '黑河': 'HJB', '浑河': 'HHT',
                      '怀化南': 'KAQ', '黄河景区': 'HCF', '怀化': 'HHQ', '后湖': 'IHN', '和静': 'HJR', '河津': 'HJV', '怀集': 'FAQ',
                      '华家': 'HJT', '河口北': 'HBM', '宏克力': 'OKB', '河口南': 'HKJ', '汉口': 'HKN', '呼兰': 'HUB', '葫芦岛北': 'HPD',
                      '葫芦岛': 'HLD', '海拉尔': 'HRX', '哈拉海': 'HIT', '寒岭': 'HAT', '海林': 'HRB', '虎林': 'VLB', '霍林郭勒': 'HWD',
                      '黄陵南': 'VLY', '海伦': 'HLB', '侯马': 'HMV', '黄梅东': 'HDU', '鲘门': 'KMQ', '海门': 'HMU', '哈密': 'HMR',
                      '侯马西': 'HPV', '淮南': 'HAH', '桦南': 'HNB', '淮南东': 'HOH', '淮南南': 'HNU', '海宁西': 'EUH', '鹤庆': 'HQM',
                      '怀柔北': 'HBP', '怀仁东': 'HFV', '怀柔南': 'IMP', '怀柔': 'HRP', '华山北': 'HDY', '衡水北': 'IHP', '黄山北': 'NYH',
                      '黄石东': 'OSN', '和什托洛盖': 'VSR', '华山': 'HGY', '和硕': 'VUR', '黑水': 'HOT', '衡水': 'HSP', '黄石': 'HSN',
                      '黄山': 'HKH', '花山南': 'KNN', '黑山寺': 'HVP', '虎石台': 'HUT', '海石湾': 'HSO', '花山镇': 'HZA', '黄土店': 'HKP',
                      '花土沟': 'HTO', '和田': 'VTR', '会同': 'VTQ', '海湾': 'RWH', '花溪大学城': 'HDE', '环县': 'KXJ', '花溪南': 'HNE',
                      '花溪西': 'HUE', '衡阳': 'HYQ', '河源东': 'HEA', '衡阳东': 'HVQ', '华蓥': 'HUW', '鄠邑': 'KXY', '汉源': 'WHW',
                      '河源': 'VIQ', '湟源': 'HNO', '惠州北': 'HUA', '菏泽东': 'KDK', '菏泽': 'HIK', '贺州': 'HXZ', '华州': 'HXY',
                      '湖州': 'VZH', '汉中': 'HOY', '惠州': 'HCQ', '惠州南': 'KNQ', '吉安': 'VAG', '集安': 'JAL', '建安': 'JUL',
                      '吉安西': 'JIG', '江边村': 'JBG', '晋城东': 'JGF', '金昌': 'JCJ', '晋城': 'JCF', '金城江': 'JJZ', '景德镇北': 'JDG',
                      '建德': 'JDU', '鸡东': 'JOB', '景德镇': 'JCG', '嘉峰': 'JFF', '加格达奇': 'JGX', '井冈山': 'JGG', '近海': 'JHD',
                      '静海': 'JHP', '蛟河': 'JHL', '精河南': 'JIR', '金华南': 'RNH', '金华': 'JBH', '蛟河西': 'JOL', '金华镇': 'JZE',
                      '晋江': 'JJS', '九江': 'JJG', '军粮城北': 'JMP', '贾鲁河': 'JLF', '吉林': 'JLL', '即墨北': 'JVK', '江门': 'JOQ',
                      '荆门': 'JMN', '剑门关': 'JME', '佳木斯': 'JMB', '佳  木  斯': 'BCI', '井南': 'JNP', '建宁县北': 'JCS',
                      '济宁': 'JIK', '江宁': 'JJH', '集宁南': 'JAC', '江宁西': 'OKH', '经棚': 'JPC', '建平': 'JAD', '酒泉南': 'JNJ',
                      '酒泉': 'JQJ', '金山北': 'EGH', '吉首东': 'JDA', '吉首': 'JIQ', '江山': 'JUH', '尖山': 'JPQ', '建三江': 'JIB',
                      '界首南': 'JKU', '九台': 'JTL', '九台南': 'JNL', '镜铁山': 'JVJ', '绩溪北': 'NRH', '介休东': 'JDV', '介休': 'JXV',
                      '靖西': 'JMZ', '嘉兴': 'JXH', '鸡西': 'JXB', '井陉': 'JJP', '进贤': 'JUG', '嘉兴南': 'EPH', '进贤南': 'JXG',
                      '绩溪县': 'JRH', '鸡西西': 'JAB', '金阳': 'JYE', '巨野': 'JYK', '嘉峪关': 'JGJ', '嘉峪关南': 'JBJ', '金阳南': 'JNE',
                      '简阳南': 'JOW', '江油': 'JFW', '金银潭': 'JTN', '靖宇': 'JYL', '锦州北': 'JFT', '蓟州北': 'JKP', '荆州': 'JBN',
                      '金寨': 'JZH', '锦州': 'JZD', '金州': 'JZT', '晋州': 'JXP', '蓟州': 'JIP', '锦州南': 'JOD', '焦作': 'JOF',
                      '焦作西': 'JIF', '开安': 'KAT', '库车': 'KCR', '库都尔': 'KDX', '库尔勒': 'KLR', '开封北': 'KBF', '开封': 'KFF',
                      '开福寺': 'FLQ', '开化': 'KHU', '康金井': 'KJB', '岢岚': 'KLV', '凯里': 'KLW', '凯里南': 'QKW', '库伦': 'KLD',
                      '开鲁': 'KLC', '克拉玛依': 'KHR', '喀什': 'KSR', '昆山': 'KSH', '克山': 'KSB', '昆山南': 'KNH', '奎屯': 'KTR',
                      '开阳': 'KVW', '昆阳': 'KAM', '开原': 'KYT', '开原西': 'KXT', '康庄': 'KZP', '喀左': 'KZT', '隆安东': 'IDZ',
                      '六安': 'UAH', '灵宝': 'LBF', '来宾北': 'UCZ', '灵宝西': 'LPF', '绿博园': 'LCF', '临沧': 'LXM', '隆昌北': 'NWW',
                      '乐昌东': 'ILQ', '芦潮港': 'UCH', '陆川': 'LKZ', '龙川': 'LUQ', '利川': 'LCN', '临川': 'LCG', '隆昌': 'LCW',
                      '潞城': 'UTP', '聊城': 'UCK', '陵城': 'LGK', '龙川西': 'LCA', '老城镇': 'ACQ', '两当': 'LDY', '鹿道': 'LDL',
                      '龙洞堡': 'FVW', '娄底': 'LDQ', '娄底南': 'UOQ', '离堆公园': 'INW', '廊坊': 'LJP', '娄烦': 'USV', '廊坊北': 'LFP',
                      '陆丰': 'LLQ', '临汾': 'LFV', '临汾西': 'LXV', '拉古': 'LGB', '芦官': 'LAE', '麓谷': 'BNQ', '良各庄': 'LGP',
                      '临河': 'LHC', '柳河': 'LNL', '漯河': 'LON', '六合': 'KLH', '珞璜南': 'LNE', '隆回': 'LHA', '隆化': 'UHP',
                      '绿化': 'LWJ', '漯河西': 'LBN', '刘家店': 'UDT', '龙井': 'LJL', '临江': 'LQL', '丽江': 'LHM', '龙嘉': 'UJL',
                      '庐江': 'UJH', '连江': 'LKS', '庐江西': 'LUU', '兰考': 'LKF', '兰考南': 'LUF', '林口': 'LKB', '龙口市': 'UKK',
                      '吕梁': 'LHV', '醴陵': 'LLG', '兰棱': 'LLB', '拉林': 'LAB', '柳林南': 'LKV', '陇南': 'INJ', '辽宁朝阳': 'VET',
                      '梁平': 'UQW', '滦平': 'UPP', '罗平': 'LPM', '梁平南': 'LPE', '临平南': 'EVH', '六盘水': 'UMW', '灵丘': 'LVV',
                      '龙桥': 'LQU', '龙山北': 'LBA', '灵石东': 'UDV', '乐山': 'IVW', '陵水': 'LIQ', '丽水': 'USH', '旅顺': 'LST',
                      '庐山': 'LSG', '溧水': 'LDH', '岚山西': 'UWK', '黎塘': 'LTZ', '芦台': 'LTP', '临潼': 'LIY', '乐同': 'LEA',
                      '灵武北': 'UWJ', '莱芜东': 'LWK', '洛湾三江': 'KRW', '泸县': 'LXE', '澧县': 'LEQ', '陇西': 'LXJ', '陇县': 'LXY',
                      '临西': 'UEP', '莱西': 'LBK', '兰溪': 'LWH', '良乡': 'LAP', '略阳': 'LYY', '辽阳': 'LYT', '耒阳': 'LYQ',
                      '溧阳': 'LEH', '龙岩': 'LYS', '龙  岩': 'GBI', '洛阳': 'LYF', '临沂北': 'UMK', '临  沂北': 'III', '连云港东': 'UKH',
                      '洛阳东': 'LDF', '连云港': 'UIH', '临沂': 'LVK', '洛阳龙门': 'LLF', '柳园南': 'LNR', '凌源': 'LYD', '辽源': 'LYL',
                      '柳园': 'DHR', '涟源': 'LAQ', '涞源': 'LYP', '罗源': 'LVS', '耒阳西': 'LPQ', '泸州': 'LUE', '林芝': 'LZO',
                      '柳州': 'LZZ', '六枝': 'LIW', '阆中': 'LZE', '龙镇': 'LZA', '立志': 'LZX', '辽中': 'LZD', '马鞍山东': 'OMH',
                      '麻城北': 'MBN', '麻城': 'MCN', '渑池南': 'MNF', '免渡河': 'MDX', '磨丁': 'VBM', '牡丹江': 'MDB',
                      '牡  丹  江': 'BBI', '莫尔道嘎': 'MRX', '帽儿山': 'MRB', '帽儿山西': 'MUB', '明光': 'MGH', '满归': 'MHX',
                      '孟关': 'MGE', '磨憨': 'MHM', '漠河': 'MVX', '梅河口': 'MHL', '民和南': 'MNO', '孟家岗': 'MGB', '米兰': 'MIR',
                      '勐腊': 'MWM', '美兰': 'MHQ', '弥勒': 'MLM', '穆棱': 'MLB', '茂名': 'MDQ', '茂名西': 'MMZ', '冕宁': 'UGW',
                      '玛纳斯': 'MSR', '闽清北': 'MBS', '民权': 'MQF', '眉山东': 'IUW', '名山': 'MSE', '密山': 'MSB', '庙山': 'MSN',
                      '马三家': 'MJT', '米沙子': 'MST', '麻尾': 'VAW', '岷县': 'MXJ', '勉县': 'MVY', '绵阳': 'MYW', '密云北': 'MUP',
                      '孟塬': 'HSY', '墨玉': 'MUR', '门源': 'MYO', '暮云': 'KIQ', '密云': 'MYP', '梅州': 'MOQ', '孟庄': 'MZF',
                      '蒙自': 'MZM', '满洲里': 'MLX', '梅州西': 'MXA', '宁安': 'NAB', '农安': 'NAT', '宁波东': 'NVH', '宁波': 'NGH',
                      '南部': 'NBE', '南曹': 'NEF', '南充北': 'NCE', '南充': 'NCW', '南城': 'NDG', '南岔': 'NCB', '南丹': 'NDZ',
                      '宁德': 'NES', '南大庙': 'NMP', '宁东南': 'NDJ', '宁东': 'NOJ', '南芬': 'NFT', '南丰': 'NFG', '宁海': 'NHH',
                      '南湖东': 'NDN', '讷河': 'NHX', '牛河梁': 'LKT', '内江北': 'NKW', '内江': 'NJW', '嫩江': 'NGX', '南江': 'FIW',
                      '牛家': 'NJB', '南口': 'NKP', '牛栏山': 'NLP', '宁陵县': 'NLF', '奈曼': 'NMD', '尼木': 'NMO', '南平市': 'NOS',
                      '宁强南': 'NOY', '那曲': 'NQO', '南通': 'NUH', '南通西': 'NXU', '宁武': 'NWV', '南翔北': 'NEH', '南雄': 'NCQ',
                      '宁乡': 'NXQ', '南阳': 'NFF', '南阳东': 'NOF', '纳雍': 'NYE', '南峪': 'NUP', '南阳寨': 'NYF', '碾子山': 'NZX',
                      '普安': 'PAN', '蒲城东': 'PEY', '平昌': 'PCE', '平顶山': 'PEN', '平度': 'PNK', '平度西': 'PAK', '平顶山西': 'PDF',
                      '普洱': 'PEM', '平房': 'PFB', '盘锦北': 'PBD', '盘锦': 'PVD', '蒲江': 'PJE', '盘龙城': 'PNN', '普兰店': 'PLT',
                      '平凉': 'PIJ', '平凉南': 'POJ', '蓬莱市': 'POK', '普宁': 'PEQ', '平泉北': 'PBP', '平泉': 'PQP', '皮山': 'PSR',
                      '磐石': 'PSL', '坪石': 'PSQ', '平山': 'PSB', '平潭': 'PIS', '莆田': 'PTS', '萍乡北': 'PBG', '凭祥': 'PXZ',
                      '萍乡': 'PXG', '普雄': 'POW', '郫县': 'PWW', '郫县西': 'PCW', '濮阳': 'PYF', '平阳': 'ARH', '平遥古城': 'PDV',
                      '濮阳东': 'PUF', '平原东': 'PUK', '彭泽': 'PZG', '普者黑': 'PZM', '盘州': 'PAE', '攀枝花': 'PRW', '彭州': 'PMW',
                      '攀枝花南': 'PNE', '彭州南': 'PKW', '庆安': 'QAB', '青白江东': 'QFW', '清城': 'QCA', '蕲春': 'QRN', '青川': 'QCE',
                      '青城山': 'QSW', '青岛': 'QDK', '青岛北': 'QHK', '青  岛北': 'KAI', '千岛湖': 'QDU', '启东': 'QOU', '青岛西': 'QUK',
                      '曲阜东': 'QAK', '前锋': 'QFB', '曲阜': 'QFK', '琼海': 'QYQ', '清河城': 'QYP', '秦皇岛': 'QTP', '清河': 'QIP',
                      '清华园': 'QHP', '曲靖北': 'QBM', '綦江东': 'QDE', '黔江': 'QNW', '曲靖': 'QJM', '前进镇': 'QEB', '邛崃': 'QLE',
                      '清流': 'QLS', '齐齐哈尔': 'QHX', '齐齐哈尔南': 'QNB', '潜山': 'QSU', '庆盛': 'QSQ', '曲水县': 'QSO', '七台河': 'QTB',
                      '青铜峡': 'QTJ', '七台河西': 'QXB', '渠县': 'QRW', '沁县': 'QVV', '清徐': 'QUV', '庆阳': 'QOJ', '清远': 'QBQ',
                      '庆元': 'QYU', '钦州东': 'QDZ', '泉州东': 'QRS', '乔庄东': 'QEP', '衢州': 'QEH', '泉州': 'QYS', '全州南': 'QNZ',
                      '清镇西': 'QUE', '融安': 'RAZ', '瑞安': 'RAH', '荣昌北': 'RQW', '荣成': 'RCK', '如东': 'RIH', '汝箕沟': 'RQJ',
                      '瑞金': 'RJG', '日喀则': 'RKO', '饶平': 'RVQ', '若羌': 'RQR', '日照': 'RZK', '日照西': 'KZK', '肃北': 'SBJ',
                      '双城北': 'SBB', '舒城东': 'SDU', '莎车': 'SCR', '沙城': 'SCP', '宋城路': 'SFF', '双城堡': 'SCB', '邵东': 'FIQ',
                      '十渡': 'SEP', '双峰北': 'NFQ', '双丰': 'OFB', '绥芬河': 'SFB', '韶关东': 'SGQ', '韶关': 'SNQ', '沙河': 'SHP',
                      '商河': 'SOK', '山海关': 'SHD', '沙河市': 'VOP', '山河屯': 'SHL', '绥化': 'SHB', '石河子': 'SZR', '三家店': 'ODP',
                      '三间房': 'SFX', '松江河': 'SJL', '水家湖': 'SQH', '松江': 'SAH', '孙家': 'SUB', '沈家': 'OJB', '三江南': 'SWZ',
                      '石景山南': 'SRP', '松江南': 'IMH', '苏家屯': 'SXT', '三江县': 'SOZ', '深井子': 'SWT', '四棵树': 'SIR', '舒兰': 'SLL',
                      '双流机场': 'IPW', '双龙湖': 'OHB', '绥棱': 'SIB', '狮岭': 'SLA', '石林': 'SLM', '双龙南': 'SNE', '商洛': 'OLY',
                      '双流西': 'IQW', '石林西': 'SYM', '胜利镇': 'OLB', '石门县北': 'VFQ', '三明北': 'SHS', '三明': 'SVS', '嵩明': 'SVM',
                      '树木岭': 'FMQ', '神木南': 'OMY', '三门峡南': 'SCF', '神木': 'HMY', '三门县': 'OQH', '三门峡西': 'SXF', '三门峡': 'SMF',
                      '商南': 'ONY', '遂宁': 'NIW', '睢宁': 'SNU', '宋': 'SOB', '石牌': 'SPQ', '沙坪坝': 'CYW', '四平东': 'PPT',
                      '山坡东': 'SBN', '四平': 'SPT', '沈丘北': 'SKF', '宿迁': 'SQU', '商丘': 'SQF', '石泉县': 'SXY', '石桥子': 'SQT',
                      '上饶': 'SRG', '石人城': 'SRB', '鄯善北': 'SMR', '宿松东': 'SSU', '蜀山东': 'HTH', '韶山': 'SSQ', '神树': 'SWB',
                      '韶山南': 'INQ', '宿松': 'OAH', '三穗': 'QHW', '松桃': 'MZQ', '汕头': 'OTQ', '汕尾': 'OGQ', '邵武': 'SWS',
                      '绍兴北': 'SLH', '绍兴东': 'SSH', '松溪': 'SIS', '涉县': 'OEP', '绍兴': 'SOH', '三亚': 'SEQ', '邵阳': 'SYQ',
                      '十堰': 'SNN', '双阳': 'OYT', '十堰东': 'OUN', '顺义': 'SOP', '三元区': 'SMS', '双鸭山': 'SSB', '松原': 'VYT',
                      '双鸭山西': 'OXB', '顺义西': 'IKP', '深圳北': 'IOQ', '苏州北': 'OHH', '深圳机场': 'SCA', '嵊州新昌': 'SKU',
                      '深圳东': 'BJQ', '宿州东': 'SRH', '绥中': 'SZD', '朔州': 'SUV', '深圳': 'SZQ', '随州': 'SZN', '宿州': 'OXH',
                      '苏州': 'SZH', '尚志': 'SZB', '随州南': 'ONN', '尚志南': 'OZB', '深圳坪山': 'IFQ', '石嘴山': 'QQJ', '石柱县': 'OSW',
                      '深圳西': 'OSQ', '泰安': 'TMK', '通北': 'TBB', '铜川东': 'TCY', '塔城': 'TZR', '汤池': 'TCX', '通道': 'TRQ',
                      '土地堂东': 'TTN', '塔尔气': 'TVX', '潼关': 'TGY', '太谷': 'TGV', '塘沽': 'TGP', '吐哈': 'THR', '通海': 'TAM',
                      '塔哈': 'THX', '天河机场': 'TJN', '泰和': 'THG', '塔河': 'TXX', '天河街': 'TEN', '太湖南': 'TAU', '天河潭': 'TTE',
                      '通化': 'THL', '太湖': 'TKH', '同江': 'TJB', '陶家屯': 'TOT', '托克托东': 'TVC', '泰来': 'TLX', '吐鲁番北': 'TAR',
                      '吐鲁番': 'TFR', '通辽': 'TLD', '铜陵': 'TJH', '铁岭': 'TLT', '铁力': 'TLB', '桐庐': 'TLU', '铁岭西': 'PXT',
                      '陶赖昭': 'TPT', '图们北': 'QSL', '图们': 'TML', '头门港': 'TMU', '图木舒克': 'TMR', '天门南': 'TNN', '潼南': 'TVW',
                      '泰宁': 'TNS', '铜仁': 'RDQ', '铜仁南': 'TNW', '唐山北': 'FUP', '田师府': 'TFT', '泰山': 'TAK', '唐山': 'TSP',
                      '天水': 'TSJ', '天水南': 'TIJ', '汤旺河': 'THB', '汤逊湖': 'THN', '土溪': 'TSW', '通远堡': 'TYT', '太阳升': 'TQT',
                      '通榆': 'KTT', '桐梓北': 'TBE', '太子城': 'IZP', '滕州东': 'TEK', '桐梓东': 'TDE', '台州': 'TEU', '泰州': 'UTH',
                      '通州': 'TOP', '台州西': 'TZH', '通州西': 'TAP', '文昌': 'WEQ', '武昌': 'WCN', '五常': 'WCB', '武当山': 'WRN',
                      '潍坊': 'WFK', '瓦房店': 'WDT', '万发屯': 'WFB', '瓦房店西': 'WXT', '王岗': 'WGB', '武功': 'WGY', '威海': 'WKK',
                      '乌海': 'WVC', '苇河': 'WHB', '芜湖': 'WHH', '乌海西': 'WXC', '苇河西': 'WIB', '温江': 'WJE', '五家': 'WUB',
                      '吴家屯': 'WJT', '五棵树': 'WKT', '乌兰察布': 'WPC', '万乐': 'WEB', '温岭': 'VHH', '乌龙泉南': 'WFN', '武隆': 'WLW',
                      '乌拉特前旗': 'WQC', '乌兰浩特': 'WWT', '渭南': 'WNY', '渭南北': 'WBY', '五女山': 'WET', '渭南西': 'WXY', '沃皮': 'WPT',
                      '汪清': 'WQL', '武清': 'WWP', '武胜': 'WSE', '威舍': 'WSM', '乌审旗': 'WGC', '乌苏': 'WSR', '歪头山': 'WIT',
                      '武威': 'WUJ', '武威南': 'WWJ', '无为南': 'WWU', '武穴北': 'WJN', '无锡东': 'WGH', '无锡': 'WXH', '乌西': 'WXR',
                      '武穴': 'WXN', '吴圩': 'WYZ', '闻喜西': 'WOV', '武夷山北': 'WBS', '五营': 'WWB', '乌伊岭': 'WPB', '武夷山': 'WAS',
                      '渭源': 'WEJ', '婺源': 'WYG', '万源': 'WYY', '万州北': 'WZE', '梧州': 'WZZ', '万州': 'WYW', '吴忠': 'WVJ',
                      '温州': 'RZH', '梧州南': 'WBZ', '温州南': 'VRH', '兴安北': 'XDZ', '雄安': 'IQP', '西安西': 'EGY', '许昌东': 'XVF',
                      '兴城': 'XCD', '宣城': 'ECH', '西昌': 'ECW', '许昌': 'XCF', '西昌西': 'XCE', '新城子': 'XCT', '新都东': 'EWW',
                      '香坊': 'XFB', '咸丰': 'XFA', '西丰': 'XFT', '息烽': 'XFW', '先锋': 'NQQ', '湘府路': 'FVQ', '轩岗': 'XGV',
                      '孝感北': 'XJN', '孝感东': 'GDN', '香港西九龙': 'XJA', '兴国': 'EUG', '西固': 'XIJ', '夏官营': 'XGJ', '宣汉': 'XHY',
                      '兴和北': 'EBC', '下花园北': 'OKP', '新化南': 'EJQ', '新会': 'EFQ', '新晃': 'XLQ', '兴和西': 'XEC', '新晃西': 'EWQ',
                      '新津': 'IRW', '辛集': 'ENP', '徐家': 'XJB', '小金口': 'NKQ', '新津南': 'ITW', '辛集南': 'IJP', '谢家镇': 'XMT',
                      '西来': 'XLE', '兴隆店': 'XDD', '新乐': 'ELP', '仙林': 'XPH', '小岭': 'XLB', '锡林浩特': 'XTC', '兴隆县': 'EXP',
                      '新立镇': 'XGT', '兴隆镇': 'XZB', '厦门北': 'XKS', '新民北': 'XOT', '厦门': 'XMS', '厦 门': 'EMS', '新民': 'XMD',
                      '厦门高崎': 'XBS', '咸宁南': 'UNN', '犀浦东': 'XAW', '溆浦南': 'EMQ', '霞浦': 'XOS', '溆浦': 'EPQ', '犀浦': 'XIW',
                      '秀山': 'ETW', '小市': 'XST', '兴山': 'EMN', '西双版纳': 'ENM', '新松浦': 'XOB', '仙桃': 'VTN', '湘潭': 'XTQ',
                      '向塘': 'XTG', '邢台东': 'EDP', '新塘南': 'NUQ', '兴文': 'XNE', '宣威': 'XWM', '修文县': 'XWE', '萧县北': 'QSH',
                      '新香坊北': 'RHB', '新乡东': 'EGF', '孝西': 'XOV', '西乡': 'XQY', '西峡': 'XIF', '新乡': 'XXF', '小新街': 'XXM',
                      '信阳': 'XUN', '旬阳': 'XUY', '咸阳': 'XYY', '岫岩': 'XXT', '襄阳': 'XFN', '新余北': 'XBG', '熊岳城': 'XYT',
                      '信阳东': 'OYN', '襄阳东': 'EKN', '兴义': 'XRZ', '信宜': 'EEQ', '秀英': 'XYA', '祥云': 'XQM', '新余': 'XUG',
                      '咸阳西': 'XOY', '新郑机场': 'EZF', '徐州东': 'UUH', '忻州': 'XXV', '新肇': 'XZT', '襄州': 'XWN', '徐州': 'XCH',
                      '香樟路': 'FNQ', '忻州西': 'IXV', '雅安': 'YAE', '延安': 'YWY', '永安南': 'YQS', '依安': 'YAX', '宜宾': 'YBW',
                      '迎宾路': 'YFW', '亚布力': 'YBB', '亚布力南': 'YWB', '叶柏寿': 'YBD', '宜宾西': 'YXE', '亚布力西': 'YSB',
                      '运城北': 'ABV', '盐城北': 'AEH', '永川东': 'WMW', '宜昌东': 'HAN', '岳池': 'AWW', '叶城': 'YER', '阳春': 'YQQ',
                      '宜春': 'YEG', '运城': 'YNV', '宜昌': 'YCN', '盐城': 'AFH', '伊春': 'YCB', '榆次': 'YCV', '杨村': 'YBP',
                      '永登': 'YDJ', '雁荡山': 'YGH', '于都': 'YDG', '姚渡': 'AOJ', '英德西': 'IIQ', '伊尔施': 'YET', '云浮东': 'IXQ',
                      '燕岗': 'YGW', '永济北': 'AJV', '延吉': 'YJL', '阳江': 'WRQ', '永济': 'YIV', '燕郊': 'AJP', '姚家': 'YAT',
                      '英吉沙': 'YIR', '延吉西': 'YXL', '营口东': 'YGT', '永康南': 'QUH', '营口': 'YKT', '牙克石': 'YKX', '依兰': 'YEB',
                      '宜良北': 'YSM', '永乐店': 'YDY', '玉林': 'YLZ', '榆林': 'ALY', '杨陵': 'YSY', '炎陵': 'YAG', '阎良': 'YNY',
                      '杨林': 'YLM', '杨陵南': 'YEY', '余粮堡': 'YLD', '杨柳青': 'YQP', '亚龙湾': 'TWQ', '羊马': 'YME', '一面坡北': 'YXB',
                      '云梦东': 'YRN', '玉门': 'YXJ', '一面坡': 'YPB', '元谋西': 'AMM', '郁南': 'YKQ', '伊宁东': 'YNR', '伊宁': 'YMR',
                      '延平东': 'ADS', '阳平关': 'YAY', '玉屏': 'YZW', '延平': 'YPS', '原平': 'YPV', '延平西': 'YWS', '原平西': 'IPV',
                      '阳泉北': 'YPP', '阳泉东': 'AYP', '雁栖湖': 'FGP', '焉耆': 'YSR', '乐清': 'UPH', '延庆': 'YNP', '阳泉曲': 'YYV',
                      '姚千户屯': 'YQT', '阳泉': 'AQP', '阳曲': 'YQV', '玉泉': 'YQB', '阳曲西': 'IQV', '榆社': 'YSV', '玉山': 'YNG',
                      '营山': 'NUW', '榆树': 'YRT', '元氏': 'YSP', '燕山': 'AOP', '玉山南': 'YGG', '榆树屯': 'YSX', '银滩': 'CTQ',
                      '烟台': 'YAK', '鹰潭': 'YTG', '永泰': 'YTS', '鹰潭北': 'YKG', '伊图里河': 'YEX', '依吞布拉克': 'YVR', '烟台南': 'YLK',
                      '烟筒山': 'YSL', '玉田县': 'ATP', '义乌': 'YWH', '玉溪': 'AXM', '云霄': 'YBS', '义县': 'YXD', '阳新': 'YON',
                      '宜兴': 'YUH', '尤溪': 'YXS', '益阳': 'AEQ', '岳阳': 'YYQ', '岳阳东': 'YIQ', '益阳南': 'YAA', '扬州东': 'YDU',
                      '崖州': 'YUQ', '永州': 'AOQ', '兖州': 'YZK', '扬州': 'YLH', '榆中': 'IZJ', '诏安': 'ZDS', '淄博北': 'ZRK',
                      '淄博': 'ZBK', '中川机场': 'ZJJ', '镇城底': 'ZDV', '正定机场': 'ZHP', '正定': 'ZDP', '准东': 'ZER', '纸坊东': 'ZMN',
                      '柘皋': 'ZGU', '自贡北': 'ZGW', '自贡': 'ZGE', '珠海': 'ZHQ', '庄河北': 'ZUT', '珠海北': 'ZIQ', '珠海长隆': 'ZLA',
                      '中华门': 'VNH', '张家川': 'ZIJ', '张家港': 'ZAU', '湛江': 'ZJZ', '织金': 'IZW', '治江': 'ZIY', '芷江': 'ZPQ',
                      '诸暨': 'ZDH', '镇江': 'ZJH', '周家': 'ZOB', '张家界': 'DIQ', '张家口': 'ZMP', '张家口南': 'IXP', '镇江南': 'ZEH',
                      '湛江西': 'ZWQ', '张家界西': 'JXA', '周口东': 'ZKF', '周口': 'ZKN', '镇赉': 'ZLT', '庄里': 'ZLY', '左岭': 'ZSN',
                      '扎兰屯': 'ZTX', '扎赉诺尔西': 'ZXX', '驻马店': 'ZDN', '中牟': 'ZGF', '驻马店西': 'ZLN', '漳平': 'ZPS', '泽普': 'ZPR',
                      '漳平西': 'ZXG', '章丘北': 'ZVK', '肇庆东': 'FCQ', '肇庆': 'ZVQ', '章丘': 'ZTK', '柞水': 'ZSY', '珠斯花': 'ZHD',
                      '中山': 'ZSQ', '樟树': 'ZSG', '朱砂古镇': 'ZSE', '周水子': 'ZIT', '中堂': 'ZTA', '昭通': 'ZDW', '中卫': 'ZWJ',
                      '中卫南': 'ZTJ', '镇雄': 'ZXE', '紫阳': 'ZVY', '枣阳': 'ZYN', '资阳北': 'FYW', '张掖': 'ZYJ', '遵义': 'ZYE',
                      '镇远': 'ZUW', '遵义西': 'ZIW', '张掖西': 'ZEJ', '资中北': 'WZW', '漳州东': 'GOS', '涿州东': 'ZAP', '枣庄': 'ZEK',
                      '漳州': 'ZUS', '株洲': 'ZZQ', '庄寨': 'VOK', '株洲南': 'KVQ', '枣庄西': 'ZFK', '株洲西': 'ZAQ', '阿巴嘎旗': 'AQC',
                      '安定': 'ADP', '安多': 'ADO', '安广': 'AGT', '敖汉': 'YED', '艾河': 'AHP', '安化': 'PKQ', '艾家村': 'AJJ',
                      '安江东': 'ADA', '阿金': 'AJD', '安匠': 'MJP', '阿克塞': 'AKJ', '安口窑': 'AYY', '敖力布告': 'ALD', '安龙': 'AUZ',
                      '阿龙山': 'ASX', '阿木尔': 'JTX', '阿南庄': 'AZM', '安仁': 'ARG', '安塘': 'ATV', '阿图什': 'ATR', '安图': 'ATL',
                      '安图西': 'AXL', '阿瓦提': 'AWR', '安溪': 'AXS', '博鳌': 'BWQ', '白壁关': 'BGV', '八步': 'BBE', '栟茶': 'FWH',
                      '板城': 'BUP', '宝坻': 'BZI', '宝坻南': 'BOI', '宝丰': 'BFF', '白沟': 'FEP', '白河东': 'BIY', '滨海港': 'BGU',
                      '宝华山': 'BWH', '白河县': 'BEY', '白芨沟': 'BJJ', '北滘': 'IBQ', '碧江': 'BLQ', '白鸡坡': 'BBM', '笔架山': 'BSB',
                      '八角台': 'BTD', '北井子': 'BRT', '保康': 'BKD', '保康县': 'BKN', '白狼': 'BAT', '博罗北': 'BLA', '博乐东': 'BOR',
                      '北流': 'BOZ', '宝林': 'BNB', '布列开': 'BLR', '宝龙山': 'BND', '百里峡': 'AAP', '八里甸子': 'BLT', '白马北': 'BME',
                      '八面城': 'BMD', '北马圈子': 'BRP', '北票南': 'RPD', '白旗': 'BQP', '白泉': 'BQL', '璧山': 'FZW', '巴山': 'BAY',
                      '白水江': 'BSY', '白沙铺': 'BSN', '白沙坡': 'BPM', '白石山': 'BAL', '白水县': 'BGY', '白水镇': 'BUM', '板塘': 'NGQ',
                      '坂田': 'BTQ', '泊头': 'BZP', '北屯': 'BYP', '巴图营': 'BWT', '白文东': 'BCV', '本溪新城': 'BVT', '本溪湖': 'BHT',
                      '博兴': 'BXK', '八仙筒': 'VXD', '白音察干': 'BYC', '宝应': 'BAU', '白音他拉': 'BID', '白音华南': 'BOD',
                      '白音胡硕': 'BCD', '白银市': 'BNJ', '霸州北': 'VPP', '巴中东': 'BDE', '彬州': 'BXY', '霸州': 'RMP', '北宅': 'BVP',
                      '霸州西': 'FOP', '长安': 'CAA', '长安西': 'CXA', '赤壁北': 'CIN', '澄城': 'CUY', '长城': 'CEJ', '承德县北': 'IYP',
                      '承德东': 'CCP', '城固北': 'CBY', '长葛': 'CEF', '查干湖': 'VAT', '册亨': 'CHZ', '草河口': 'CKT', '崔黄口': 'CHP',
                      '蔡家沟': 'CJT', '成吉思汗': 'CJX', '岔江': 'CAM', '陈江南': 'KKQ', '蔡家坡': 'CJY', '策勒': 'CLR', '昌乐': 'CLK',
                      '超梁沟': 'CYP', '茶陵南': 'CNG', '长岭子': 'CLT', '长宁': 'CNE', '长农': 'CNJ', '常平': 'DAQ', '长坡岭': 'CPM',
                      '常平南': 'FPQ', '长箐': 'CQE', '辰清': 'CQB', '长寿': 'EFW', '长寿湖': 'CSE', '蔡山': 'CON', '苍石': 'CST',
                      '草市': 'CSL', '磁山': 'CSP', '常山': 'CSU', '常熟': 'CAU', '楚山': 'CSB', '长山屯': 'CVT', '长汀': 'CES',
                      '春湾': 'CQQ', '岑溪': 'CNZ', '长兴': 'CBH', '磁西': 'CRP', '磁窑': 'CYK', '长阳': 'CYN', '城阳': 'CEK',
                      '创业村': 'CEX', '朝阳地': 'CDD', '昌邑': 'CRK', '朝阳南': 'CYD', '长垣': 'CYF', '朝阳镇': 'CZL', '陈庄': 'CZY',
                      '潮州': 'CKQ', '曹子里': 'CFP', '长治南': 'CAF', '城子坦': 'CWT', '车转湾': 'CWM', '大安': 'RAT', '德安': 'DAG',
                      '大坝': 'DBJ', '德保': 'RBZ', '到保': 'RBT', '大巴': 'DBD', '电白': 'NWQ', '大板': 'DBC', '东边井': 'DBB',
                      '德伯斯': 'RDT', '打柴沟': 'DGJ', '德昌': 'DVW', '大厂': 'DCI', '都昌': 'DCG', '东城南': 'IYQ', '德昌西': 'DXE',
                      '滴道': 'DDB', '大磴沟': 'DKJ', '东戴河': 'RDD', '丹东西': 'RWT', '刀尔登': 'DRD', '得耳布尔': 'DRX', '东二道河': 'DRB',
                      '杜尔伯特': 'TKX', '大方': 'DFE', '东丰': 'DIL', '都格': 'DMM', '东莞港': 'DGA', '大港南': 'DNU', '大官屯': 'DTT',
                      '东光': 'DGP', '东海': 'DHB', '东花园北': 'QBP', '大灰厂': 'DHP', '鼎湖东': 'UWQ', '鼎湖山': 'NVQ', '大禾塘': 'SOQ',
                      '东海县': 'DQH', '东津': 'DKB', '丹江口': 'DON', '董家口': 'DTK', '大口屯': 'DKP', '东来': 'RVD', '大林': 'DLD',
                      '带岭': 'DLB', '达拉特旗': 'DIC', '独立屯': 'DTX', '豆罗': 'DLV', '达拉特西': 'DNC', '大连西': 'GZT', '大朗镇': 'KOQ',
                      '东明村': 'DMD', '洞庙河': 'DEP', '大平房': 'DPD', '大盘石': 'RPP', '大堡': 'DVT', '大青沟': 'DSD', '大其拉哈': 'DQX',
                      '道清': 'DML', '德清': 'DRH', '杜桥': 'DQU', '德清西': 'MOH', '东胜东': 'RSC', '东升': 'DRQ', '登沙河': 'DWT',
                      '砀山': 'DKH', '大石头南': 'DAL', '大石头': 'DSL', '大石寨': 'RZT', '灯塔': 'DGT', '定陶': 'DQK', '东台': 'DBH',
                      '大田边': 'DBM', '当涂东': 'OWH', '东通化': 'DTL', '丹徒': 'RUH', '东湾': 'DRJ', '大旺': 'WWQ', '低窝铺': 'DWJ',
                      '德兴东': 'DDG', '大兴沟': 'DXL', '德兴': 'DWG', '定襄': 'DXV', '代县': 'DKV', '甸心': 'DXM', '丹霞山': 'IRQ',
                      '东戌': 'RXP', '东辛庄': 'DXD', '大雁': 'DYX', '大阳': 'RET', '丹阳北': 'EXH', '东淤地': 'DBV', '大营': 'DYV',
                      '定远': 'EWH', '岱岳': 'RYV', '大余': 'DYG', '大营子': 'DZD', '大营镇': 'DJP', '大战场': 'DTJ', '兑镇': 'DWV',
                      '道州': 'DFZ', '东镇': 'DNV', '东庄': 'DZV', '端州': 'WZQ', '低庄': 'DVQ', '豆庄': 'ROP', '大足南': 'FQW',
                      '大竹园': 'DZY', '大杖子': 'DAP', '豆张庄': 'RZP', '峨边南': 'ENE', '二道沟门': 'RDP', '二道湾': 'RDX', '二龙': 'RLD',
                      '二龙山屯': 'ELA', '二密河': 'RML', '额敏': 'EMR', '恩平': 'PXQ', '峨山': 'EVM', '二营': 'RYJ', '鄂州东': 'EFN',
                      '福安': 'FAS', '丰城东': 'FIG', '凤城东': 'FDT', '富川': 'FDZ', '丰城': 'FCG', '方城': 'FNF', '丰城南': 'FNG',
                      '繁昌西': 'PUH', '扶沟南': 'FGF', '富海': 'FHX', '凤凰古城': 'FCA', '福海西': 'FHA', '奉节': 'FJE', '枫林': 'FLN',
                      '福利屯': 'FTB', '丰乐镇': 'FZB', '阜南': 'FNH', '抚宁': 'FNP', '阜宁': 'AKH', '阜宁南': 'FNU', '富平': 'FPY',
                      '佛坪': 'FUY', '法启': 'FQE', '芙蓉镇': 'FRA', '丰顺东': 'FDA', '复盛': 'FAW', '丰顺': 'FUQ', '繁峙': 'FSV',
                      '抚顺': 'FST', '福山口': 'FKP', '扶绥南': 'FNZ', '抚松': 'FSL', '福山镇': 'FZQ', '凤台南': 'FTU', '冯屯': 'FTX',
                      '浮图峪': 'FYP', '费县北': 'FBK', '富县东': 'FDY', '富县': 'FEY', '费县': 'FXK', '汾阳': 'FAV', '凤阳': 'FUH',
                      '富源北': 'FBM', '扶余': 'FYT', '抚州北': 'FBG', '抚州东': 'FDG', '范镇': 'VZK', '固安东': 'GQP', '固安': 'GFP',
                      '高碑店东': 'GMP', '高碑店': 'GBP', '沟帮子': 'GBD', '谷城北': 'GBN', '古城东': 'GUU', '恭城': 'GCZ', '谷城': 'GCN',
                      '古城镇': 'GZB', '贵定北': 'FMW', '广德': 'GRH', '贵定': 'GTW', '广德南': 'GNU', '葛店南': 'GNN', '贵定县': 'KIW',
                      '岗嘎': 'GAO', '贡嘎': 'GGO', '官高': 'GVP', '葛根庙': 'GGT', '干沟': 'GGL', '高各庄': 'GGP', '广汉北': 'GVW',
                      '甘河': 'GAX', '郭家店': 'GDT', '个旧': 'JJM', '古浪': 'GLJ', '橄榄坝': 'GVM', '归流河': 'GHT', '关岭': 'GLE',
                      '关林': 'GLF', '甘洛南': 'GNE', '桂林西': 'GEZ', '郭磊庄': 'GLP', '高密北': 'GVK', '光明城': 'IMQ', '高密': 'GMK',
                      '灌南': 'GIU', '工农湖': 'GRT', '广宁': 'FBQ', '广宁寺南': 'GNT', '广宁寺': 'GQT', '高平东': 'GVF', '高坪': 'GGN',
                      '广平': 'GPP', '高平': 'GPF', '弓棚子': 'GPT', '甘泉北': 'GEY', '甘旗卡': 'GQD', '甘泉': 'GQY', '高桥镇': 'GZD',
                      '赶水东': 'GDE', '光山': 'GUN', '灌水': 'GST', '孤山口': 'GSP', '果松': 'GSL', '嘎什甸子': 'GXD', '高山子': 'GSD',
                      '高滩': 'GAY', '高台': 'GTJ', '古田北': 'GBS', '古田': 'GTS', '官厅': 'GTP', '高台南': 'GAJ', '官厅西': 'KEP',
                      '赣县北': 'GIG', '贵溪': 'GXG', '涡阳': 'GYH', '高邮北': 'GEU', '观音机场': 'GCU', '高邮': 'GAU', '菇园': 'GYL',
                      '灌云': 'GOU', '公营子': 'GYD', '光泽': 'GZS', '古镇': 'GNQ', '虢镇': 'GZY', '盖州': 'GXT', '瓜州': 'GZJ',
                      '固镇': 'GEH', '官字井': 'GOT', '冠豸山南': 'GSS', '古丈西': 'GXA', '红安': 'HWN', '海安': 'HIH', '淮安南': 'AMH',
                      '怀安': 'QAP', '惠安': 'HNS', '惠安堡': 'KBJ', '黄柏': 'HBL', '淮北北': 'PLH', '鹤壁东': 'HFF', '海北': 'HEB',
                      '鹤壁': 'HAF', '会昌北': 'XEG', '寒葱沟': 'HKB', '河唇': 'HCZ', '华城': 'VCQ', '霍城': 'SER', '汉川': 'HCN',
                      '黑冲滩': 'HCJ', '横道河子东': 'KUX', '化德': 'HGC', '河东里': 'KLJ', '海东': 'LVO', '洪洞': 'HDV', '海东西': 'HDO',
                      '横峰': 'HFG', '韩府湾': 'HXJ', '黄冈': 'KGN', '横沟桥东': 'HNN', '黄冈西': 'KXN', '洪河': 'HPB', '红花沟': 'VHD',
                      '黄花筒': 'HUD', '惠环': 'KHQ', '花湖': 'KHN', '贺家店': 'HJJ', '厚街': 'HJA', '黑井': 'HIM', '涵江': 'HJS',
                      '获嘉': 'HJF', '杭锦后旗': 'HDC', '河间西': 'HXP', '花家庄': 'HJM', '黄口': 'KOH', '湖口': 'HKG', '怀来': 'VQP',
                      '海林北': 'KBX', '浩良河': 'HHB', '黄流': 'KLQ', '黄陵': 'ULY', '鹤立': 'HOB', '桦林': 'HIB', '和龙': 'HLL',
                      '海龙': 'HIL', '哈拉苏': 'HAX', '呼鲁斯太': 'VTJ', '火连寨': 'HLT', '虎门北': 'HBA', '虎门东': 'HDA', '黄梅': 'VEH',
                      '虎门': 'IUQ', '洪梅': 'HMA', '韩麻营': 'HYP', '衡南': 'HNG', '桦南东': 'KNB', '黄泥河': 'HHL', '化念': 'HDM',
                      '海宁': 'HNH', '怀宁': 'APH', '惠农': 'HMJ', '和平北': 'HPA', '和平': 'VAQ', '合浦': 'HVZ', '花棚子': 'HZM',
                      '横琴北': 'HOA', '霍邱': 'FBH', '宏庆': 'HEY', '横琴': 'HQA', '花桥': 'VQH', '红旗渠': 'HQF', '华容东': 'HPN',
                      '怀仁': 'HRV', '华容南': 'KRN', '华容': 'HRN', '红寺堡北': 'HEJ', '黑山北': 'HQT', '黄石北': 'KSN', '贺胜桥东': 'HLN',
                      '黄松甸': 'HDL', '汉寿': 'HHA', '衡山': 'HSQ', '虎什哈': 'HHP', '惠山': 'VCH', '红山': 'VSB', '汉寿南': 'VSQ',
                      '含山南': 'HSU', '红寺堡': 'HSJ', '红砂岘': 'VSJ', '衡山西': 'HEQ', '桓台': 'VTK', '荷塘': 'KXQ', '黑台': 'HQB',
                      '黄桶北': 'HBE', '海坨子': 'HZT', '黑旺': 'HWK', '徽县': 'HYY', '红星': 'VXB', '红兴隆': 'VHB', '红岘台': 'HTJ',
                      '换新天': 'VTB', '滑浚': 'HWF', '合阳': 'HAY', '海晏': 'HFO', '红彦': 'VIX', '合阳北': 'HTY', '河源北': 'HYA',
                      '海阳北': 'HEK', '汉阴': 'HQY', '槐荫': 'IYN', '花园口': 'HYT', '淮阳南': 'HVF', '黄羊滩': 'HGJ', '花园': 'HUN',
                      '黄羊镇': 'HYJ', '霍州东': 'HWV', '黄州': 'VON', '壶镇': 'HUU', '化州': 'HZZ', '霍州': 'HZV', '惠州西': 'VXQ',
                      '巨宝': 'JRT', '靖边': 'JIY', '金宝屯': 'JBD', '晋城北': 'JEF', '交城': 'JNV', '建昌': 'JFD', '加查': 'JIO',
                      '泾川': 'JAJ', '碱厂': 'JUT', '鄄城': 'JCK', '旌德': 'NSH', '峻德': 'JDB', '井店': 'JFP', '江都': 'UDH',
                      '尖峰': 'PFQ', '鸡冠山': 'JST', '金沟屯': 'VGP', '精河': 'JHR', '金河': 'JHX', '锦河': 'JHB', '江华': 'JHZ',
                      '建湖': 'AJH', '纪家沟': 'VJD', '锦界': 'JEY', '姜家': 'JJB', '金坑': 'JKT', '金口河南': 'JHE', '将乐': 'JLS',
                      '芨岭': 'JLJ', '九郎山': 'KJQ', '江门东': 'JWQ', '角美': 'JES', '佳木斯西': 'JUB', '莒南': 'JOK', '莒南北': 'VNK',
                      '济宁北': 'MIK', '济宁东': 'MNK', '建宁南': 'JQS', '建瓯东': 'JZS', '建瓯': 'JVS', '建瓯西': 'JUS', '金普': 'PWT',
                      '建桥': 'JQA', '江桥': 'JQX', '句容西': 'JWH', '九三': 'SSX', '金山': 'JSR', '建始': 'JRN', '建水': 'JSM',
                      '稷山': 'JVV', '吉舒': 'JSL', '建设': 'JET', '甲山': 'JOP', '京山': 'JCN', '嘉善': 'JSH', '嘉善南': 'EAH',
                      '界首市': 'JUN', '江所田': 'JOM', '金山屯': 'JTB', '吉水西': 'JSG', '景泰': 'JTJ', '金塔': 'JIJ', '吉文': 'JWX',
                      '嘉祥北': 'MXK', '泾县': 'LOH', '莒县': 'JKK', '嘉祥': 'JUK', '郏县': 'JXF', '夹心子': 'JXT', '揭阳': 'JYA',
                      '建阳': 'JYS', '姜堰': 'UEH', '江油北': 'JBE', '巨野北': 'MYK', '揭阳机场': 'JUA', '揭阳南': 'JRQ', '江永': 'JYZ',
                      '江源': 'SZL', '靖远': 'JYJ', '缙云': 'JYH', '济源': 'JYF', '金月湾': 'PYQ', '靖远西': 'JXJ', '缙云西': 'PYH',
                      '胶州北': 'JZK', '焦作东': 'WEF', '晋中': 'JZV', '靖州': 'JEQ', '景州': 'JEP', '胶州': 'JXK', '旧庄窝': 'JVP',
                      '金杖子': 'JYD', '康城': 'KCP', '宽甸': 'KDT', '克东': 'KOB', '昆都仑召': 'KDC', '库尔木依': 'VPR', '开江': 'KAW',
                      '喀喇其': 'KQX', '开平南': 'PVQ', '口前': 'KQL', '奎山': 'KAB', '葵潭': 'KTQ', '康熙岭': 'KXZ', '克一河': 'KHX',
                      '开远南': 'KUM', '昆玉': 'ESR', '冷坝': 'LBE', '琅勃拉邦': 'VJM', '来宾': 'UBZ', '老边': 'LLT', '灵璧': 'GMH',
                      '寮步': 'LTQ', '洛川东': 'LRY', '罗城': 'VCZ', '乐昌': 'LCQ', '黎城': 'UCP', '临城': 'UUP', '蓝村': 'LCK',
                      '乐东': 'UQQ', '林东': 'LRC', '乐都': 'LDO', '梁底下': 'LDP', '六道河子': 'LVP', '鲁番': 'LVM', '落垡': 'LOP',
                      '来凤': 'LFA', '龙丰': 'KFQ', '禄丰南': 'LQM', '老府': 'UFD', '兰岗': 'LNB', '龙骨甸': 'LGM', '临高南': 'KGQ',
                      '芦沟': 'LOM', '龙沟': 'LGJ', '临海': 'UFH', '凌海': 'JID', '拉哈': 'LHX', '林海': 'LXX', '滦河': 'UDP',
                      '临海南': 'LHU', '凌海南': 'UNT', '龙华': 'LHP', '滦河沿': 'UNP', '六合镇': 'LEX', '罗江东': 'IKW', '亮甲店': 'LRT',
                      '刘家河': 'LVT', '廉江': 'LJZ', '罗江': 'LJW', '柳江': 'UQZ', '两家': 'UJT', '李家': 'LJB', '龙江': 'LJX',
                      '莲江口': 'LHB', '利津南': 'LNK', '李家坪': 'LIJ', '厉家寨': 'UPK', '林口南': 'LRB', '路口铺': 'LKQ', '老莱': 'LAX',
                      '龙里北': 'KFW', '沥林北': 'KBQ', '兰陵北': 'COK', '醴陵东': 'UKQ', '临澧': 'LWQ', '零陵': 'UWZ', '陆良': 'LRM',
                      '卢龙': 'UAP', '喇嘛甸': 'LMX', '里木店': 'LMB', '洛门': 'LMJ', '芦庙': 'LMU', '龙南': 'UNG', '龙南东': 'LBG',
                      '六盘水东': 'LDE', '落坡岭': 'LPP', '六盘山': 'UPJ', '乐平市': 'LPG', '洛浦': 'LVR', '临清': 'UQK', '礼泉南': 'UNY',
                      '龙泉市': 'LVU', '礼泉': 'LGY', '临泉': 'LOU', '乐山北': 'UTW', '冷水江东': 'UDQ', '连山关': 'LGT', '流水沟': 'USP',
                      '灵石': 'LSV', '露水河': 'LUL', '罗山': 'LRN', '涟水': 'LIU', '龙市': 'LAG', '梁山': 'LMK', '鲁山': 'LAF',
                      '娄山关南': 'LSE', '柳树屯': 'LSD', '李石寨': 'LET', '龙山镇': 'LAS', '梨树镇': 'LSB', '轮台': 'LAR', '龙塘坝': 'LBM',
                      '濑湍': 'LVZ', '龙塘镇': 'LVB', '李旺': 'VLJ', '狼尾山': 'LRJ', '灵武': 'LNJ', '莱芜西': 'UXK', '岚县': 'UXV',
                      '朗县': 'LIO', '芦溪': 'LUG', '临湘': 'LXQ', '滦县': 'UXP', '林西': 'LXC', '朗乡': 'LXB', '郎溪南': 'LXU',
                      '莱西南': 'LXK', '莱阳': 'LYK', '凌源东': 'LDD', '临沂东': 'UYK', '老营': 'LXL', '临邑': 'LUK', '临颍': 'LNF',
                      '龙游南': 'LYU', '龙游': 'LMH', '林源': 'LYX', '鹿寨北': 'LSZ', '临淄北': 'UEK', '临泽': 'LEJ', '龙爪沟': 'LZT',
                      '雷州': 'UAQ', '来舟': 'LZS', '鹿寨': 'LIZ', '拉鲊': 'LEM', '六枝南': 'LOE', '临泽南': 'LDJ', '马鞍山': 'MAH',
                      '毛坝': 'MBY', '毛坝关': 'MGY', '明城': 'MCL', '毛陈': 'MHN', '渑池': 'MCF', '庙城': 'MAP', '茅草坪': 'KPM',
                      '猛洞河': 'MUQ', '磨刀石': 'MOB', '民丰': 'MFR', '明港': 'MGN', '明港东': 'MDN', '马皇': 'MHZ', '墨江': 'MJM',
                      '闵集': 'MJN', '马兰': 'MLR', '汨罗东': 'MQQ', '民乐': 'MBJ', '马莲河': 'MHB', '茅岭': 'MLZ', '庙岭': 'MLL',
                      '米林': 'MIO', '麻柳': 'MLY', '马林': 'MID', '茂林': 'MLD', '马龙': 'MGM', '木里图': 'MUD', '汨罗': 'MLQ',
                      '玛纳斯湖': 'MNR', '牟平': 'MBK', '民权北': 'MIF', '马桥河': 'MQB', '闽清': 'MQS', '眉山': 'MSW', '明水河': 'MUT',
                      '蒙山': 'MOK', '麻山': 'MAB', '马踏': 'PWQ', '眉县东': 'CXY', '美溪': 'MEB', '麻阳': 'MVQ', '米易东': 'MDE',
                      '麦园': 'MYS', '麻阳西': 'MYA', '庙庄': 'MZJ', '米脂': 'MEY', '明珠': 'MFQ', '南博山': 'NBK', '牛车河': 'NHA',
                      '宁城': 'NCD', '南仇': 'NCK', '南城司': 'NSP', '宁都': 'NIG', '宁洱': 'NEM', '南芬北': 'NUT', '南观村': 'NGP',
                      '南宫东': 'NFP', '南关岭': 'NLT', '宁国': 'NNH', '南河川': 'NHJ', '南华': 'NAM', '宁化': 'NHS', '内黄': 'NUF',
                      '泥河子': 'NHD', '内江东': 'NDE', '宁家': 'NVT', '能家': 'NJD', '南靖': 'NJS', '南江口': 'NDQ', '南口前': 'NKT',
                      '南朗': 'NNQ', '奈林皋': 'NGT', '乃林': 'NLD', '南陵': 'LLH', '尼勒克': 'NIR', '宁明': 'NMZ', '南木': 'NMX',
                      '南堡北': 'TLP', '南桥': 'NQD', '南台': 'NTT', '南头': 'NOQ', '南屯': 'NTR', '乃托': 'YHW', '南湾子': 'NWP',
                      '泥溪': 'NIE', '宁县': 'AXJ', '内乡': 'NXF', '牛心台': 'NXT', '宁乡西': 'NXA', '娘子关': 'NIP', '南漳': 'NZN',
                      '南召': 'NAF', '南杂木': 'NZT', '蓬安': 'PAW', '平安': 'PAL', '磐安南': 'PNU', '普安县': 'PUE', '平安驿': 'PNO',
                      '平安镇': 'PZT', '磐安镇': 'PAJ', '屏边': 'PBM', '平坝南': 'PBE', '蒲城': 'PCY', '裴德': 'PDB', '普定': 'PGW',
                      '偏店': 'PRP', '瓢儿屯': 'PRT', '平岗': 'PGL', '平果': 'PGZ', '平关': 'PGM', '盘关': 'PAM', '徘徊北': 'PHP',
                      '平河口': 'PHM', '平湖': 'PHQ', '潘家店': 'PDP', '皮口南': 'PKT', '皮口': 'PUT', '偏岭': 'PNT', '屏南': 'PNS',
                      '平南南': 'PAZ', '朋普': 'PRM', '彭山北': 'PPW', '蒲石': 'PSY', '彭山': 'PSW', '彭水': 'PHW', '屏山': 'PSE',
                      '平社': 'PSV', '盘山': 'PUD', '坪上': 'PSK', '平台': 'PVT', '平田': 'PTM', '葡萄菁': 'PTW', '平旺': 'PWV',
                      '平型关': 'PGV', '蓬溪': 'KZW', '平遥': 'PYV', '彭阳': 'PYJ', '鄱阳': 'PYG', '平洋': 'PYX', '平邑': 'PIK',
                      '平原堡': 'PPJ', '平原': 'PYK', '平峪': 'PYP', '平庄北': 'PZD', '邳州东': 'PIU', '平庄': 'PAD', '邳州': 'PJH',
                      '泡子': 'POD', '平庄南': 'PND', '乾安': 'QOT', '迁安': 'QQP', '秦安': 'QGJ', '庆城': 'QHJ', '蕲春南': 'QCN',
                      '祁东北': 'QRQ', '青岛机场': 'QJK', '祁东': 'QMQ', '青堆': 'QET', '庆丰': 'QFT', '曲阜南': 'QQK', '奇峰塔': 'QVP',
                      '清河门北': 'QBD', '千河': 'QUY', '齐河': 'QIK', '清河门': 'QHD', '渠旧': 'QJZ', '潜江': 'QJN', '曲江': 'QIM',
                      '全椒': 'INH', '秦家': 'QJB', '祁家堡': 'QBT', '清涧县': 'QNY', '秦家庄': 'QZV', '七里河': 'QLD', '渠黎': 'QLZ',
                      '秦岭': 'QLY', '青莲': 'QEW', '青龙': 'QIB', '青龙山': 'QGH', '祁门': 'QIH', '且末': 'QMR', '前磨头': 'QMP',
                      '清水北': 'QEJ', '青神': 'QVW', '岐山': 'QAY', '前山': 'QXQ', '确山': 'QSN', '清水': 'QUJ', '青山': 'QSB',
                      '清水县': 'QIJ', '戚墅堰': 'QYH', '青田': 'QVH', '桥头': 'QAT', '犍为': 'JWE', '前卫': 'QWD', '前苇塘': 'QWP',
                      '祁县东': 'QGV', '黔西': 'QXE', '祁县': 'QXV', '乾县': 'QBY', '青县': 'QXP', '桥西': 'QXJ', '旗下营南': 'QNC',
                      '旗下营': 'QXC', '泉阳': 'QYL', '千阳': 'QOY', '祁阳': 'QWQ', '沁阳': 'QYF', '祁阳北': 'QVQ', '七营': 'QYJ',
                      '庆阳山': 'QSJ', '清原': 'QYT', '青州市北': 'QOK', '钦州': 'QRZ', '曲子': 'QJJ', '青州市': 'QZK', '棋子湾': 'QZQ',
                      '仁布': 'RUO', '瑞昌': 'RCG', '瑞昌西': 'RXG', '如皋': 'RBH', '如皋南': 'RNU', '容桂': 'RUQ', '榕江': 'RVW',
                      '任丘': 'RQP', '融水': 'RSZ', '热水': 'RSD', '乳山': 'ROK', '容县': 'RXZ', '饶阳': 'RVP', '汝阳': 'RYF',
                      '绕阳河': 'RHD', '汝州': 'ROF', '石坝': 'OBJ', '上板城': 'SBP', '施秉': 'AQW', '上板城南': 'OBP', '石城东': 'SDG',
                      '商城': 'SWN', '舒城': 'OCH', '遂昌': 'SCU', '顺昌': 'SCS', '神池': 'SMV', '石城': 'SCT', '山城镇': 'SCL',
                      '山丹': 'SDJ', '山丹马场': 'JEJ', '绥德': 'ODY', '顺德': 'ORQ', '三道湖': 'SDL', '水洞': 'SIL', '商都': 'SXC',
                      '四道湾': 'OUD', '三都县': 'KKW', '顺德学院': 'OJQ', '胜芳': 'SUP', '四方台': 'STB', '水富': 'OTW', '三关口': 'OKJ',
                      '桑根达来': 'OGC', '上高镇': 'SVK', '沙海': 'SED', '上杭': 'JBS', '蜀河': 'SHY', '松河': 'SBM', '沙河口': 'SKT',
                      '赛汗塔拉': 'SHC', '泗洪': 'GQH', '沙后所': 'SSD', '双河市': 'OHR', '四会': 'AHQ', '三河县': 'OXP', '四合永': 'OHD',
                      '三汇镇': 'OZW', '双河镇': 'SEL', '三合庄': 'SVP', '畲江北': 'SOA', '沈家河': 'OJJ', '双吉': 'SML', '尚家': 'SJB',
                      '三江口': 'SKD', '司家岭': 'OLK', '沙井西': 'SJA', '松江镇': 'OZL', '三井子': 'OJT', '十家子': 'SJD', '三家寨': 'SMM',
                      '什里店': 'OMP', '疏勒': 'SUR', '舍力虎': 'VLD', '疏勒河': 'SHJ', '双辽': 'ZJD', '石岭': 'SOL', '石磷': 'SPB',
                      '石龙': 'SLQ', '萨拉齐': 'SLC', '索伦': 'SNT', '沙岭子': 'SLP', '石门县': 'OMQ', '神木西': 'OUY', '山南': 'SAO',
                      '肃宁': 'SYP', '神农架': 'SMN', '苏尼特左旗': 'ONC', '双牌': 'SBZ', '遂平': 'SON', '沙坡头': 'SFJ', '商丘东': 'SIF',
                      '石桥': 'SQE', '沈丘': 'SQN', '商丘南': 'SPF', '水泉': 'SID', '石人': 'SRL', '桑日': 'SRO', '狮山北': 'NSQ',
                      '三水北': 'ARQ', '松山湖北': 'KUQ', '鄯善': 'SSR', '松树': 'SFT', '石山': 'SAD', '首山': 'SAT', '三水': 'SJQ',
                      '狮山': 'KSQ', '泗水': 'OSK', '山市': 'SQB', '三十家': 'SRD', '三水南': 'RNQ', '泗水南': 'ONK', '三十里堡': 'SST',
                      '松树镇': 'SSL', '双水镇': 'PQQ', '索图罕': 'SHX', '石梯': 'STE', '三堂集': 'SDH', '神头': 'SEV', '石头': 'OTB',
                      '沙沱': 'SFM', '上万': 'SWP', '沙湾南': 'SWE', '沙湾市': 'SXR', '孙吴': 'SKB', '歙县北': 'NPH', '遂溪': 'SXZ',
                      '石岘': 'SXL', '寿县': 'SOU', '沙县': 'SAS', '始兴': 'IPQ', '随县': 'OVN', '歙县': 'OVH', '泗县': 'GPH',
                      '水茜': 'SSS', '上西铺': 'SXM', '石峡子': 'SXJ', '寿阳': 'SYV', '泗阳': 'MPH', '沭阳': 'FMH', '松阳': 'SUU',
                      '水洋': 'OYP', '三阳': 'SYU', '射阳': 'SAU', '双洋': 'SQS', '绥阳': 'SYB', '松原北': 'OCT', '邵阳北': 'OVQ',
                      '三阳川': 'SYJ', '上腰墩': 'SPJ', '三营': 'OEJ', '山阴': 'SNV', '三义井': 'OYD', '上虞南': 'SVU', '三源浦': 'SYL',
                      '上园': 'SUD', '三原': 'SAY', '上虞': 'BDH', '邵阳西': 'SXA', '绥中北': 'SND', '深圳机场北': 'SBA', '嵊州北': 'SEU',
                      '孙镇': 'OZY', '神州': 'SRQ', '桑植': 'SZA', '深州': 'OZP', '肃州': 'SRJ', '松滋': 'SIN', '十字门': 'SIA',
                      '师宗': 'SEM', '苏州园区': 'KAH', '苏州新区': 'ITH', '台安': 'TID', '台安南': 'TAD', '通安驿': 'TAJ', '桐柏': 'TBF',
                      '太仓': 'TCU', '桃村北': 'TOK', '桐城东': 'TOU', '铁厂沟': 'TJR', '铁厂': 'TCL', '郯城': 'TZK', '桐城': 'TTH',
                      '桐城南': 'TUU', '太仓南': 'TNU', '铁刹山': 'PST', '桃村': 'TCK', '田东北': 'TBZ', '田东': 'TDZ', '天岗': 'TGL',
                      '太谷东': 'TEV', '铁干里克': 'VAR', '土贵乌拉': 'TGC', '通沟': 'TOL', '太谷西': 'TIV', '太和北': 'JYN', '太和东': 'TDU',
                      '唐河': 'THF', '唐海南': 'IEP', '通化县': 'TXL', '团结': 'TIX', '谭家井': 'TNJ', '唐家湾': 'PDQ', '统军庄': 'TZP',
                      '铜陵北': 'KXH', '吐列毛杜': 'TMD', '图里河': 'TEX', '亭亮': 'TIZ', '田林': 'TFZ', '天门': 'TMN', '太姥山': 'TLS',
                      '土牧尔台': 'TRC', '土门子': 'TCJ', '洮南': 'TVT', '太平川': 'TIT', '太平镇': 'TEB', '台前': 'TTK', '图强': 'TQX',
                      '天桥岭': 'TQL', '土桥子': 'TQJ', '甜水堡': 'TUJ', '汤山城': 'TCT', '台山': 'PUQ', '桃山': 'TAB', '唐山西': 'TSI',
                      '天台山': 'TIU', '通途': 'TUT', '通渭': 'TWJ', '田心东': 'KQQ', '藤县': 'TAZ', '同心': 'TXJ', '桐乡': 'TCH',
                      '田阳': 'TRZ', '天义': 'TND', '汤阴': 'TYF', '驼腰岭': 'TIL', '太阳山': 'TYJ', '桃源': 'TYA', '汤原': 'TYB',
                      '通远堡西': 'TST', '塔崖驿': 'TYP', '滕州': 'TXK', '天镇': 'TZV', '天祝': 'TZJ', '天柱山': 'QWH', '武安': 'WAP',
                      '文安': 'WBP', '万安县': 'WAG', '王安镇': 'WVP', '吴堡': 'WUY', '五叉沟': 'WCT', '吴川': 'WAQ', '温春': 'WDB',
                      '五大连池': 'WRB', '文登东': 'WGK', '文登': 'WBK', '五道沟': 'WDL', '五道河': 'WHP', '文地': 'WNZ', '卫东': 'WVT',
                      '望都': 'WDP', '武当山西': 'WWN', '乌尔旗汗': 'WHX', '潍坊北': 'WJK', '五府山': 'WFG', '王府': 'WUT', '湾沟': 'WGL',
                      '吴官田': 'WGM', '威虎岭北': 'WBL', '威海北': 'WHK', '芜湖北': 'WBU', '芜湖南': 'RVH', '卫辉南': 'WVF', '卫辉': 'WHF',
                      '吴家川': 'WCJ', '渭津': 'WJL', '午汲': 'WJP', '威箐': 'WAM', '魏家泉': 'WJR', '倭肯': 'WQB', '五龙背': 'WBT',
                      '五龙背东': 'WMT', '瓦拉干': 'WVX', '五莲': 'WLK', '卧龙寺': 'WLY', '乌兰木图': 'VLT', '卧里屯': 'WLX', '望牛墩': 'WNA',
                      '乌奴耳': 'WRX', '万宁': 'WNQ', '万年': 'WWG', '渭南南': 'WVY', '渭南镇': 'WNJ', '吴桥': 'WUP', '万荣': 'VOM',
                      '巫山': 'WOE', '文水': 'WEV', '巍山': 'WOM', '武山': 'WSJ', '瓦石峡': 'WHR', '魏善庄': 'WSP', '五通': 'WTZ',
                      '王瞳': 'WTP', '五台山': 'WSV', '王团庄': 'WZJ', '无为': 'IIH', '瓦屋山': 'WAH', '五五': 'WVR', '武乡东': 'WVV',
                      '威信': 'WXE', '武乡': 'WUV', '闻喜': 'WXV', '卫星': 'WVB', '无锡新区': 'IFH', '王杨': 'WYB', '武义北': 'WDH',
                      '武义': 'RYH', '瓦窑田': 'WIM', '五原': 'WYC', '湾仔': 'WZA', '湾仔北': 'WBA', '苇子沟': 'WZL', '韦庄': 'WZY',
                      '五寨': 'WZV', '武陟': 'WIF', '湾沚南': 'WNU', '魏杖子': 'WKD', '微子镇': 'WQP', '兴安': 'XAZ', '新安': 'EAM',
                      '新安县': 'XAF', '新保安': 'XAP', '下板城': 'EBP', '西八里': 'XLP', '许昌北': 'EBF', '项城': 'ERN', '小村': 'XEM',
                      '新绰源': 'XRX', '下城子': 'XCB', '喜德': 'EDW', '小得江': 'EJM', '西大庙': 'XMP', '小董': 'XEZ', '小东': 'XOD',
                      '西渡': 'XDA', '喜德西': 'XXE', '襄汾': 'XFV', '信丰': 'EFG', '襄汾西': 'XTV', '信丰西': 'XFG', '新干': 'EGG',
                      '孝感': 'XGN', '新干东': 'XGG', '兴国西': 'XIG', '夏格庄': 'XZK', '西岗子': 'NBB', '宣化北': 'VJP', '西湖东': 'WDQ',
                      '新和': 'XIR', '宣和': 'XWJ', '香河': 'XHI', '襄河': 'XXB', '斜河涧': 'EEP', '新华屯': 'XAX', '新华': 'XHB',
                      '新化': 'EHQ', '宣化': 'XHP', '西华': 'EHF', '小河沿': 'XYD', '下花园': 'XYP', '小河镇': 'EKY', '徐家店': 'HYK',
                      '峡江': 'EJG', '新绛': 'XJV', '仙居南': 'XNU', '许家屯': 'XJT', '兴凯': 'EKB', '小榄': 'EAQ', '香兰': 'XNB',
                      '新李': 'XLJ', '西柳': 'GCT', '西林': 'XYB', '新林': 'XPX', '新立屯': 'XLD', '兴隆县西': 'IRP', '西麻山': 'XMB',
                      '下马塘': 'XAT', '孝南': 'XNV', '咸宁北': 'XRN', '咸宁东': 'XKN', '兴宁': 'ENQ', '咸宁': 'XNN', '兴平': 'XPY',
                      '西平': 'XPN', '新坪田': 'XPM', '西平西': 'EGQ', '新邱': 'XQD', '新青': 'XQB', '兴泉堡': 'XQJ', '仙人桥': 'XRL',
                      '小寺沟': 'ESP', '夏石': 'XIZ', '浠水': 'XZN', '杏树': 'XSB', '下社': 'XSV', '徐水': 'XSP', '浠水南': 'VNN',
                      '杏树屯': 'XDT', '许三湾': 'XSJ', '响水县': 'XSU', '邢台': 'XTP', '湘潭北': 'EDQ', '仙桃西': 'XAN', '下台子': 'EIP',
                      '小湾东': 'XNM', '徐闻': 'XJQ', '新窝铺': 'EPD', '西乌旗': 'XWD', '修武': 'XWF', '修武西': 'EXF', '新县': 'XSN',
                      '息县': 'ENN', '湘乡': 'XXQ', '萧县': 'EOH', '新乡南': 'ENF', '新兴县': 'XGQ', '西小召': 'XZC', '小西庄': 'XXP',
                      '向阳': 'XDB', '旬阳北': 'XBY', '咸阳北': 'EBY', '襄垣东': 'EAF', '兴业': 'SNZ', '小雨谷': 'XHM', '新沂': 'VIH',
                      '小月旧': 'XFM', '新沂南': 'XYU', '仙游': 'XWS', '小扬气': 'XYX', '襄垣': 'EIF', '夏邑县': 'EJH', '新友谊': 'EYB',
                      '新阳镇': 'XZJ', '新帐房': 'XZX', '悬钟': 'XRP', '汐子': 'XZD', '西哲里木': 'XRD', '新杖子': 'ERP', '永安': 'YAS',
                      '永安乡': 'YNB', '盐边': 'YBE', '元宝山': 'YUD', '羊草': 'YAB', '永城北': 'RGH', '秧草地': 'YKM', '禹城东': 'YSK',
                      '盐城大丰': 'YFU', '砚川': 'YYY', '盐池': 'YKJ', '阳岔': 'YAL', '应城': 'YHN', '宜城': 'YIN', '郓城': 'YPK',
                      '晏城': 'YEK', '禹城': 'YCK', '阳澄湖': 'AIH', '阳城': 'YNF', '迎春': 'YYB', '雁翅': 'YAP', '云彩岭': 'ACP',
                      '虞城县': 'IXH', '营城子': 'YCT', '于都北': 'YYG', '英德': 'YDQ', '云东海': 'NAQ', '尹地': 'YDM', '永定': 'YGS',
                      '阳东': 'WLQ', '园墩': 'YAJ', '永福南': 'YBZ', '阳高': 'YOV', '杨岗': 'YRB', '雨格': 'VTM', '阳高南': 'AGV',
                      '阳谷': 'YIK', '友好': 'YOB', '沿河城': 'YHP', '洋河': 'GTH', '岩会': 'AEP', '羊臼河': 'YHM', '元江': 'AJM',
                      '营街': 'YAM', '永嘉': 'URH', '余江': 'YHG', '岳家井': 'YGJ', '云居寺': 'AFP', '燕家庄': 'AZK', '永康': 'RFH',
                      '英库勒': 'YLR', '银浪': 'YJX', '运粮河': 'YEF', '伊拉哈': 'YLX', '尉犁': 'WRR', '鄢陵': 'YIF', '伊林': 'YLB',
                      '月亮田': 'YUM', '义马': 'YMF', '阳明堡': 'YVV', '云梦': 'YMN', '伊敏': 'YMX', '一面山': 'YST', '沂南': 'YNK',
                      '云南驿': 'ANM', '银瓶': 'KPQ', '营盘水': 'YZJ', '乐清东': 'OLH', '永庆': 'YQL', '杨桥': 'YQA', '源迁': 'AQK',
                      '玉泉镇': 'YFR', '永仁': 'ARM', '颍上北': 'YBU', '野三关': 'BNN', '榆树沟': 'YGP', '玉石': 'YSJ', '阳朔': 'YCZ',
                      '永寿': 'ASY', '云山': 'KZQ', '窑上': 'ASP', '玉舍': 'AUM', '沂水': 'YUK', '颍上': 'YVH', '偃师': 'YSF',
                      '月山': 'YBF', '杨树岭': 'YAD', '雁石南': 'YMS', '野三坡': 'AIP', '榆社西': 'AXV', '永寿西': 'AUY', '鹰手营子': 'YIP',
                      '源潭': 'YTQ', '于田': 'YWR', '玉田南': 'YTI', '伊通': 'YTL', '牙屯堡': 'YTZ', '烟筒屯': 'YUX', '烟台西': 'YTK',
                      '羊尾哨': 'YWM', '野象谷': 'AGM', '阳西': 'WMQ', '云县': 'AIM', '阳信': 'YVK', '应县': 'YZV', '攸县': 'YOG',
                      '永修': 'ACG', '攸县南': 'YXG', '洋县西': 'YXY', '义县西': 'YSD', '云阳': 'YUE', '酉阳': 'AFW', '弋阳': 'YIG',
                      '余姚': 'YYH', '余姚北': 'CTH', '阳邑': 'ARP', '鸭园': 'YYL', '杨源': 'AYS', '鸳鸯镇': 'YYJ', '燕子砭': 'YZY',
                      '宜州': 'YSZ', '银盏': 'YZA', '仪征': 'UZH', '耀州': 'YOY', '禹州': 'YZF', '迤资': 'YQM', '羊者窝': 'AEM',
                      '杨杖子': 'YZD', '镇安': 'ZEY', '治安': 'ZAD', '招柏': 'ZBP', '张百湾': 'ZUP', '子长': 'ZHY', '赵城': 'ZCV',
                      '枝城': 'ZCN', '邹城': 'ZIK', '诸城': 'ZQK', '章党': 'ZHT', '肇东': 'ZDB', '照福铺': 'ZFM', '准格尔': 'ZEC',
                      '章古台': 'ZGD', '赵光': 'ZGB', '政和': 'ZES', '中和': 'ZHX', '织金北': 'ZJE', '枝江北': 'ZIN', '钟家村': 'ZJY',
                      '紫荆关': 'ZYP', '朱家沟': 'ZUB', '周家屯': 'ZOD', '褚家湾': 'CWJ', '仲恺': 'ZKA', '曾口': 'ZKE', '张兰': 'ZLV',
                      '珠琳': 'ZOM', '枣林': 'ZIV', '扎鲁特': 'ZLD', '樟木头东': 'ZRQ', '樟木头': 'ZOQ', '扎囊': 'ZNO', '中宁东': 'ZDJ',
                      '中宁': 'VNJ', '周宁': 'ZNS', '中宁南': 'ZNJ', '邹平': 'ZLK', '镇平': 'ZPF', '漳浦': 'ZCS', '张桥': 'ZQY',
                      '枣强': 'ZVP', '庄桥': 'ZQH', '朱日和': 'ZRC', '中山北': 'ZGQ', '樟树东': 'ZOG', '钟山': 'ZSZ', '昭山': 'KWQ',
                      '钟山西': 'ZAZ', '支提山': 'ZIS', '珠窝': 'ZOP', '张维屯': 'ZWB', '彰武': 'ZWD', '漳县': 'ZXJ', '资溪': 'ZXS',
                      '棕溪': 'ZOY', '镇西': 'ZVT', '钟祥': 'ZTN', '张辛': 'ZIP', '正镶白旗': 'ZXC', '遵义南': 'ZNE', '竹园': 'ZUM',
                      '枣庄东': 'ZNK', '卓资东': 'ZDC', '子洲': 'ZZY', '涿州': 'ZXP', '中寨': 'ZZM', '壮志': 'ZUX', '咋子': 'ZAL',
                      '卓资山': 'ZZC', '安溪东': 'ANS', '保山': 'BAM', '北滩': 'BEJ', '白银南': 'BVJ', '茶卡': 'CVO', '德化': 'DKS',
                      '大田北': 'DTS', '富阳西': 'FUU', '革居': 'GEM', '古路': 'GOE', '花博山': 'KBT', '黄水': 'SZE', '杭州西': 'HVU',
                      '江北机场': 'JCE', '金  阳': 'WCI', '靖远北': 'JOJ', '绛帐': 'JZY', '珞璜东': 'LHE', '龙兴': 'LIE', '明溪': 'MOS',
                      '南安北': 'NUS', '南彭': 'NAE', '宁强': 'NQY', '平川西': 'PCJ', '秦王川': 'QWJ', '水土': 'SUE', '三元西': 'SRS',
                      '统景': 'TOE', '桐庐东': 'TBU', '西阳村': 'XQF', '漾濞': 'AVM', '永春': 'ACS', '银花': 'YWE', '迎龙': 'YVE',
                      '永平县': 'APM', '越西': 'YIE'}

    @classmethod
    def update_station_name(cls, session: Session) -> None:
        """
        更新火车站名称
        :param session:
        :return:
        """
        station_names = session.get(url=UrlConfig.get_station_name_url()).text
        ptn = re.compile(r'@[^|]+'  # 拼音缩写三位
                         r'\|([^|]+)'  # 站点名称
                         r'\|([^|]+)'  # 编码
                         r'\|[^|]+'  # 拼音
                         r'\|[^|]+'  # 拼音缩写
                         r'\|[^@]+',  # 序号
                         re.X)
        GlobalConfig.__station_name = dict(ptn.findall(station_names))

    @classmethod
    def get_station_name(cls, ) -> dict:
        """
        返回火车站名称
        :return:
        """

        return GlobalConfig.__station_name


class SeatType(object):

    def __init__(self):
        raise MyError(error_messages="SeatType对象不能被创建。")

    """
    座位类型
    """
    # 无座
    NO_SEAT = '1'
    # 硬座
    HARD_SEAT = '1'

    # 软座
    SOFT_SEAT = None

    # 硬卧
    HARD_SLEEPER = '3'
    # 二等卧
    SECOND_CLASS_BEDROOM = None

    # 软卧
    SOFT_SLEEPER = '4'
    # 一等卧
    FIRST_CLASS_SLEEPER = None

    # 高级软卧
    PREMIUM_SOFT_SLEEPER = None

    # 二等座
    SECOND_CLASS = 'O'
    # 二等包座
    _2ND_CLASS_PRIVATE_SEAT = None

    # 一等座
    FIRST_CLASS = 'M'

    # 商务座
    BUSINESS_SEAT = '9'
    # 特等座
    STATE_CLASS = 'P'

    # 动卧
    LIE_DOWN = None



    __seat_type_str_cn = {
        '1': '硬座',
        '11': '无座',
        '3': '硬卧',
        '4': '软卧',
        '9': '商务座',
        'O': '二等座',
        'P': '特等座',
        'M': '一等座',

    }

    @classmethod
    def get_seat_type_str_cn(cls) -> dict:
        """

        :return:
        """
        return cls.__seat_type_str_cn

    __seat_type_str_en = {
        None: 'gg_num', '高级软座': 'gr_num', '其他': 'qt_num', '4': 'rw_num', '软座': 'rz_num',
        'P': 'tz_num', '11': 'wz_num', None: 'yb_num', '3': 'yw_num', '1': 'yz_num',
        'O': 'ze_num', 'M': 'zy_num', '9': 'swz_num', '动卧': 'srrb_num'
    }

    @classmethod
    def get_seat_type_str_en(cls) -> dict:
        """

        :return:
        """
        return cls.__seat_type_str_en


class TicketType(object):
    def __init__(self):
        raise MyError(error_messages="TicketType对象不能被创建。")

    """
    # 车票类型
    """
    # 成人票
    ADULT_TICKETS = '1'
    # 儿童票
    CHILD_TICKETS = '2'
    # 学生票
    STUDENT_TICKETS = '3'
    # 残军票
    REMNANT_TICKETS = '4'
