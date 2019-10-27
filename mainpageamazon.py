import scrapy
import time
import random

pagenum = 20 #CHANGE THE PAGE NUMBER HERE FOR EASE OF ACCESS

class AmazonAttempt(scrapy.Spider):
	name = "MainPageAmazon"
	start_urls = ["https://www.amazon.com/s?k=headphones&page=" + str(pagenum)]

	def parse(self, response):
		productranking = 294 #plug-in the start product number wanted here
		for item in response.css("div.sg-col-20-of-24.s-result-item.sg-col-0-of-12.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-12-of-16.sg-col-24-of-28"): #for each product
			checkad = item.css("div.a-section.a-spacing-none.a-spacing-top-small div.a-row.a-spacing-micro span.a-size-base.a-color-secondary::text").extract_first() #supposed to check if product is sponsered, does not work!
			name = item.css("a.a-link-normal.a-text-normal span.a-size-medium.a-color-base.a-text-normal::text").extract_first() #name of product
			rating = item.css("div.a-section.a-spacing-none.a-spacing-top-micro div.a-row.a-size-small span::attr(aria-label)").extract_first() #rating of product, does NOT get distribution of ratings.
			numratings = item.css("div.a-row.a-size-small span a.a-link-normal span.a-size-base::text").extract_first() #number of reviews
			price = item.css("a.a-size-base.a-link-normal.s-no-hover.a-text-normal span.a-price span.a-offscreen::text").extract_first()

			distributionofratings = []
			for distribution in item.css("table.a-normal.a-align-middle.a-spacing-base tbody tr.a-histogram-row"):
				distributionofratings.append(distribution.css("td.a-nowrap span.a-size-small a.a-link-normal::text").extract_first())

			if item.css("span.aok-inline-block.s-image-logo-view span.aok-relative.s-icon-text-medium.s-prime i::attr(aria-label)").extract_first() == None: #checks for if product is prime
				prime = 0
			else:
				prime = 1

			if item.css("span.a-badge-label span.a-badge-label-inner.a-text-ellipsis span.a-badge-text::text").extract_first() == "Best Seller": #checks if product is best seller
				bestseller = 1
			else:
				bestseller = 0

			if item.css("span.a-badge-label span.a-badge-label-inner.a-text-ellipsis span.a-badge-text::text").extract_first() == "Amazon's ": #checks if product is Amazon Choice
				amazonchoice = 1
			else:
				amazonchoice = 0

			if price != None and name != None:
				yield {
					"page":pagenum,
					"productranking":productranking,
					"price":price,
					"name":name,
					"rating":rating,
					"numofratings":numratings,
					#"distributionofratings":distributionofratings,
					"prime":prime,
					"bestseller":bestseller,
					"amazonchoice":amazonchoice
				}
				productranking = productranking + 1

			#this is here to let the bot run on a page and stop the bot for a certain time before continuing onto the next page
			"""next = response.css("div.a-text-center ul.a-pagination li.a-last a::attr(href)").extract_first()
			if next:
				time.sleep(random.randint(4,10))
				yield response.follow(next, self.parse)"""






		
       