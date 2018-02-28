import socket
from flask import Flask
from datetime import datetime 

application = Flask(__name__)

@application.route("/")

def hello():
    #open the log file
    with open("/mnt/log", "w") as log: #append mode
        log.write(str(datatime.now()) + ":" + socket.gethostname() + "\n<br>") #write a line
    
    #read the log history
    log_file = open("/mnt/log","r")
    log_history = log_file.read()
    log_file.close()   
    txt = "<html><title>CEC</title><body>"+log_history"</body></html>"
    return txt

if __name__ == "__main__":
    application.run()
