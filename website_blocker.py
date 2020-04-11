import time
from datetime import datetime as dt

hosts_temp = r"filepath_to_copy_of_hosts_file_for_testing"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# Here 'r' stands for raw string so that python dont take \W, \n, \t as special character
# To write in hosts_path one has to open cmd as administrator

redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working Hours....")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun hours....")
        with open(hosts_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() # This delete the content of the file from current point to downwards
    time.sleep(5)
