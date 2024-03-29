#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib.request
import json

import websocket


def issue_access_token(client_id, client_secret):
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
    }
    headers = {
        'Content-Type': 'application/json',
    }
    req = urllib.request.Request('https://typetalk.com/oauth2/access_token', json.dumps(params).encode(), headers)
    with urllib.request.urlopen(req) as res:
        return json.load(res)['access_token']


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print('disconnected streaming server')


def on_open(ws):
    print('connected streaming server')


def main():
    if not ('TYPETALK_CLIENT_ID' in os.environ and 'TYPETALK_CLIENT_SECRET' in os.environ):
        print('TYPETALK_CLIENT_ID and TYPETALK_CLIENT_SECRET should be set in your environment variables')
        sys.exit(1)

    access_token = issue_access_token(os.environ['TYPETALK_CLIENT_ID'], os.environ['TYPETALK_CLIENT_SECRET'])
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://message.typetalk.com/api/v1/streaming",
                                header=["Authorization: Bearer %s" % access_token],
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    try:
        ws.run_forever(sslopt={"check_hostname": False})
    except KeyboardInterrupt:
        ws.close()


if __name__ == "__main__":
    main()
