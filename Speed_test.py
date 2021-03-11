# Python program to test 
# internet speed 

import speedtest

st = speedtest.Speedtest() 


option = int(input('''What speed do you want to test: )) 

1) Download Speed 

2) Upload Speed 

3) Ping 

Your Choice: ''')) 



if option == 1:
    print("Please wait while we get your Download Speed")
    megabyte = st.download() / 1000000
    print(f"Download Speed: {round(megabyte)} mbs/s")

elif option == 2:
     print("Please wait while we get your Upload Speed")
     megabyte = st.upload() / 1000000
     print(f"Upload Speed: {round(megabyte)} mbs/s")

else: 

    print("Please enter the correct choice !") 
