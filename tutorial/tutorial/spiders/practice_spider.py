from pathlib import Path 
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes2"

    def start_requests(self):

        url = "https://www.amazon.in/s?k=laptop&page=2&crid=39XWLS20P7RXU&qid=1735206283&sprefix=laptop%2Caps%2C333&ref=sr_pg_2"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        filename = "amazon2.html"
        Path(filename).write_bytes(response.body)
        self.log(f"saved file {filename}")






