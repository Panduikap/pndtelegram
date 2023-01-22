from kimin.Core_Scraping import Scraping
from kimin.Core_Scraping import Notifikasi
from scrapy.crawler import CrawlerProcess

import json, time

def Phase1():
	with open('url.min','r') as dataku:
		url = dataku.read().splitlines()

	with open('user_id.min', 'r') as dataku:
		user_id = dataku.read().splitlines()

	with open('token.min', 'r') as dataku:
		token = dataku.read()
		
	Notifikasi.SetData(url)
	Notifikasi.SetID(user_id)
	Notifikasi.SetToken(token)
	process = CrawlerProcess(
		{
			'DOWNLOD_DELAY': 2,
			'CONCURRENT_REQUESTS':2
		})

	process.crawl(Scraping, DOWNLOADER_MIDDLEWARES = {
			'scrapy_splash.SplashCookiesMiddleware': 723,
			'scrapy_splash.SplashMiddleware': 725,
			'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
			},
		SPIDER_MIDDLEWARES = {
			'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
			},
		DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter',
		HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
		)
	process.start()

Phase1()
	