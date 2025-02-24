from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import sys

def main():
    port = 4443
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(
        certfile="./cert.pem", 
        keyfile="./key.pem")
    context.check_hostname = False

    with HTTPServer(("localhost", port), SimpleHTTPRequestHandler) as httpd:
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        print("Listening on port: {}".format(port))
        httpd.serve_forever()

if __name__ == "__main__":
    main()