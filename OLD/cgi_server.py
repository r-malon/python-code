'''from http.server import *
address = ('127.0.0.1', 8081)
send_response(200)
send_header('Content-Type', 'text/html\n\n')
end_headers()
msg='<h1>Ola jose!</h1><br><p>Como vai?</p>'
wfile.write(msg, 'utf-8')
s=HTTPServer(address)
s.serve_forever()'''

from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "<h1>Hello jailson!</h1>"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
  print('starting server...')
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
