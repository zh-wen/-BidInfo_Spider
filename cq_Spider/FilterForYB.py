# coding=utf-8
import re
import sys

import time

import datetime

reload(sys)
sys.setdefaultencoding( "utf-8" )
class FilterForYB:
    def __init__(self,str = ''):
        self.str = str
    def get_project_name(self):
        str = self.str
        re_project_name = u"(?<=\u9879\u76ee\u540d\u79f0.)\s*([\u4e00-\u9fff]+\([\u4e00-\u9fff]+\)[\u4e00-\u9fff]*|[\u4e00-\u9fff]+)"
        re_project_name = re.compile(re_project_name)
        m_project_name = re_project_name.findall(str)
        if m_project_name:
            #for l in m_project_name:
            l = m_project_name[0]
            l = l.decode()
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            return l
    def get_bid_name(self):
        str = self.str
        re_bid_name=u"[\u4e00-\u9fff]+\([\u4e00-\u9fff]+\)\u516c\u53f8|[\u4e00-\u9fff]+\u516c\u53f8"
        re_bid_name = re.compile(re_bid_name)
        m_bid_name = re_bid_name.findall(str)
        if m_bid_name:
            l = m_bid_name[0]
            l = l.decode()
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            if "流标" in l:
                return None
            else:
                return l

    def get_bid_money(self):
        str = self.str
        re_bid_money = u"\d+\.?\d*\s*[\u4e00-\u9fff]?(?=\u5143)|\d+\.\d*(?=\s)"
        re_bid_money = re.compile(re_bid_money)
        m_bid_money = re_bid_money.findall(str)
        if m_bid_money:
            #for l in m_project_name:
            l = m_bid_money[0]
            l = l.decode()
            l = l.replace(u'\xa0', u' ')
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            l = l.replace(',','')
            money = re.search("\d+\.?\d*",l)
            money = float(money.group(0))
            unit = "万"
            unit = unit.decode("utf8")
            if(re.search(unit,l)):
                money *= 10000
            return money
    def get_bid_time(self):
        str = self.str
        re_bid_time = u"(?<=\u6210\u4ea4\u4eba\u65e5\u671f).\s*\d+\s*\u5e74\s*\d+\s*\u6708\s*\d+\s*\u65e5|(?<=\u8bc4\u5ba1\u65e5\u671f).\s*\d+\s*\u5e74\s*\d+\s*\u6708\s*\d+\s*\u65e5|(?<=\u8bc4\u5ba1\u65e5\u671f).\s*\d+\s*-\s*\d+\s*-\s*\d+"
        re_bid_time = re.compile(re_bid_time)
        m_bid_time = re_bid_time.findall(str)
        if m_bid_time:
            #for l in m_project_name:
            l = m_bid_time[0]
            l = l.decode()
            l = l.replace('；','')
            l = l.replace('。','')
            l = l.replace('：','')
            l = l.replace('\r','')
            l = l.replace('\n','')
            l = l.replace(' ','')
            re_money = u"\d+\u5e74\d+\u6708\d+\u65e5"
            re_money = re.compile(re_money)
            l = re_money.findall(l)
            l = l[0]
            l = time.strptime(l,u"%Y\u5e74%m\u6708%d\u65e5")
            l = datetime.date(l.tm_year,l.tm_mon,l.tm_mday)
            l = l.strftime("%Y-%m-%d %H:%M:%S")
            return l