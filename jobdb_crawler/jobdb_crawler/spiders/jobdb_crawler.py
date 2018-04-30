#-*- coding: utf-8 -*-
import scrapy


class JobDBSpider(scrapy.Spider):
    name = "jobdb"
    start_urls = [
        'https://m.jobsdb.co.th/en-th/jobad/public-relations-campaign-300003001614256?pageIdx=1601&jobAdOffset=8&searchResultUrl=search.do%3FSalaryT%3D2147483647%26careerLevelFromId%3D0%26pageNumber%3D1602%26SalaryFText%3D%26SalaryTText%3D%26careerLevelToId%3D0%26jobAdOffset%3D6%26employmentTermId%3D0%26industryId%3D0%26submitForm%3Dtrue%26moreOption%3Dfalse%26locationId%3D0%26SalaryType%3D1%26pager.offset%3D16010%26jobFunctionId%3D0%26SalaryF%3D0%26keyword%3D&moreOption=false&jobFunctionId=0&industryId=0&careerLevelFromId=0&careerLevelToId=0&locationId=0&employmentTermId=0&method=add&SalaryType=1&SalaryT=2147483647&SalaryF=0&Career=&JobCat=&JobTypes=&Locations=&EM_Locations=&JobInd=&SearchFields=&AD=',
    ]

    def parse(self, response):
        titles = response.xpath('string(//title/text())').extract()
        organization = response.xpath('string(//*[@itemprop="hiringOrganization"])').extract()
        joblocation = response.xpath('string(//*[@itemprop="jobLocation"])').extract()                
        experience = response.xpath('string(//*[@itemprop="experienceRequirements"])').extract()
        education = response.xpath('string(//*[@itemprop="educationRequirements"])').extract()      
        industry = response.xpath('string(//*[@itemprop="industry"])').extract()
        employmentType = response.xpath('string(//*[@itemprop="employmentType"])').extract()
        jobfunction = response.xpath('normalize-space(//td[@class="jobDd"])').extract() 
        salary = response.xpath('string(//*[@itemprop="baseSalary"])').extract()
        level = response.xpath('string(//table//td[last()]/text())').extract()
        jobdes = response.xpath('string(//*[@id="jobs_content"]/div[1])').extract()
        comde = response.xpath('string(//*[@id="jobs_company"]/div)').extract()

        #Give the extracted content row wise
        for item in zip(titles,organization,joblocation,experience,education,industry,employmentType,jobfunction,salary,level,jobdes,comde):
        #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'organization' : item[1],
                'joblocation' : item[2],                
                'experience' : item[3],
                'education' : item[4],                
                'industry' : item[5],
                'employmentType' : item[6],
                'jobfunction' : item[7],
		        'salary' : item[8],
                'level' : item[9],
                'jobdescription' : item[10],
                'companydetail' : item[11]                               
            }         
                    
            yield scraped_info
        
        next_page = response.xpath('//*[@id="sticky-top"]/div/a[2]/@href').extract_first()
        if next_page is not None:
           yield response.follow(next_page, callback=self.parse)