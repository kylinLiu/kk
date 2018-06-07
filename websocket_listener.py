# coding: utf-8
"""
# @Time    : 2018/6/6 15:15
# @Author  : Kylin
# @File    : main.py
# @Software: PyCharm
# @Descript:
"""

import websocket
import json
import sys

try:
    import thread
except ImportError:
    import _thread as thread
import time
import zlib


def on_message(ws, message):
    print "message"
    # decompress = zlib.decompressobj()
    # ss = decompress.decompress(message)
    print(message)
    # ws.close()
    # sys.exit()


def on_error(ws, error):
    print "error"
    print(error)


def on_close(ws):
    print "on_close"
    print("### closed ###")


def on_open(ws):
    def run(*args):
        message_list = [
            # {"event": 'login', "parameters": {
            #     "token": 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI0YTczOTgxMy0zNTJjLTQyMDEtOWU1OC1kMjI3ZWY2NTUyZTdVb3pEIiwidWlkIjoiMHRNVjVXc2NDRzBHMTE0eVZEOUpLUT09Iiwic3ViIjoiMTU4KioqNTA1MSIsImVtbCI6IjI0NzY1MTMwNUBxcS5jb20iLCJzdGEiOjAsIm1pZCI6MCwiaWF0IjoxNTI4MjUxODk2LCJleHAiOjE1Mjg4NTY2OTYsImlzcyI6Im9rY29pbiJ9.tWyYCdPCKeuHL15tfsFF3NPc7S5KTCPOMRX87TcdMhcUpR522KFnxD4QDq98vTdv30KGl1AhEvX-CYO8zIQ1CQ',
            #     "binary": "0"}},
            # {"event": 'addChannel',
            #  "parameters": {"base": "f_usd_eth", "binary": "0", "contract": "this_week", "product": "futures",
            #                 "quote": "usd", "type": "ticker"}},
            # 获取分钟线(现货)
            {"event": 'addChannel',
             "parameters": {"base": "f_usd_eth", "binary": "0", "period": "1min", "product": "futures", "quote": "usd",
                            "type": "kline"}}
        ]
        # message =
        for message in message_list:
            value = json.dumps(message)
            # time.sleep(1)
            ws.send(value)
        while True:
            ping_data = json.dumps({'event': 'ping'})
            ws.send(ping_data)
            time.sleep(5)

        # ws.close()
        print("thread terminating...")

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://okexcomreal.bafang.com:10441/websocket",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
