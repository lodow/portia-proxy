SPIDER_MANAGER_CLASS = 'slybot.spidermanager.SlybotSpiderManager'
EXTENSIONS = {'slybot.closespider.SlybotCloseSpider': 1}
ITEM_PIPELINES = {'slybot.dupefilter.DupeFilterPipeline': 1}
SPIDER_MIDDLEWARES = {'slybot.spiderlets.SpiderletsMiddleware': 999} # as close as possible to spider output
SLYDUPEFILTER_ENABLED = True
PROJECT_DIR = 'slybot-project'
FEED_EXPORTERS = {
    'csv': 'slybot.exporter.SlybotCSVItemExporter',
}
CSV_EXPORT_FIELDS = None
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 5,
}

try:
    from local_slybot_settings import *
except ImportError:
    pass
