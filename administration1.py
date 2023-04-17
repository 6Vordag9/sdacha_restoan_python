import main
import table
import random
import os
import zakupka
class adm:
    def glavnayaStr(mail):
        Cleare = os.system("cls")
        print("Вы вошли как админ")
        isSelected = False
        ff = main.UsersAdd.GetUserInfo(mail)
        for i in ff:
            ffdict=i.to_dict()
            id = i.id
        if int(ffdict['money'])<=0:
            userupdate = table.Users(mail,ffdict['password'],ffdict['role'], 500, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
            main.UsersAdd.UpdateUser(id,userupdate)
        j = main.UsersAdd.GetUserInfo(mail)
        for i in j:
            jdict=i.to_dict()
            id = i.id    
        monyePlus = int(jdict['money'])
        plusproc = random.randint(20, 40)
        monyePlus = monyePlus + (monyePlus * (plusproc / 100))
        
        userupdate = table.Users(mail,ffdict['password'],ffdict['role'],monyePlus, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
        main.UsersAdd.UpdateUser(id,userupdate)  
        while(isSelected==False):
            Cleare()
            print("\nВыберите действие:")
            print("1.Посмотреть историю пользователя.")
            print("2.Закупка товара.")
            print("3.Проверить карту клиента.")
            print("4.Выйти на авторизацию.")
            dei = int(input("Введите цифру нужного действия "))
            Cleare()
            match dei:
                case 1:
                    usermail = input("Введите почту пользователя:")
                    gg = main.ZakazAdd.GetUserZakaz(usermail)
                    for i in gg:
                        ggdict=i.to_dict()
                        print("______________________")
                        print ("Название блюд: " + ggdict['nameDish'])
                        print ("Колличество блюд: "+ str(ggdict['countDish']))
                        print ("Ценник заказа: "+ str(ggdict['priceWhitchskidka']))
                        print ("Колличество голов крыс "+ str(ggdict['countHeadRat']))
                case 2:
                    
                    zakupka.Zalup.kup(mail)
                case 3:
                    usermail = input("Введите почту пользователя:")
                    gg = main.UsersAdd.GetUserInfo(usermail)
                    for i in gg:
                        ggdict=i.to_dict()
                        print("______________________")
                        print ("Почта пользователя: " + ggdict['mail'])
                        print ("Уровень карты лояльности: "+ (ggdict['cardLoyalty']))
                        print ("Потрачено денег: "+ str(ggdict['moneySpent']))
                        
                case 4:
                    isSelected=True
# adm.glavnayaStr("test@test.test")            
    