import socket
from flask import Flask
from datetime import datetime 

application = Flask(__name__)

@application.route("/")

def hello():
    #open the log file
    with open("/mnt/log", "w") as log: #append mode
        log.write(str(datatime.now()) + ":" + socket.gethostname() + "\n") #write a line
    
    #read the log history
    log = open("/mnt/log","r")
    log_history = log.read()
    log.close()   
    
    return ""+log_history


if __name__ == "__main__":
    application.run()
