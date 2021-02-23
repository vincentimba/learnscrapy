import scrapy
from ..items import DoubanMovie
# 这里我卡了很久，主要还是对 python 上级目录的引用方法不够熟悉


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['douban.com']
    headerssss = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36 ',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9 '
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url, headers=self.headerssss)

    def parse(self, response):
        item = DoubanMovie()  # 这里就是上级目录中引用的类 DoubanMovie 中创造一个实例 item
        movies = response.xpath('//ol[@class="grid_view"]/li')
        # 这里的 Xpath 代码非常关键，它提取了所有下层的 li，从而生成一个迭代器
        for movie in movies:  # 这里的每一个 movie 也就是一个 li 了
            item['ranking'] = movie.xpath(".//div[@class='pic']/em/text()").get()
            item['movie_name'] = movie.xpath(".//div[@class='info']/div/a/span[1]/text()").get()
            item['score'] = movie.xpath(".//div[@class='star']/span[2]/text()").get()
            item['score_num'] = movie.xpath(".//div[@class='star']/span[4]/text()").get()[:-3]
            print(item)
            yield item  # 这里犯了很低级的语法错误，yield 的缩进要注意在 for 语句内部

        next_page = response.xpath("//span[@class='next']/a/@href").get()

        if next_page:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, headers=self.headerssss)




