#reciever


import socket
import time

# number of functions in socket module / library
# print(dir(socket))

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #tcp protocol will be used by default if nothing is mentioned in bracket


my_ip = "127.0.0.1"
my_port = 9999
my_address = (my_ip,my_port)
# lets create a connection string 
s.bind(my_address)

# socket --- IP:PORT   -- 52.2.116.225:9999
# facebook ---            www.facebook.com:443
# --                      157.240.239.35:443
#port -- 0-65535
#lets recv text data
# s.recvfrom()

data = s.recvfrom(100)
#only filtering message

new_data = data[0]
final_message = new_data.decode('ascii')

print(final_message)
time.sleep(2)