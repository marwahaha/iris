# -*- coding: utf-8 -*-

# Scrapy settings for gplaycrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import os

BOT_NAME = 'gplaycrawler'

SPIDER_MODULES = ['gplaycrawler.spiders']
NEWSPIDER_MODULE = 'gplaycrawler.spiders'
CONCURRENT_REQUESTS_PER_DOMAIN = 100
ITEM_PIPELINES = {'gplaycrawler.pipelines.GplayPipeline': 100}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Alo Ventures (+http://alo.ventures)'

REACTOR_THREADPOOL_MAXSIZE = 20
LOG_LEVEL = 'DEBUG'
COOKIES_ENABLED = False
##RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 60
##REDIRECT_ENABLED = False
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1

#DB Settings
db_name = 'gplay'
db_username = 'postgres'
db_password = 'postgres'
db_host = os.environ['POSTGRES_HOST']#'127.0.0.1'