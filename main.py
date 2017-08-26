import scrapy

class LoginSpider(scrapy.Spider):
    name = 'login-codex'
    loginurl = "http://quotes.toscrape.com/login"
    start_urls = [loginurl]

    def parse(self, response):
        tok= response.css('input[name="csrf_token"]::attr(value)').extract_first()
        data = {
            'csrf_token' : tok,
            'username' : 'abc',
            'password' : 'abc',
        }
        yield scrapy.FormRequest(url=self.loginurl, formdata = data, callback=self.parse_quotes)
        

    def parse_quotes(self, response):
        for q in response.css('div.quote'):
            yield{
                'author_name':q.css('small.author::text').extract_first(),
                'author_url':q.css(
                    'small_author ~ a[href*="goodreads.com"]::attr(href)'
                ).extract_first()
            }


        