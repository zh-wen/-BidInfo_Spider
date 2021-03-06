#coding=utf-8
import scrapy
import re
from cq_Spider.items import CqSpiderItem
from scrapy.http import FormRequest,Request

class DdkSpider(scrapy.Spider):
	name = 'cqwz'
	allowed_domains = ["www.wzqztb.com"]
	start_urls = [
	"http://www.wzqztb.com/wzweb/jyxx/001004/001004004/MoreInfo.aspx?CategoryNum=001004004"
	]
	head_url = "http://www.wzqztb.com"
	
	def parse(self,response):
		page_count = response.xpath('//*[@id="MoreInfoList1_Pager"]//tr/td[1]/font[2]/b/text()').extract().pop()
		print page_count
		viewstate = response.xpath('//*[@id="__VIEWSTATE"]/@value').extract().pop()
		x = 1;
		while x <= int(page_count):	
			yield FormRequest(self.start_urls[0],
						formdata = {
						'__VIEWSTATE': viewstate,
						'__EVENTTARGET': 'MoreInfoList1$Pager',
						'__EVENTARGUMENT': str(x)
						},
						callback = self.parse_catalogue
						) 	
			x += 1
		
	def parse_catalogue(self,response):		
		num = response.xpath('//tr/td[1]/font[3]/b/text()').extract().pop()
		linklist = response.xpath('//*[@id="MoreInfoList1_DataGrid1"]//tr/td/a/@href').extract()
		for link in linklist:
			yield Request(url = self.head_url + link, callback = self.parse_page_content)

	def parse_page_content(self,response):
		item = CqSpiderItem()
		page_content = response.xpath('//*[@id="bulletinContent"]').extract()
		if page_content:
			page_content = page_content.pop()
			page_content = re.sub('<[^>]+>',' ',page_content)
			item['page_content'] = page_content
			item['link'] = response.url
			return item
	
