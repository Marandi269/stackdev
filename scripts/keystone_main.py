import sys
import wsgiref.simple_server as wss

from keystone.server.wsgi import initialize_public_application

if __name__ == "__main__":
    print("hello")
    print(sys.path)
    server = wss.make_server('0.0.0.0', 5001, initialize_public_application())
    print("*" * 80)
    print("STARTING test server keystone.server.wsgi.initialize_public_application")
    url = "http://%s:%d/" % (server.server_name, server.server_port)
    print("Available at %s" % url)
    print("DANGER! For testing only, do not use in production")
    print("*" * 80)
    sys.stdout.flush()

    server.serve_forever()
