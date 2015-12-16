#coding=utf-8
import scrapy
import re
from cq_Spider.items import CqSpiderItem
from scrapy.http import FormRequest,Request

class DdkSpider(scrapy.Spider):
	name = 'cqddk'
	allowed_domains = ["www.ddkggzy.com"]
	start_urls = [
	"http://www.ddkggzy.com/lbWeb/n_newslist_zz_item.aspx?Item=200011"
	]

	head_url = "http://www.ddkggzy.com/lbWeb/"
	
	def parse(self,response):
		nextpage = response.xpath('//*[@id="ctl00_ContentPlaceHolder2_F3"]/@value').extract()
		viewstate = response.xpath('//*[@id="__VIEWSTATE"]/@value').extract().pop()
		eventvalidation = response.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract().pop()
		pagenum = response.xpath('//*[@id="ctl00_ContentPlaceHolder2_A2"]').extract()
		if nextpage:
				yield FormRequest(self.start_urls[0],
						formdata = {
						'__EVENTTARGET':'', 
						'__EVENTARGUMENT':'',
						'__VIEWSTATE': viewstate,
						'ctl00$n_list7$searchBox':'',
						'ctl00$ContentPlaceHolder2$F3': nextpage,
						'__EVENTVALIDATION': eventvalidation
						},
						callback = self.parse
						) 	
		
		linklist = response.xpath('//nobr/a/@href').extract()
		for link in linklist:
			yield Request(url = self.head_url + link, callback = self.parse_page_content)

	def parse_page_content(self,response):
		item = CqSpiderItem()
		page_content = response.xpath('//*[@id="bulletinContent"]/tbody').extract()
		page_content = response.xpath('//tr/td[3]/table').extract()
		if page_content:
			page_content = page_content.pop()
			page_content = re.sub('<[^>]+>',' ',page_content)
			print page_content
			item['page_content'] = page_content
			item['link'] = response.url
			return item

