from wsgiref.simple_server import make_server

def web_app(environment, response):
    status = '200 ok'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    response(status, headers)

    return [b'Hello World']

with make_server('', 8000, web_app) as server:
    print('\nServer Successfully Started\n\nRunning On Port                8000\nRunning In WebBrowser At       http://127.0.0.1:8000/')
    server.serve_forever()