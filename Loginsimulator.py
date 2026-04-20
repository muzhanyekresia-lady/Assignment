def login(correctEmail = "test@gmail.com," correctPass = "test123"):
    usermail = input("Enter Email:")
    userpass =input (" Enter password:")
    if usermail == correctEmail and userpass == correctPass:
        print(f" Acess granted, welcome{Usermail}")
    else:
        print(f" incorrect credentail, {Usermail} not found") 

login()           
    
 