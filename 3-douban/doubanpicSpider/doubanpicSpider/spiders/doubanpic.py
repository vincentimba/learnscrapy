import scrapy
import time
import re
from ..items import DoubanpicspiderItem

# 参考文章 - https://blog.csdn.net/qq_28837549/article/details/102820099


class DoubanpicSpider(scrapy.Spider):
    name = 'doubanpic'
    allowed_domains = ['douban.com']
    start_urls = {'https://movie.douban.com/celebrity/1051057/photo/2632604481/'}  # 豆瓣艺人照片网页地址
    # 在这里输入第一页地址
    def parse(self, response):
        # 提取页面内的页数信息
        di_ji_zhang_group = response.xpath("//div[@class='article']/div/span[@class='opt-left']/text()").get()
        di_ji_zhang_group_num = re.findall('第(.*?)张/共(.*?)张', di_ji_zhang_group, re.S)

        # 提取下一页的 url
        next_page_url = response.xpath("//a[@id='next_photo']/@href").get()
        print(next_page_url)

        # 开始爬取
        image_num = int(di_ji_zhang_group_num[0][0])
        image_total_num = int(di_ji_zhang_group_num[0][1])
        print("-----------\n--------现在爬取第 {}/{} 页的内容----------\n-----------".format(image_num, image_total_num))
        if image_num <= image_total_num:
            item = DoubanpicspiderItem()
            img_url = re.findall('data-image="(.*?)\.webp', response.body.decode('utf-8'), re.S)[0]
            img_url = img_url.replace('/l/', '/raw/') + '.jpg'
            print(img_url)
            item['image_urls'] = [img_url]
            item['images'] = [image_num]
            yield item
        yield scrapy.Request(url=next_page_url, callback=self.parse)

