# response = '''HTTP/1.1 {status}
# Connection: Close
#
# {html}
# '''
#
# context = {}
#
# context['status'] = 200
# context['html'] = '<html></html>'
#
# response.format(**context)

LISTING = '<a href="{file}">{file}<a/><br>'

import SocketServer
import re
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

ROOT = 'C:\\'

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("hello !")

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        #print "{} wrote:".format(self.client_address[0])
        #print self.data
        path = re.findall('^GET (.*) HTTP\/1\.1$', self.data.splitlines()[0])[0]
        target = os.path.join(ROOT, *path.split('/'))
        print path.split('/')
        if os.path.exists(target):
            # TODO: check if target is directory return list of files
            print target
            if os.path.isdir(target):
                content = '\n'.join([LISTING.format(file=f) for f in os.listdir(target)])
                #result = []
                #for f in os.listdir(target):
                #    result.append.LISTING.format(file=f)
            else:
                content = open(target).read()
            content = """HTTP/1.1 200
Content-Type: text/html

""" + content
            #print '----'
            #print content
            #print '----'
            self.request.sendall(content)
        else:
            self.request.sendall('404 not found')

if __name__ == "__main__":
    HOST, PORT = "localhost", 8000

# Create the server, binding to localhost on port 9999

# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
print 'listening on ', HOST, ':', PORT

server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
# serv = HTTPServer((HOST, PORT), HttpProcessor)
server.serve_forever()