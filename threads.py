from threading import *
import time

import redis
from tenacity import *
import wx

EVT_REDIS_CONN_ID = wx.NewId()

def EVT_REDIS_CONN(win, func):
    win.Connect(-1, -1, EVT_REDIS_CONN_ID, func)

class RedisConnectEvent(wx.PyEvent):
    def __init__(self, connection):
        super().__init__()
        self.SetEventType(EVT_REDIS_CONN_ID)
        self.connection = connection

class RedisConnectThread(Thread):
    def __init__(self, config, notify):
        super().__init__()
        self.notify = notify

        self.conn = redis.Redis(
            host=config['host'],
            port=config['port'],
            db=config['database']
        )

        self.start()

    @retry(wait=wait_fixed(2))
    def run(self):
        # Attempt to establish the connection.
        self.conn.ping()
        # Post an event to notify that the connection was successful.
        wx.PostEvent(self.notify, RedisConnectEvent(self.conn))