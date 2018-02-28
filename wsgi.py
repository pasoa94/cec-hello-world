import socket
from flask import Flask
from datetime import datetime 

application = Flask(__name__)

@application.route("/")

def hello():
    #open the log file
    #with open("/mnt/log", "w") as log: #append mode
    #    log.write(str(datatime.now()) + ":" + socket.gethostname() + "\n<br>") #write a line
    
    #read the log history
    #log_file = open("/mnt/log","r")
    #log_history = log_file.read()
    #log_file.close()  
    
    #txt = "<html><title>CEC</title><body>"+log_history+"</body></html>"
    
    with open("/mnt/logfile", "a") as file:
        file.write(str(datetime.now()) +": " + socket.gethostname() + "<br>\n") 
    
    #open logfile and return its contents
    fr = open("/mnt/logfile","r")
    log = fr.read()
    fr.close()
    txt = "<html><title> Jarvis Logfile </title><body>" + log + "</body></html>"
    
    return txt

if __name__ == "__main__":
    application.run()
