import time
print("="*44)
time.sleep(2)

print(" "*30 + " welcome to hacknet")
time.sleep(2)

print("="*44)

print("Press '1' to hack your Device")
time.sleep(2)

print("press '2' to hack someone else's Device")
time.sleep(5)

num = int(input("please enter 1 or 2 :-  "))

if num==1 or num == 2  :
    print("Process is started")
    time.sleep(5)
    
    if num==1:
        print("Hacking your Device") 
        time.sleep(2)
      
        print("Hacking"+"-"*10+"5%") 
        time.sleep(2)
        
        print("Hacking"+"-"*15+"10%")
        time.sleep(2)
        
        print("Hacking"+'-'*25 + "20%")
        time.sleep(2)
        
        print('Hacking'+'-'*35 + "50%")
        time.sleep(2.5)
        
        print("Hacking"+"-"*45 + "75%")
        time.sleep(3)
        
        print("Hacking" + "-"*50 + "99%")
        time.sleep(5)
        
        print("Hacking"+ "-"*55 + "100%")
        time.sleep(2)
        
        print("Hacking is complete")
        time.sleep(6)
        
        while True :
            print('error')
            print("system is not responding")

    if num==2 :
        print("please wait your network connection is slow")
        time.sleep(2)
        
        k = str(int(input("The number you want to hack:-")))
        y = str(int(input("country code please:-")))
        print("+"+y+k)
        time.sleep(2)
        
        print("press ok to continue" )
        time.sleep(6)
        
        u = input("press ok to continue")
        if u == 'ok':
            print("Our server is gathering information")
            time.sleep(5)
            
            print("Hacking" +"-"*10 + "10%")
            time.sleep(2)
            
            print("Hacking" + "-"*20 + "30%")
            time.sleep(2)
            
            print("Hacking" + "-"*30 +"50%")
            time.sleep(2)
            
            print("Hacking" + "-"*40+ "79%")
            time.sleep(2)
            
            print("Hacking"+"-"*45 + "99%")
            time.sleep(5)
            
            print("Hacking is complete")
            time.sleep(2)
            
            print(" wait your network connection is slow")
            time.sleep(4)
            
            print("gallery" + "-"*100)
            time.sleep(3)
            
            print("WhatsApp" + "-"*100)
            time.sleep(3)
            
            print("Facebook" +"-"*100)
            time.sleep(3)
            
            print("sorry connection lost")
            time.sleep(2)
            
            print("Trying to reconnect")
            time.sleep(3)
            
            print("process stopped")
else:    
    print("you gave a invalid input")
    time.sleep(2)
    print(" I think you don't know English please go and learn English 😁😁😁dummy ")

print("process finished")







