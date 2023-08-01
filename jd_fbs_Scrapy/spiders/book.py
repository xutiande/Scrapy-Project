import json

import scrapy
from jd_fbs_Scrapy.items import JdFbsScrapyItem
# 1.导入类
from scrapy_redis.spiders import RedisSpider


# 2.继承类
class BookSpider(RedisSpider):
    name = 'book'
    # 3.注销start_urls && allowed_domains
    # allowed_domains = ['jd.com','dc.3.cn']
    # start_urls = ['https://dc.3.cn/category/get']
    # 4.设置redis-key
    redis_key = 'py21'

    # 5.设置动态__init__
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop("domain", '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(BookSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        text = json.loads(response.text)
        big_category_len = len(text['data'][-5]['s'][0]['s'])
        for lens in range(big_category_len):
            big_category_link = {}  # 存放类名与其类名下的url地址
            big_category_link__list = text['data'][-5]['s'][0]['s'][lens]['s']  # 获取到链接处
            big_category_name_list = text['data'][-5]['s'][0]['s'][lens]['n']  # 获取类名
            big_category_name = big_category_name_list.split('|')[1]  # 提取
            link_list = []
            for i in big_category_link__list:  # 对链接进行清洗
                link = i['n'].split('|')[0]
                if '-' in link:
                    split_link = 'https://list.jd.com/list.html?cat=' + ','.join(link.split("-"))
                    link_list.append(split_link)
                else:
                    link_list.append('https://' + link)

                big_category_link['big_category'] = big_category_name
                big_category_link['big_category_link'] = link_list
                break
        print('*' * 100)
        print(big_category_link['big_category_link'][0], )
        yield scrapy.Request(
            url=big_category_link['big_category_link'][0],
            callback=self.parse_book_list,
            meta={"py21": big_category_link},
        )

    def parse_book_list(self, response):
        temp = response.meta['py21']
        book_list = response.xpath('//*[@id="J_goodsList"]/ul/li/div[1]')
        for book in book_list:
            item = JdFbsScrapyItem()
            item['big_category'] = temp['big_category']
            item['big_category_link'] = temp['big_category_link']

            # 图书信息
            item['bookName'] = book.xpath('./div[3]/a/em/text()').extract_first()
            item['shopName'] = book.xpath('./div[5]/span/a/text()').extract_first()
            item['link'] = book.xpath('./div[3]/a/@href').extract_first()
            item['price'] = book.xpath('./div[2]/strong/i/text()').extract_first()
            yield item
