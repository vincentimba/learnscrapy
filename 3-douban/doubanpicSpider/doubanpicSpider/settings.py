# Scrapy settings for doubanpicSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubanpicSpider'

SPIDER_MODULES = ['doubanpicSpider.spiders']
NEWSPIDER_MODULE = 'doubanpicSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'doubanpicSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/53.0.2785.143 Safari/537.36 ',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9 ',
    'cookie': 'bid=J6YogCel2BY; douban-fav-remind=1; ll="118371"; '
              '_vwo_uuid_v2=D18778B832E60A13AF5C4E8AA2740173B|0076b34fbb4efb8ac35efff01c403fe3; '
              '__utma=30149280.282277331.1609641479.1613541767.1614065330.12; '
              '__utmz=30149280.1614065330.12.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; '
              'ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1614065401%2C%22https%3A%2F%2Fwww.douban.com'
              '%2Fsearch%3Fq%3D%25E9%259F%25A9%25E8%2589%25BA%25E7%2591%259F%22%5D; _pk_ses.100001.4cf6=*; '
              '__utmz=223695111.1614065401.10.9.utmcsr=douban.com|utmccn=('
              'referral)|utmcmd=referral|utmcct=/search; __utmc=223695111; __utmb=223695111.0.10.1614065401; '
              '__utma=223695111.1287014501.1609803694.1613541767.1614065401.10; regpop=1; push_doumail_num=0; '
              'push_noty_num=0; douban-profile-remind=1; ct=y; dbcl2="175091215:vBz7smx0jq0"; ck=htsS; '
              '__utmv=30149280.17509; __utmb=30149280.15.10.1614065330; '
              '_pk_id.100001.4cf6=3c25122621b40454.1609803693.10.1614066288.1613541767. ',
    'Referer': 'https://www.douban.com/'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'doubanpicSpider.middlewares.DoubanpicspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'doubanpicSpider.middlewares.DoubanpicspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'doubanpicSpider.pipelines.DoubanpicspiderPipeline': 300,
    'scrapy.pipelines.images.ImagesPipeline': 1,
}

IMAGES_STORE = 'D:\\scrapy_project\\douban_pics\\image'
IMAGES_EXPIRES = 45
IMAGES_MIN_HEIGHT = 100
IMAGES_MIN_WIDTH = 100

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
