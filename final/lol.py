import scrapy

class TestSpider(scrapy.Spider):
		#print("ENter the Location :")
	loc = str(raw_input("Enter the location :"))
	start_urls = ['https://lawrato.com/lawyers/'+loc]

	def parse(self, response):
	        SET_SELECTOR = '.col-lg-12.padBtm.pad-lt-rt'
	        NAME_SELECTOR = 'a h3 span ::text'
                AREA_SELECTOR = 'span p span ::text'
                EXPE_SELECTOR = 'p ::text'
		file = open("data1.txt","w+")
		Name = ""
		for brickset in response.css(SET_SELECTOR):
			temp = brickset.css(NAME_SELECTOR).extract_first() 
	                print(temp)
			Name = Name + str(temp)
			Name = Name + "\n"
			#print(Name)
		    	#for line in file:
        		#        print(line)
			#	line = line.rstrip()  # remove '\n' at end of line
			#        if Name == line:
			#		continue
			#	else:
			file.write(Name)
			#Location = brickset.css(AREA_SELECTOR).extract_first()  
			#print(Location)
			#file.write(Location)
			#brickset1 = response.CSS('col-lg-7.col-xs-7.pad.lt-rt')
			#Expertise = brickset.css(EXPE_SELECTOR).extract_first()
			#print(Expertise)
			#file.write(Expertise)
			NAME_SELECTOR = 'a h3 ::text'
			#AREA_SELECTOR = 'p ::text'
			#EXPE_SELECTOR = 'p ::text' 
			#}
		file.close()
			

