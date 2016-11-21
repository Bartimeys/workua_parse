import taskflow.engines
from scrapy import signals
from scrapy.crawler import Crawler, CrawlerProcess
from scrapy.utils.project import get_project_settings
from taskflow import task
from taskflow.patterns import linear_flow

from workua.spiders.workua_spider import WorkuaSpider


class RunTask(task.Task):
    def __init__(self):
        super(RunTask, self).__init__()
        self.spider = Crawler(WorkuaSpider, get_project_settings())

    def execute(self, *args, **kwargs):
        self.from_crawler(self.spider)
        self.process = CrawlerProcess(get_project_settings())
        self.process.crawl(self.spider)
        self.process.start()

    def revert(self, *args, **kwargs):
        self.process.stop()

    def from_crawler(self, spider):
        spider.signals.connect(self.spider_opened, signal=signals.spider_opened)
        spider.signals.connect(self.spider_idle, signal=signals.spider_idle)

    def spider_opened(self):
        print('Started crwaling...')

    def spider_idle(self):
        print('Finished crawling')


def main():
    flow = linear_flow.Flow('workua').add(RunTask())
    engine = taskflow.engines.load(flow)
    try:
        engine.run()
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
