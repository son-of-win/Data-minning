import scrapy
import json

class amazone(scrapy.Spider):
    name = 'amazone'
    start_urls = ['https://www.amazon.com/Roku-Express-Streaming-Media-Player/dp/B07WVFCVJN/ref=lp_16225007011_1_1?s=computers-intl-ship&ie=UTF8&qid=1596682424&sr=1-1']
    history = set()
    count_response = 0
    def parse(self, response):
        if response.url not in self.history and self.count_response <= 200:
            f = open('C:/Users/huuvuot/Desktop/scrapy/result/amazone.json','a+',encoding='utf-8')
            self.history.add(response.url)
            data = {
                'name_product':response.css("span[id=productTitle]::text").get().strip(),
                'rate' : response.css("span[id=acrCustomerReviewText]::text").get(),
                'customer_reply' : response.css("a[id=askATFLink] span.a-size-base::text").get().strip(),
                'price_and_ship' : response.css("span[id=priceblock_ourprice]::text").get() + response.css("span.a-size-base.a-color-base b::text").get(),
                'description' : response.css("ul.a-unordered-list.a-vertical.a-spacing-mini span.a-list-item::text").extract()
            }

            #ghi du lieu vao file
            json.dump(data,f,ensure_ascii=False)
            f.write('\n')
            self.count_response = self.count_response + 1

            #get next links
            next_links = self.get_next_links(response)
            if next_links is not None:
                for link in next_links:
                    yield response.follow(link , callback= self.parse)

    def get_next_links(self,response):
        next_links = response.css("div.a-section.a-spacing-none.p13n-asin >  a.a-link-normal::attr(href)").extract()

        if len(next_links) == 0:
            return  None
        else: return next_links





