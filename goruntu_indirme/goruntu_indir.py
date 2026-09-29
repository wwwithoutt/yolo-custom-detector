from icrawler.builtin import BingImageCrawler
bing_crawler = BingImageCrawler(storage={'root_dir': 'indirilen_gorseller'})

bing_crawler.crawl(
    keyword="spacex falcon 9",
    max_num=70, 
    filters=
    {
          'size': 'large', 
          'type': 'photo',
    }
)