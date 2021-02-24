# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.spiders import Request


class AnimalSpiderPipeline(object):

    # 先创建一个用来生成目录的方法
    def create_dir(self, path):
        # 去除首尾的空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        isExists = os.path.exists(path)
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            print(path + ' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path + ' 目录已存在')
            return False

    def process_item(self, item, spider):
        """
        这个方法将调用上面创建的方法来创建目录，
        并将不同的动物介绍信息保存到不同的文件夹中
        写法要参考爬虫文件中存入 item 时使用的名称
        animal_item = AnimalspiderItem()
        animal_item['name'] = name
        animal_item['img_url'] = img_url
        animal_item['animal_info'] = animal_info.strip()
        """

        # 定义存放照片的文件夹名称
        animal_img_path = './animal_imgs/' + item['name']
        # 存放动物信息的 txt 文件的目录位置
        animal_txt = animal_img_path + "/" + item['name'] + '.txt'

        # 调用上面配置的方法来创建目录
        self.create_dir(animal_img_path)
        # 写入各个动物的介绍信息
        with open(animal_txt, 'wb') as f:
            f.write((item['name'] + item['animal_info'] + '\n').encode('utf-8'))
        return item


class ImagesSpiderPipeline(ImagesPipeline):
    """
    ImagesPipeline 是一个用来保存图片的管道类
    只要在爬虫文件中抛出 Item 类的实例，它就会自动将其拾取并解析内部的信息，提取其中的图片 url 并下载
    在本例子中，我们在 settings.py 中重新定义了它，将其定义为了 IMAGES_URLS_FIELD = 'img_url'
    也就是说，只有在 Item 的实例中，将需下载的图片的 url 导入 'img_url' 这个键下，管道才能正确的完成下载

    这个类内部已经定义好了一系列的方法，无需额外配置即可直接使用
    使用时直接将其继承，并在 settings.py 文件中配置即可
    但如果想要又更多定制化的操作，我们就必须将一些方法重写
    这里我们重写其中的 self.get_media_requests 和 self.file_path 两个方法
    """
    def get_media_requests(self, item, info):
        # 这个方法用来获取图片的 url，并通过 Request 方法来保存图片
        # 这里将 item 加入到 Request 的 meta 字典中，继续传入下一个方法
        # 需要注意的是，在源代码中这里返回的时一个列表，所以这里模仿源代码也使用列表
        return [Request(item['img_url'], meta={'item': item})]

    def file_path(self, request, response=None, info=None, *, item=None):
        # 先从 Request 的 meta 字典中取出图片的信息
        item = request.meta['item']
        # 根据取出的信息定义好图片保存的路径
        path = "./" + item["name"]
        img_name = item["name"]
        img_path = path + '/' + img_name + '.jpg'
        print('######将使用路径 {} 保存图片##########'.format(img_path))
        # 这个方法最终返回的是一个字符串格式的路径
        return img_path

