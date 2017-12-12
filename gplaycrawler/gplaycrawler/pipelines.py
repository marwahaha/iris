# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


##class GplaycrawlerPipeline(object):
##    def process_item(self, item, spider):
##        return item 
#from scrapy.contrib.pipeline.images import ImagesPipeline  
import json
import logging
import sys
import time  


from twisted.enterprise import adbapi  
from scrapy.http import Request  
from scrapy.exceptions import DropItem 
import pika
import psycopg2 

from settings import rabbitmq_server_host, rabbitmq_queue
from queries import get_conn, get_cursor

  
  
class GplayPipeline(object):  
  
    def __init__(self):  
        tries=0
        max_cn_tries=5
        self.conn = None
        self.rabbit_mq_connection = None
        self.channel = None
        while tries<max_cn_tries:
            logging.info('Attempt {}/{} to connect to PostgreSQL at {}'.format(tries+1,max_cn_tries,db_config['host']))
            try:
                self.conn = get_conn()
                break
            except psycopg2.OperationalError as e:
                tries+=1
                if tries == max_cn_tries:
                    logging.exception(e)
                    logging.error('could not connect to PostgreSQL for some reason..check settings.py')
                    sys.exit()
                time.sleep(1)

        tries=0
        max_cn_tries=10
        while tries<max_cn_tries:
            logging.info('Attempt {}/{} to connect to RabbitMQ at {}'.format(tries+1,max_cn_tries,rabbitmq_server_host))
            try:
                self.rabbit_mq_connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_server_host))
                self.channel = self.rabbit_mq_connection.channel()
                self.channel.queue_declare(rabbitmq_queue)
                break
            except Exception as e:
                tries+=1
                if tries == max_cn_tries:
                    logging.exception(e)
                    logging.error('could not create connection to {} or declare queue {}'.format(rabbitmq_server_host, rabbitmq_queue))
                    sys.exit()
                time.sleep(1)

    def process_item(self, item, spider):
        """ 
        Put new items on the DB and publish to the rabbitmq for downloading
        """
        if str(item['Link']).find('details?id') != - 1:
            cur = get_cursor(self.conn)

            tries=0
            max_tries=3
            while tries<max_tries:
                try:
                    insert_app(item, commit=False)
                    duplicate = False

                    #push to queue
                    serializable_item = dict(item)
                    self.channel.publish(exchange='',
                                         routing_key=rabbitmq_queue,
                                         body=json.dumps(serializable_item),
                                         properties=pika.BasicProperties(content_type='application/json',delivery_mode=2))#2 = write to disk
                    self.conn.commit()
                    break
                except psycopg2.IntegrityError as e:
                    #duplicate
                    self.conn.rollback()
                    spider.logger.exception(e)
                    break
                except Exception as e:
                    spider.logger.exception(e)
                    tries+=1
                    time.sleep(1)

        return item
