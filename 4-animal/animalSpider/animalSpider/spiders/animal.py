import scrapy
from animalSpider.items import AnimalspiderItem
# 虽然这里在 Pycharm 上会报错，但不影响程序的运行
# 解决方法为：在 Pycharm 中右键 root 目录，将其设为项目的根目录
# 当然保险期间也可以使用下面相对目录的写法
# from ..items import AnimalspiderItem
import re

class AninmalSpider(scrapy.Spider):
    name = 'animal'
    allowed_domains = ['www.iltaw.com']

    def start_requests(self):
        url = 'http://www.iltaw.com/animal/all?page='
        page_num = 1
        page_url = url + str(page_num)
        yield scrapy.Request(page_url,
                             callback=self.parse,
                             meta={'page_num': page_num})

    # 在代码调试过程中，出现了不能正确调用回调函数的问题，表现为一直不能解析具体图片 url 的内容
    # 在排查了 allowed_domains 的设置和过滤开关的设置后，最终缺点是 Request 优先级的问题
    # 可以在 scrapy.Request(page_url, callback=self.parse, priority=10) 中设置优先级
    # Request 的优先级用 priority 的数字参数来定义。数字越大，优先级越高。
    # 但我这里还是选择更改整个爬虫的结构来改变优先级的问题

    def parse(self, response):  # 第一个 parse 方法用来获取每一页上各个动物页面的 url
        # 先从 Request 中的 meta 字典中取出相应的页数
        page_num = response.meta['page_num']
        # 获取这一页内的动物的链接，并将其调入 parse_animal 方法中处理
        print('#####开始处理第{}页的内容#####'.format(page_num))
        print('#######[{}]#######'.format(response.url))
        animal_urls = response.xpath("//li[@class='clearfix']/div[1]/a/@href").extract()
        for url in animal_urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_animal)
        # 处理完毕后，定义下一页的 url
        next_page_num = page_num + 1
        if next_page_num <= 80:
            next_page_url = 'http://www.iltaw.com/animal/all?page=' + str(next_page_num)
            yield scrapy.Request(next_page_url,
                                 callback=self.parse,
                                 meta={'page_num': next_page_num})
        else:
            print('##############爬取完毕#############')
            # 先判断页数是否小于等于80，接着再组合出 url ，将其代入自己重新来过
            # 简直就是俄罗斯套娃

    def parse_animal(self, response):
        # 提取需要的各项信息
        name = response.xpath("/html/body/div[1]/div/div[2]/div/div[2]/h3/text()").get()
        img_url = response.xpath('//div[@class="img"]/img/@data-url').get()
        # 这里的图片 url 信息也可以使用了正则表达式来抓取，如下
        # img_url = re.findall('"bdPic":"(.*?)","bdStyle', response.body.decode('utf-8'), re.S)[0]
        # 由于在 html 原文中，各个文字内容终究有着隔断，所以用 join 函数来将他们连接到一起
        animal_info = "".join(response.xpath('/html/body/div[1]/div/div[4]/div/div[2]/text()').extract())
        # 调用自己继承创建的 Item，并将相应的内容导入
        animal_item = AnimalspiderItem()
        animal_item['name'] = name
        animal_item['img_url'] = img_url
        animal_item['animal_info'] = animal_info.strip()
        # 将封装好信息的实例抛出
        yield animal_item


