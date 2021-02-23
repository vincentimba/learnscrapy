import scrapy


class ZhangbhSpider(scrapy.Spider):  # 创建了一个类 ZhangbhSpider，从 scrapy.Spider 继承而来
    name = 'zhangbh'  # 爬虫名称
    # allowed_domains = ['zhangbh.com']  # 域名，非必须
    start_urls = {'https://zhangbh.xyz'}  # 要爬取的网页地址

    def parse(self, response):  # 对于网站的解析方法，这里的 response 指获取到的网页源代码
        selectors = response.xpath('//article/header/h2/a')
        for slector in selectors:
            url = slector.xpath('./@href')
            post_title = slector.xpath('./text()')
            print(url.get(), post_title.get())
        next_page = response.xpath("//a[@class='extend next']/@href").get()
        # 提取到每一页中下一页的 url
        if next_page:
            next_url = response.urljoin(next_page)
            # 对获取到的下一页 url 进行网址拼接
            yield scrapy.Request(next_url, callback=self.parse)
            # 对 next_url 进行请求
            # 利用回调函数，将得到的 response 再返回给自己来处理
