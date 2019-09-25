import time
from datetime import datetime as dt
import platform

# Dynamically allotting host_file_path according to the Operating System
host_file_path=''
if platform.system()=='Linux':
    host_file_path= '/etc/hosts'
elif platform.system()=='Windows':
    host_file_path= 'C:\Windows\System32\drivers\etc\hosts'
else:
    print('Caution: Error while detecting the platform.')
    print('\tDetected Platform was',platform.system())

redirect_path = "127.0.0.1"
websites = [
"www.facebook.com",
"facebook.com", "twitter.com", "www.twitter.com",
"youtube.com", "www.youtube.com",
"www.reddit.com",
"reddit.com",
"www.dsogaming.com","dsogaming.com",
"www.gamemag.ru","gamemag.ru",
"www.9gag.com","9gag.com",
"www.3dnews.ru","3dnews.ru",
"www.phoronix.com","phoronix.com"
]


def write_to_hosts_file(host_file_path, websites,redirect_path):
        print("Time to block website!")
        # Open the hosts file
        with open(host_file_path, 'r+') as file:
            # Read the content and print it out on the terminal
            content = file.read()
            print(content)
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write (redirect_path + " " + website + "\n")
        print("Updated /etc/hosts \n")


def unblock_hosts(host_file_path, websites, redirect_path):
        with open (host_file_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("Websites are unblocked!")

# Need to make script very adaptable

# To make the script running all the time
while True:
    curr_time = dt(dt.now().year, dt.now().month, dt.now().day,dt.now().hour, dt.now().minute)

    time_allow_start_1 = dt(dt.now().year, dt.now().month, dt.now().day, 8)
    time_allow_end_1 = dt(dt.now().year, dt.now().month, dt.now().day, 9,00)
    print('curr_time is ', curr_time)
    print('time 1 is ', time_allow_start_1)
    print('time 2 is ', time_allow_end_1)
    #time.sleep(10)
    time_allow_start_3 = dt(dt.now().year, dt.now().month, dt.now().day, 20)
    time_allow_end_3 = dt(dt.now().year, dt.now().month, dt.now().day, 21,00)

    time_allow_start_2 = dt(dt.now().year, dt.now().month, dt.now().day, 16)
    time_allow_end_2 = dt(dt.now().year, dt.now().month, dt.now().day, 17,00)


    if time_allow_start_3 <curr_time< time_allow_end_3:
        print('Allow time')
        unblock_hosts(host_file_path, websites, redirect_path)
    elif time_allow_start_2 <curr_time< time_allow_end_2:
        print('Allow time')
        unblock_hosts(host_file_path, websites, redirect_path)
    elif time_allow_start_1 <curr_time< time_allow_end_1:
        print('Allow time')
        unblock_hosts(host_file_path, websites, redirect_path) 
    else:
        print('Block Time')
        write_to_hosts_file(host_file_path, websites,redirect_path)
    time.sleep(10)
        
    #     print("Time to block website!")
    #     # Open the hosts file
    #     with open(host_file_path, 'r+') as file:
    #         # Read the content and print it out on the terminal
    #         content = file.read()
    #         print(content)
    #         for website in websites:
    #             if website in content:
    #                 pass
    #             else:
    #                 file.write (redirect_path + " " + website + "\n")
    # else:
    #     with open (host_file_path, 'r+') as file:
    #         content = file.readlines()
    #         file.seek(0)
    #         for line in content:
    #             if not any(website in line for website in websites):
    #                 file.write(line)
    #         file.truncate()
    #     print("Websites are unblocked!")
    # time.sleep(10)