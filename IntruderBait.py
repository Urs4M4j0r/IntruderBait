import socket
import sys
import threading
import paramiko
import os
from datetime import datetime

# Generate an RSA host key (2048 bits) for the SSH server
hostKey = paramiko.RSAKey.generate(2048)

# Define the SSH port to listen on
port = 2222

# Specify the file to record login attempts
loginsRecorded = 'logins.txt'

# Create a thread lock to ensure thread safety during file operations
lock = threading.Lock()


# Define a class to handle SSH server functionality using paramiko
class SSHServerHandler(paramiko.ServerInterface):
    def __init__(self, client_addr, argDict):
        # Initialize an event to signal when authentication is complete
        self.event = threading.Event()
    
        # Capture the IP address of inbound connections
        self.client_ip = client_addr[0]

        # Check if we should record the IP, timestamp, both or only username:password
        if argDict['ipAddr']:
            self.recordIP = True
        else:
            self.recordIP = False

        if argDict['timeStamp']:
            self.recordTime = True
        else:
            self.recordTime = False

        if argDict['recordDuplicates']:
            self.recordDup = True
        else:
            self.recordDup = False        

    # This method is called when a client attempts password authentication
    def check_auth_password(self, username, password):
        with lock:
            try:

                # Set log_entry according to whether the IP is desired or not
                log_entry = ''
                if self.recordIP:
                    log_entry += self.client_ip + '\n'
                if self.recordTime:
                    log_entry += str(datetime.now()) + '\n'
                    
                userPass = username + ':' + password + '\n'
                log_entry += userPass +'\n'
                    
                    
                # Print and log the new login attempt
                print(log_entry)
                
                # Open the logins file in append mode
                with open(loginsRecorded, 'r+') as loginsRecorded_handle:
                    if userPass not in loginsRecorded_handle.read():
                        loginsRecorded_handle.write(log_entry)
                    elif self.recordDup:
                        loginsRecorded_handle.write(log_entry)
            except:
                # Since this is meant to be set and forget just suppress exceptions. If you're having issues change this to print out the exception.
                pass
        # Return AUTH_FAILED to indicate authentication failure
        return paramiko.AUTH_FAILED

    # This method defines the allowed authentication methods (only password in this case)
    def get_allowed_auths(self, username):
        return 'password'

# Define a function to handle incoming SSH connections
def handleConnection(client, client_addr, argDict):
    transport = paramiko.Transport(client)
    transport.add_server_key(hostKey)
    server_handler = SSHServerHandler(client_addr, argDict)
    transport.start_server(server=server_handler)
    channel = transport.accept(1)
    if channel is not None:
        # Close the channel (session)
        channel.close()

# Define a function to run the SSH server
def runServer(argDict):
    print('Listening for SSH connections on port ' + str(port) +'\n')
    try:
        # Create a socket to listen for incoming SSH connections
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', port))
        server_socket.listen(100)

        # Redirect paramiko logs to a log file
        paramiko.util.log_to_file('paramiko.log')

        while True:
            try:
                # Accept an incoming connection and retrieve the client socket and address
                client_socket, client_addr = server_socket.accept()
                # Start a new thread to handle the connection
                threading.Thread(target=handleConnection, args=(client_socket, client_addr, argDict)).start()
            except:
                # Since this is meant to be set and forget just suppress exceptions. If you're having issues change this to print out the exception.
                pass

    except:
        # Since this is meant to be set and forget just suppress exceptions. If you're having issues change this to print out the exception.
        pass

# Entry point of the script
if __name__ == '__main__':
    # Check if the recorded logins file exists. If no, create it. This is done because it's opened with r+ so we don't write duplicates
    if not os.path.exists(loginsRecorded):
        open(loginsRecorded, 'a').close()
    argDict = {
        'ipAddr':False,
        'timeStamp':False,
        'recordDuplicates':False
        }
    # Check if arguments were passed
    numArgs = len(sys.argv)

    if numArgs > 1:
        for arg in sys.argv:
            if arg.lower() == '-p':
                argDict.update({'ipAddr':True})
            elif arg.lower() == '-t':
                argDict.update({'timeStamp':True})
            elif arg.lower() == '-d':
                argDict.update({'recordDuplicates':True})
                
    # Get argument to check for the -p switch. This indicates if you would like ip addresses recorded or not.

        
    #Run SSH server
    runServer(argDict)
