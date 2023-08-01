# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdFbsScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    big_category = scrapy.Field()  # 大分类
    big_category_link = scrapy.Field()  # 大分类链接
    small_category = scrapy.Field()  # 小分类
    small_category_link = scrapy.Field()  # 小分类链接
    bookName = scrapy.Field()  # 书名
    shopName = scrapy.Field()  # 作者
    link = scrapy.Field()  # 链接
    price = scrapy.Field()  # 价格
