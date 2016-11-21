# -*- coding: utf-8 -*-

BOT_NAME = 'workua'

SPIDER_MODULES = ['workua.spiders']
NEWSPIDER_MODULE = 'workua.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'workua.pipelines.WorkuaPipeline': 300,
}

LOG_FILE = 'workua.log'
