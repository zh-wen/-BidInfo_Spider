# -*- coding: utf-8 -*-

# Scrapy settings for cqspider1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cqspider'

SPIDER_MODULES = ['cqspider.spiders']
NEWSPIDER_MODULE = 'cqspider.spiders'

ITEM_PIPELINES = {
    'cqspider.pipelines.CqspiderPipeline':300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cqspider1 (+http://www.yourdomain.com)'
