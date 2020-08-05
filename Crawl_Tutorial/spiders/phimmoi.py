import scrapy
import json

class vnexpress(scrapy.Spider):
    name = 'phimmoi'
    start_urls = ['http://www.phimmoizz.net/phim/mat-troi-chim-day-bien-2020-11193/']
    history = set()
    count_response= 0
    def parse(self,response):
        if (response.url not in self.history) and self.count_response <= 200:
            f = open('C:/Users/huuvuot/Desktop/scrapy/result/phimmoi.json','a+',encoding='utf-8')

            self.history.add(response.url)
            key = response.css("dt.movie-dt::text").extract()
            value = response.css("dd.movie-dd::text").extract()
            description = {x:y for x,y in zip(key, value)}


            data = {
                'tag': response.css("span[itemprop='name']::text").extract(),
                'name_film': response.css("a.title-1::text").get(),
                'description': description,
                'tomtat': response.css("div[id=film-content] p::text").get(),
                'keyword': response.css("ul.tag-list a.tag-link::text").extract(),
                'link_film': response.css("a[id='btn-film-watch']::attr(href)").get()
            }


            json.dump(data,f,ensure_ascii=False)
            f.write('\n')
            self.count_response = self.count_response + 1

            #get next links
            next_links = self.get_next_link(response)
            for link in next_links:
                yield response.follow(link,callback=self.parse)


    def get_next_link(self, response):
        next_links = response.css("li.movie-item a.block-wrapper::attr(href)").extract()
        if(len(next_links) == 0):
            return None
        else:
            return next_links

                

