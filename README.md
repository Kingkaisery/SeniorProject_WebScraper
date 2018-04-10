# Project Title

This scraper is part of my senior project. This code is for scrap data about job from thai job website. 

## Getting Started

### Prerequisites

Executing this scraper requires Python 2.7 along with the scrapy 1.5

## Running 

you need to go to spider of each scraper such as ./SeniorProject_WebScraper/jobdb_crawler/jobdb_crawler/spiders/
and run this command

```
scrapy call [spider-name] -o output.csv
```
example

```
scrapy call [jobdb] -o jobdb_data.csv
```

More information please read [scrapy](https://scrapy.org/)
