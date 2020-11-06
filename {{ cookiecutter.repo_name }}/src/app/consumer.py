# -*- coding: utf-8 -*-

import time
from predictor import Predictor

class Consumer(object):

    def __init__(self):
        self.predictor = Predictor()
        pass

    def loadMessages(self):
        pass

    def processMessages(self):
        pass

    def sendOutputMessages(self):
        pass


def run(consum):
    input_messages = consum.loadMessages()
    output_messages = consum.processMessages(input_messages)
    status = consum.sendOutputMessages(output_messages)
    return status


if __name__ == '__main__':
    consumer = Consumer()
    while True:
        status = run(consumer)
        time.sleep(2)
