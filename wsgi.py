import socket
from flask import Flask
from datetime import datetime 

application = Flask(__name__)

@application.route("/")

def hello():
    #read the log file and update it with the new log
    with open("/mnt/log_history", "a") as f:
        f.write(str(datetime.now()) +"   --->   " + socket.gethostname() + "<br>\n") 
    
    #open the log file for printing it in the body of the application
    f = open("/mnt/log_history","r")
    foo = f.read()
    f.close()
    
    return "<html><title>Song3</title><body>" + foo + "</body></html>"
    

if __name__ == "__main__":
    application.run()
