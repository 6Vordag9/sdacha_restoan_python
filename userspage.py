import main
import zakaz
import table
import random
import os
class gg1: 
   
    def glavnayaUsersPage(mail):
        Cleare = os.system("cls")
        isSelected=False
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
        print("Вы вошли как пользователь")
        while(isSelected==False):
            
            print("\nВыберите действие:")
            print("1.Создать заказ.")
            print("2.История заказов.")
            print("3.Проверить карту лояльности.")
            print("4.Выйти на авторизацию.")
            dei = int(input("Введите цифру нужного действия "))
            Cleare()
            match dei:
                case 1:
                    zakaz.addzakazik.sobrat(mail,id)
                case 2:
                    gg = main.ZakazAdd.GetUserZakaz(mail)
                    for i in gg:
                        ggdict=i.to_dict()
                        print("______________________")
                        print ("Название блюд: " + ggdict['nameDish'])
                        print ("Колличество блюд: "+ str(ggdict['countDish']))
                        print ("Ценник заказа: "+ str(ggdict['priceWhitchskidka']))
                        print ("Колличество голов крыс "+ str(ggdict['countHeadRat']))
                case 3:
                    print("Ваша карта имеет уровень: "+jdict['cardLoyalty']+"\n Вы потратили уже: "+  str(jdict['moneySpent']))
                case 4:
                    Cleare()
                    isSelected = True
                    
# gg1.glavnayaUsersPage("onlidan545545@mail.ru")