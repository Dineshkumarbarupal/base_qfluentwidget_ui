import scrapy
from fake_useragent import UserAgent

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    ua = UserAgent()

    def start_requests(self):
        url = "https://www.amazon.com/"
        headers = {'User-Agent': self.ua.random}
        yield scrapy.Request(url=url, headers=headers, callback=self.parse)




