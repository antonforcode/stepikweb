def app(environ, start_response):
    env_data = environ["QUERY_STRING"]
    data = env_data.replace("&", "\n")
    data = bytes(data, encoding = 'ascii')
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return data
