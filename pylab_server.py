#!/usr/bin/env python2.7

import SocketServer
import visa
import json

class InstrumentRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        command = self.rfile.readline().strip()
        if command == 'list':
            self.wfile.write(json.dumps(self.list_instruments())+'\r\n')

    def list_instruments(self):
        rm = visa.ResourceManager()
        return rm.list_resources()

if __name__ == '__main__':
    HOST, PORT = "localhost", 9090

    server = SocketServer.TCPServer((HOST, PORT), InstrumentRequestHandler)

    server.serve_forever()
