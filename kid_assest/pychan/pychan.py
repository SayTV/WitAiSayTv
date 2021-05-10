import socket
import os
from urllib.parse import unquote
def check_correct_route(first_part,action):
    return first_part.lower().find(action.lower()) !=-1

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999
channel_file='channel_full.json'
# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    response_content=""
    #print(request)
    reqData=request.splitlines()
    ct=0
    check_route=""
    #for req_line in reqData:
        #print(ct,req_line)
        #ct=ct+1
    route=reqData[0]
    msg_data=[]
    route_parts=route.split(' ')
    #print('rel url is: ', route_parts[1])
    retCode="200"
    try:
        route_info=route_parts[1].split('/')
        route=route_info[1]
        route_info.remove('')
        route_info.remove(route)
        msg_data=route_info
    except:
        route="/"
        msg_data=[]    
    if check_correct_route(route,'listen'):
        #print('rount found is :',route)
        # Send HTTP response
        has_message=""
        message="\"\""
        if os.path.isfile(channel_file):
            try:
                file = open(channel_file,mode='r')
                # read all lines at once
                message = file.read()
                
                # close the file
                file.close()
                os.remove(channel_file)
                has_message= ("true")
            except:    
                print('error happen')
                has_message= ("true")
        else:
            has_message=("false")
        
        
      
        response_content='{"hasMessage":'+has_message+',"message":'+message+' }'    
    elif check_correct_route(route,'tell'):
        with open(channel_file, 'w') as f:
            msg_body="\n".join(msg_data)
            f.write('{"content":'+unquote(msg_body)+'}')
        response_content='{"result":"OK"}'
    else:
        response_content='{"error":"endpoint was not found"}'

    response = 'HTTP/1.0 '+retCode+' OK\nAccess-Control-Allow-Origin: *\n\n'+response_content
   
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()