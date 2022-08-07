# program to make a qrcode having personal information of the user
from msvcrt import getch
import qrcode
import os 
import cv2
qr=qrcode.QRCode(
    version=1,     
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

def option():
    os.system("cls")
    print("\t\t <--------------------------------------------->")
    print(f"\t\t     <-------- Choose Your Options ---------> ")
    print(f"\t\t\t   1. URL QRCode generator")
    print(f"\t\t\t   2. Contact  QRCode generator")
    print(f"\t\t\t   3. Message  QRCode generator")
    print(f"\t\t\t   4. Mail  QRCode generator")
    print(f"\t\t\t   5. Text  QRCode generator")
    print(f"\t\t\t   6. Phone  QRCode generator")
    print("\t\t <--------------------------------------------->")

    chu=int(input())

    if chu==1:
        generate_url()
    elif chu==2:
        generate_contact()
    elif chu==3:
        generate_msg()
    elif chu==4:
        generate_mail()
    elif chu==5:
        generate_text()
    elif chu==6:
        generate_phone()
    else:
        print(f"\t\t <---- Invalid options ---> ")
        getch()

def generate_mail():
    os.system("cls")
    print(f"\t\t <----- Welcome to Mail QRCODE GENERATOR ----> ")
    mail_address=input("\t\t\t Enter Email Address -----> ")
    subject=input("\t\t\t Enter Subject of Mail -----> ")
    body=input("\t\t\t Enter Message of Mail -----> ")
    data="mailto:"+mail_address+"?"+"body="+body+"&subject="+subject
    save_to_data(data)

def generate_phone():
    os.system("cls")
    print(f"\t\t <----- Welcome to Phone QRCODE GENERATOR ----> ")
    Phone_no=input("\t\t\t Enter Phone no -----> ")
    # tel:+1-202-555-0180
    data="tel:"+Phone_no
    save_to_data(data)

def generate_text():
    os.system("cls")
    print(f"\t\t <----- Welcome To Free QRCODE GENERATOR ----> ")
    data=input("\t\t Enter Text Now -----> ")
    save_to_data(data)

def generate_msg():
    os.system("cls")
    print(f"\t\t <----- Welcome to Message QRCODE GENERATOR ----> ")
    phoneno=input("\t\t\t Enter Phone no -----> ")
    message=input("\t\t\t Enter Message To Send  -----> ")
    # SMSTO:90055856:sarooj is back in the hell
    data="SMSTO:"+phoneno+":"+message
    save_to_data(data)

def generate_url():
    os.system("cls")
    print(f"\t\t <----- Welcome to Generator URL ------> ")
    data=input(f"\t\t\t Enter the Url ----> ")
    save_to_data(data)

def save_to_data(info):
    os.system("cls")
    image_name=input("\n\t\t\t Enter the name of image ----> ")
    path_full=os.getcwd()+"/Image"
    if (os.path.exists(path_full) != 1):
        os.mkdir("Image")
    path="Image/"+image_name+".png"
    qr.add_data(info)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black", back_color="white")
    img.save(path)
    print(f"\t\t\t  [GENERATING] QrCode .....")
    print(f"\t\t\t  [Sucessfully Generated] QRCode .....")
    print(f"\t\t\t  <----- Image is Saved to {path} ----> ")
    getch()

def generate_contact(): 
    os.system("cls")
    print(f"\n\t\t <----- Welcome To Input Section ------> ")
    first_name=input("\t\t\t Enter Firtname -----> ")
    organization=input("\t\t\t Enter Organization -----> ")
    title_name=input("\t\t\t Enter Title name -----> ")
    email = input("\t\t\t Enter Email Address ----> ")
    phone_no = input("\t\t\t Enter Phnoe number ----> ")
    mobile_no = input("\t\t\t Enter Mobile number ----> ")
    Fax=input("\t\t\t  Enter Fax -----> ")
    Address = input("\t\t\t Enter the Address -----> ")
    url=input("\t\t\t Enter the url of any profile ----> ")

    os.system("cls")
    print(f"\t\t   <---- Checking data now ----> ")
    print(f"\t\t\t  First Name ----> {first_name} ")
    print(f"\t\t\t  Organization ----> {organization} ")
    print(f"\t\t\t  title_name ----> {title_name} ")
    print(f"\t\t\t  Email ----> {email} ")
    print(f"\t\t\t  Phone no ----> {phone_no} ")
    print(f"\t\t\t  Mobile no ----> {mobile_no} ")
    print(f"\t\t\t  Fax ----> {Fax} ")
    print(f"\t\t\t  Address ----> {Address} ")
    print(f"\t\t\t  URL ----> {url} ")
    
    cha=input("\n\n\t\t\t Press y for to generated Qr code \n\t\t\t Press n for to edit --> ")
    if cha=='Y' or cha=='y':
        # info="BEGIN:VCARD\nVERSION:4.0\nFN:"+name+"\nTITLE:"+title_name+"\nTEL;TYPE:tel:"+phone_no+"\nADR;TYPE#WORK;PREF:;;"+Address+"\nEMAIL:"+email+"\nEND:VCARD"
        
        info="BEGIN:VCARD\nVERSION:3.0\nN:;"+first_name+"\nORG:"+organization+"\nTITLE:"+title_name+"\nEMAIL;TYPE=INTERNET:"+email+"\nURL:"+url+"\nTEL;TYPE=CELL:"+mobile_no+"\nTEL:"+phone_no+"\nTEL;TYPE=FAX:"+Fax+"\nADR:"+Address+"\nEND:VCARD"
        save_to_data(info)
        
    else:
        os.system("cls")
        generate_contact()

def about():
    os.system("cls")
    print(f"\t\t <---- This program is designed by Saroj Kumar Tharu to store personal information in qrcode form ------> ")

def descan():
    print(f"\t\t <----- Welcome to Decode Section ------> ")
    print("\t\t Enter path of QRCODE ----> ")
    path=input()
    image=cv2.imread(path);
    detector=cv2.QRCodeDetector() 
    var,b,c=detector.detectAndDecode(image)

    os.system("cls")
    print(f"\t\t\t <----- The Content of the QRCODE ------> ")
    print(f"{var}")
    getch()

def menu():

    while True:
        os.system("cls")
        print("\t\t <---------------------------------------->")
        print(f"\t\t     <----- Welcome To Main Menu -----> ")
        print(f"\t\t\t   1 . Generate QRCODE ")
        print(f"\t\t\t   2 . Decode QRCODE ")
        print(f"\t\t\t   10. About ")
        print(f"\t\t\t   99. Exit ")
        print("\t\t <---------------------------------------->")
        ch = int(input())

        if ch == 1:
            option()
        elif ch==2:
            descan()
        elif ch == 10:
            about()
            getch()
        elif ch == 99:
            print(f"\t\t <------- Thanks For Our Program ----> ")
            exit(0)
        else:
            print(f"\t\t <------ Invalid option ----> ")
            getch()


def main():
    menu()


if __name__ == "__main__":
    main()
