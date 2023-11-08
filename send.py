#sender

import socket

# number of functions in socket module / library
# print(dir(socket))

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #tcp protocol will be used by default if nothing is mentioned in bracket
                    #ip address   # protocol
# finally s can create UDP socket
#target system address
target_ip = "127.0.0.1"
target_port = 9999
final_target = (target_ip,target_port)
#taking input from user
msg = input("Please enter your message : ")
# since python3 is supporting minimum encoding
new_msg = msg.encode('ascii')

#sending data

s.sendto(new_msg,final_target)

