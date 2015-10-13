import scrapy

class FormSpider(scrapy.Spider):
    name = "form"

    start_urls = [
            "http://192.168.56.102/mutillidae/index.php?page=add-to-your-blog.php",
            "http://192/168/56/102/mutillidae/index.php?page=view-someones-blog.php"
            ]

    def parse(self, response):
        print(response)
