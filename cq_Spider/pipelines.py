# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import MySQLdb
from scrapy.exceptions import DropItem
from scrapy.http import Request
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class CqspiderPipeline(object):
	pass
	def __init__(self):
		self.conn = MySQLdb.connect(user = '----',
								passwd = '----',
								db = 'nuaa_se',
								host = 'localhost',
								charset="utf8",
								use_unicode=True)
		self.cursor = self.conn.cursor()
    
	def process_item(self,item,spider):	
		try:
			if item['project_name'] and item['bid_name'] and item['bid_money'] and item['bid_time']:	
				self.cursor.execute("""INSERT IGNORE INTO bid_info(Project_Name,Project_Bidder,Bid_Money,Bid_Time)
							VALUES (%s,%s,%s,%s)""",
							(item['project_name'],
							item['bid_name'],
							item['bid_money'],
							item['bid_time']))
				self.conn.commit()
    
		except MySQLdb.Error,e:
				print "Error %d: %s " %(e.args[0],e.args[1])
    
	 	return item
