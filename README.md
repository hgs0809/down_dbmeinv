# down_dbmeinv
执行抓取  scrapy crawl pic

需要安装python的pymongo                        pip install pymongo

在settings.py里面设置了
USER_AGENT 浏览器user_agent

DOWNLOAD_DELAY   每次延长多少秒执行下一次操作

MONGO_URI='/tmp/mongodb-27017.sock'              //mongo的sock路径

MONGO_DATABASE='local'              //库名

ITEM_PIPELINES  //启用item_pipelines
