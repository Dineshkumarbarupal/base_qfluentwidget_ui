import scrapy
from pathlib import Path

class LaptopData(scrapy.Spider):
    name = "laptop"
    start_urls = [
        "https://www.meesho.com/search?q=laptop&searchType=manual&searchIdentifier=text_search"
    ]
    
    def parse(self, response):
        filename = "meesho.html"
        
        # Save the HTML content as a readable text file
        Path(filename).write_text(response.text, encoding='utf-8')
        self.log(f"File saved: {filename}")
