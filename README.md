# 链家爬虫

基于Scrapy框架开发，爬取链家上海新房所有楼盘信息
http://sh.fang.lianjia.com/

运行main.py即可运行，爬取结束会生成overview.json和detail.json两个文件，文件的每一行为一个json.
其中:
overview.json中每个json表示一个楼盘概况，示例链接 http://sh.fang.lianjia.com/loupan/pg1/
detail.json中每个json表示一个楼盘详细信息，示例链接 http://sh.fang.lianjia.com/detail/lujinsheshanyuanzi/