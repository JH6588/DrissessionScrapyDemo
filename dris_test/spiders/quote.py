import scrapy
from dris_test.http import DrissessionPageRequest

class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    def start_requests(self):
        url = 'https://quotes.toscrape.com/js/'
        yield DrissessionPageRequest(url=url, callback=self.parse)

    def parse(self, response):
        quote_item = {}
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item