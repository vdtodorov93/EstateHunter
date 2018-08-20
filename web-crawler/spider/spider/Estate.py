# import scrapy
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors import LinkExtractor
#
# class EstateSpider(scrapy.Spider):
#     name='estate'
#
#     def start_requests(self):
#         urls = ['https://www.imot.bg/pcgi/imot.cgi?act=5&adv=1c152475812917029&slink=3xeoxy&f1=1']
#
#         return [scrapy.Request(url=url, callback=self.parse) for url in urls]
#
#     def parse(self, response):
#         url = response.url
#         title = response.css('h1::text').extract_first()
#         price = response.css('h1::text').extract_first()
#         currency = response.css('h1::text').extract_first()
#         square_meters = response.css('h1::text').extract_first()
#         floor = response.css('h1::text').extract_first()
#         phone = response.css('h1::text').extract_first()
#         tec = response.css('h1::text').extract_first()
#         building_material = response.css('h1::text').extract_first()
#         neighbourhood = response.css('h1::text').extract_first()
#         house_type = response.css('h1::text').extract_first()
#         text = response.css('#description_div').extract_first()
#
#         # tableInfo = response.css('table tbody tr td table')
#         tableInfo = response.css('table')[7]
#         # tableInfo = tableInfo.css('td::text').extract()[1]
#
#         print('URL is: {}'.format(url))
#         print('Title is {}'.format(title))
#         print('price is {}'.format(price))
#         print('currency is {}'.format(currency))
#         print('square_meters is {}'.format(square_meters))
#         print('floor is {}'.format(floor))
#         print('phone is {}'.format(phone))
#         print('tec is {}'.format(tec))
#         print('building_material is {}'.format(building_material))
#         print('neighbourhood is {}'.format(neighbourhood))
#         print('house_type is {}'.format(house_type))
#         print('text is {}'.format(text))
#         print('tableInfo is {}'.format(tableInfo))
#
# # class EstateCrawlSpider(CrawlSpider):
# #     name = "imotbg"
# #     allowed_domains = ['imot.bg']
# #     start_urls = ['https://www.imot.bg/pcgi/imot.cgi?act=3&slink=3xedu2&f1=1']
# #     rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]
# #
# #
# #     def parse_items(self, response):
# #         url = response.url
# #         title = response.css('h1::text').extract_first()
# #         print('URL is: {}'.format(url))
# #         print('Title is {}'.format(title))
