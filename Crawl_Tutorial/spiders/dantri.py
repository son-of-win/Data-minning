import scrapy


class Sendo(scrapy.Spider):
    name = 'dantri'
    start_urls = [
        'https://dantri.com.vn/suc-khoe/ca-tu-vong-thu-3-lien-quan-covid-19-tai-da-nang-20200801092828794.htm']
    count_response = 0  # biến đếm số lương bài crawl
    history = set()

    def parse(self, response):
        if response.url not in self.history:
            f = open('C:/Users/huuvuot/Desktop/scrapy/result/dantri_new.txt', 'a+', encoding="utf-8")
            self.history.add(response.url)
            title = response.css("h1.dt-news__title::text").get().strip()
            dateTime = response.css("span.dt-news__time::text").get()
            author = response.css("div.dt-news__content strong::text").get()
            tag = response.css("ul.dt-breadcrumb a::text").extract()

            # ghi dữ liệu vào file
            f.write(title + '\n')
            f.write(dateTime + '\n')
            f.write(author + '\n')
            f.write(tag + '\n')
            f.write('_' * 100 + '\n')
            self.count_response = self.count_response + 1
            
            # get next link
            next_links = self.get_next_links(response)
            if (next_links is not None) and self.count_response <= 200:
                for link in next_links:
                    #link = 'https://dantri.com.vn' + link
                    yield response.follow(link, self.parse)    # tương tự với scrapy.Request(link, callback=self.parse)

    # else: print(self.n)

    def get_next_links(self, response):   # lấy danh sách link bài viết liên quan để mở rộng thu thập
        next_links = response.css("div.dt-section__body a.news-item__avatar::attr(href)").extract()
        if len(next_links) == 0:
            return None
        else:
            return next_links

