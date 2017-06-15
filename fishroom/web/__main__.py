#!/usr/bin/env python3
import tornado.ioloop
import tornado.web
from .handlers import (
    DefaultHandler, TextStoreHandler, ChatLogHandler, MessageStreamHandler,
    PostMessageHandler, APILongPollingHandler, APIPostMessageHandler,
    RobotsTxtHandler
)
from ..config import config


def main():
    debug = config.get("debug", False)
    application = tornado.web.Application([
        (r"/", DefaultHandler),
        (r"/robots.txt", RobotsTxtHandler),
        (r"/log/([a-zA-Z0-9_-]+)/([a-zA-Z0-9-]+)", ChatLogHandler),
        (r"/log/([a-zA-Z0-9_-]+)/([a-zA-Z0-9-]+)/([0-9]+)", TextStoreHandler),
        (r"/messages/([a-zA-Z0-9_-]+)/", PostMessageHandler),
        (r"/msg_stream", MessageStreamHandler),
        (r"/api/messages", APILongPollingHandler),
        (r"/api/messages/([a-zA-Z0-9_-]+)/", APIPostMessageHandler),
    ], debug=debug, autoreload=debug)
    application.listen(config['chatlog']['port'],address=config['chatlog']['host'])
    print("Serving on",config['chatlog']['host'],":",format(config['chatlog']['port']))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

# vim: ts=4 sw=4 sts=4 expandtab
