######## Backup File ########
import getpass
import telnetlib

user = raw_input("Enter your username:")
password = getpass.getpass()

HOST = ("192.168.30.142","192.168.30.140","192.168.30.141")

for i in HOST:
    print ("\n\nconnecting to " + i)
    tn = telnetlib.Telnet(i, timeout = 15)
    if i is "192.168.30.142":
        tn.read_until("login:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("sh configuration | display set\n")
        tn.write("exit\n")
       
    elif i is "192.168.30.140":
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("terminal length 0\n")
        tn.write("show runn\n")
        tn.write("exit\n")
            
    elif i is "192.168.30.141":
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("en\n")
        tn.write("terminal length 0\n")
        tn.write("show running\n\n")
        tn.write("exit\n\n")
        #print tn.read_all()
    readall = tn.read_all()
    File = open("File "+ str(i), "w")
    File.write(readall)
    File.write("\n")
    File.close()
    print("Backup of "+i+" completed")
    
