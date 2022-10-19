
def main():
    print("EMAIL SLICER")
    print("")

    
    email_in=input("Enter your email: ")
   

    (name, domain)=email_in.split("@")
    (domain,extension)=domain.split(".")

    print("Name: ",name)
    print("Domain: ",domain)
    print("Extension: ",extension)
    

while True: 
        main()
