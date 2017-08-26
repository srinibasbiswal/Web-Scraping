# exection: scrapy runspider test.py
import scrapy
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://testing-ground.scraping.pro/login")
username = driver.find_element_by_name("usr")
password = driver.find_element_by_name("pwd")

username.send_keys("admin")
password.send_keys("12345")

driver.find_element_by_css_selector("input[value = 'Login']").click()

class LoginSpider(scrapy.Spider):
    name = 'login-codex'
    loginurl = "http://testing-ground.scraping.pro/login"
    start_urls = [loginurl]

    def parse(self, response):        
        data = {
            'username' : 'admin',
            'password' : '12345',
        }
        yield scrapy.FormRequest(url=self.loginurl, formdata = data, callback=self.parse_data)
        

    def parse_data(self, response):
        for data in response.css('div#caseinfo'):
            yield{
                'Extracted data': data.css('div#caseinfo').extract_first()
            }


        