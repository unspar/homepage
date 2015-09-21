#! /usr/bin/python3

import sys
import http.server as sv


class MyHandeler(sv.BaseHTTPRequestHandler):
	def do_GET(s):
		'''this responds to a get request'''
		
		s.send_response(200)
		s.send_header('Content-type', "text/html")
		s.end_headers()
		s.wfile.write(b"<html><head><title>Title goes here.</title></head>")
		s.wfile.write(b"<body><p>This page is dynamically generated</p>")
		s.wfile.write(b"</body></html>")


def run(server_class=sv.HTTPServer, handler_class=MyHandeler):
	server_address = ('', 8000)
	httpd = server_class(server_address, handler_class)
	httpd.serve_forever()



run()


