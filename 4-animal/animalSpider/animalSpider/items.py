# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimalspiderItem(scrapy.Item):
    # 动物的名字
    name = scrapy.Field()
    # 动物图片的下载链接
    img_url = scrapy.Field()
    # 动物的介绍文字
    animal_info = scrapy.Field()

