import scrapy
import csv
from django.utils.encoding import smart_str
all_tweets = dict()  #dictionary to store tweets in
f = csv.writer(open('tweets.csv', 'w'))

class Basic(scrapy.Spider):    #create a class for our webcrawling spider
    name = 'Twitter'            #Name of spider
    start_urls = ['https://twitter.com/realDonaldTrump']        #website to crawl

    def parse(self, response):
        OVERALL_TWEET = '.content'
        CLASS_SELECTOR = '.js-tweet-text-container'
        TEXT_SELECTOR = 'p ::text'
        DATE_CLASS = '.time'
        DATE_SELECTOR = 'a ::text'
        for item in response.css(OVERALL_TWEET):
            name = smart_str(item.css(CLASS_SELECTOR).css(TEXT_SELECTOR).extract_first())
            date = smart_str(item.css(DATE_CLASS).css(DATE_SELECTOR).extract_first())
            f.writerow([date, name])
            if item.css(TEXT_SELECTOR).extract_first() not in all_tweets:
                all_tweets[item.css(TEXT_SELECTOR).extract_first()] = 1
                #run analysis code for that tweet in relation to the stock market
            yield {
                'Name': name,
                'Date': date,
            }



