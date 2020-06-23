import requests
r = requests.get('https://103.235.224.104/admin/')
print(r.status_code)
print(r)

# requests.exceptions.SSLError: HTTPSConnectionPool(host='103.235.224.104', port=443): Max retries exceeded with url: /admin/ (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate 
# verify failed')])")))