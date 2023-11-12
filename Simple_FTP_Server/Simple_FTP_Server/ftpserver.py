import http.server
import socketserver
import os
import threading

USERNAME = "pooja"
PASSWORD = "pooja"
PATH = r"C:\Users\pooja\Pooja_FTP_Server_Folder"
SCRIPT_PATH = r"C:\Users\pooja\Simple_FTP_Server\Simple_FTP_Server"
ANONYMOUS_PATH = os.path.join(SCRIPT_PATH, "Error")

f = open("logs.txt", "a")

uname = ""
passwd = ""


def initvars():
    global uname
    global passwd
    uname = ""
    passwd = ""


print(f"PATH : {PATH}")


class GetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("printing request : ", self.path)
        st = str(self.path)
        f.write(st + "\n")
        authorize(st, PATH, ANONYMOUS_PATH)
        http.server.SimpleHTTPRequestHandler.do_GET(self)


def authorize(st, PATH, ANONYMOUS_PATH):
    li = list(st)
    global uname
    global passwd

    print("uname is ", uname)
    print("passwd is ", passwd)
    if uname == USERNAME and passwd == PASSWORD:
        ind1 = li.index("/")
        add_path = st[ind1:]
        new_path = os.path.join(PATH, add_path)
        print("Providing access to : ", new_path)

    else:
        if "username=" in st and "passwd=" in st:
            ind1 = li.index("=")
            ind2 = li.index("&")
            uname = st[ind1 + 1:ind2]
            print("Received username : ", uname)

            li = [li[i] for i in range(ind2, len(st))]
            ind1 = li.index("=")
            for i in range(ind1 + 1, len(li)):
                passwd = passwd + li[i]

            print("Received password : ", passwd)

            if uname == USERNAME and passwd == PASSWORD:
                os.chdir(PATH)
            else:
                os.chdir(ANONYMOUS_PATH)
        else:
            print("Access prohibited")
            os.chdir(SCRIPT_PATH)


def StartServer():
    print("Server is up")
    host = "127.0.0.1"
    port = 1515
    handler = GetHandler
    os.chdir(SCRIPT_PATH)

    http_server = socketserver.TCPServer((host, port), handler)

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("Server is shutting down")
        http_server.shutdown()
        http_server.server_close()
        print("Server has stopped")


print("Server starting")
initvars()

if __name__ == '__main__':
    cthread = threading.Thread(target=StartServer)
    cthread.daemon = True
    cthread.start()

try:
    cthread.join()
except KeyboardInterrupt:
    print("Main thread received KeyboardInterrupt. Exiting.")
