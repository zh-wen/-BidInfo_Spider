#coding=utf-8
import scrapy
import re
from cq_Spider.items import CqSpiderItem
from scrapy.http import FormRequest,Request

class DdkSpider(scrapy.Spider):
	name = 'cqhc'
	allowed_domains = ["www.cqhcjy.com"]
	start_urls = [
	"http://www.cqhcjy.com/lbWeb/n_newslist_zz_item.aspx?Item=200011"
	]
	head_url = "http://www.cqhcjy.com/lbWeb/"
	x = 1

	def parse(self,response):
		current_page = response.xpath('//*[@id="ctl00_ContentPlaceHolder2_A2"]//text()').extract().pop()
		print current_page
		page_count = response.xpath('//*[@id="ctl00_ContentPlaceHolder2_A1"]//text()').extract().pop()
		nextpage = response.xpath('//*[@id="ctl00_ContentPlaceHolder2_F3"]/@value').extract().pop()
		viewstate = response.xpath('//*[@id="__VIEWSTATE"]/@value').extract().pop()
		eventvalidation = response.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract().pop()
		if self.x < int(page_count):	
			yield FormRequest(self.start_urls[0],
							formdata = {
							'__VIEWSTATE': viewstate,
							'__EVENTVALIDATION': eventvalidation,
							'ctl00$ContentPlaceHolder2$F3':nextpage,
							},
							callback = self.parse
			                  )
			self.x += 1
		linklist = response.xpath('//nobr/a/@href').extract()
		for link in linklist:
			yield Request(url = self.head_url + link,callback = self.parse_page_content)

	def parse_page_content(self,response):
		item = CqSpiderItem()
		page_content = response.xpath('//tr[2]/td[2]//tr[2]/td//tr[4]/td[2]/div[1]').extract()
		if page_content:
			page_content = page_content.pop()
			page_content = re.sub('<[^>]+>',' ',page_content)
			item['page_content'] = page_content
			item['link'] = response.url
			return item
	
