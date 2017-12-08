def app(environ, start_response):
    env_data = environ.get("QUERY_STRING", "")
    data = env_data.replace("&", "\n")
    data = data.encode()
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return iter([data])
