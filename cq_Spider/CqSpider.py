import scrapy

class CqSpider(scrapy.Spider):
	name = "cqspider"
	allowed_domains = [cqzb.com]
	start_urls=[
		"http://www.cqzb.com/ciiccms/cqztb/category/zfcg/zfcg_cgjggg/list.html"
    ]

	headers = {
	Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
	Accept-Encoding:gzip, deflate
	Accept-Language:zh-CN,zh;q=0.8
	
}
