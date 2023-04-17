import main
import re
import table
import emails
import administration1
import os
from userspage import gg1

class vhod:
    def authe():
        MailValid:bool=False
        Cleare = os.system("cls")
        Cleare()
        print("Выберите одно из действий.")
        print("1.Авторизация")
        print("2.Регистрация")
        users = main.UsersAdd.Getusers()
        for i in users: usersdict=i.to_dict()
        dei = int(input("Введите цифру нужного действия "))
        match dei:
            case 1:
                mail = input("Введите вашу почту\n")
                password = input("Введите пароль\n")
                
                for i in users:
                    usersdict=i.to_dict()
                    if(mail == usersdict['mail']and password == usersdict['password']):
                            isRegistr = True
                            if (mail == usersdict['mail']and password == usersdict['password'] and usersdict['role']==1):                 
                                administration1.adm.glavnayaStr(mail)
                            else:
                                gg1.glavnayaUsersPage(mail)
                    else:
                        isRegistr = False
                    if(isRegistr==True):
                            print("Авторизация прошла успешно")
            case 2:
                mail = input("Введите вашу почту\n")
                while(MailValid==False):
                    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
                    for i in users:
                        usersdict=i.to_dict()
                    if not re.match(pattern, mail):
                            mail = input("Данная почта уже существует или не соотвутсвует стандарту, введите другую\n")
                    elif (mail == usersdict['email']):
                            mail = input("Данная почта уже существует или не соотвутсвует стандарту, введите другую\n")
                    else:
                            MailValid=True      
                password = input("Введите пароль\n") 
                while(len(password)<6):
                    password = input("Введите пароль\n")  
                code = emails.sendMail(mail);    
                vveden = int(input("Введите код с почты\n")) 
                while(not code == vveden):
                    vveden = input("Введите код с почты\n") 
                main.UsersAdd.Usersadd(table.Users(mail,password,0,500,0,"not"))
                
vhod.authe()                        
                