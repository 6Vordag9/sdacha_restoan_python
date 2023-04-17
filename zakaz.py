import random
import table
import datetime
import main
import os
class addzakazik:
    def sobrat(mail,id):
        price = 100
        Cleare = os.system("cls")
        priceDosntskidka=0
        tarakan = 0
        sale = 0
        nameDish = "Оливье "
        nameAllDish=""
        countDish = int(input("Введите колличество блюд "))
        while (countDish<=0):
                countDish = int(input("Введите колличество блюд"))
                
        if countDish == 5:
            countDish+=1
        for i in range(countDish):
                Cleare()
                nameDish = nameDish + (input("Введите название для своего оливье "))
                vibrano = False
                while vibrano==False:
                    print("Выберите картошку:\n 1:Картошка фри: +20 рублей \n 2:Картошка вареная: +15 рублей")
                    potato = int(input())
                    match potato:
                        case 1: 
                        
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                        jjdict=i.to_dict()
                            if jjdict['PotatFrice'] <= 0:
                                print("На складе не достаточно товара")
                            else:   
                                price+=20       
                                ingridupdate =table.ingridienticdobav(jjdict['PotatFrice']-1,jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                                main.Ingridient.UpdateIngrid(ingridupdate)
                                vibrano = True   
                        case 2: 
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                        jjdict=i.to_dict()
                            if jjdict['PotatoBoiled'] <= 0:
                                print("На складе не достаточно товара")
                            else:   
                                price+=15       
                                ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled']-1,jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                                main.Ingridient.UpdateIngrid(ingridupdate)
                                vibrano = True 
                vibrano = False
                while vibrano==False:   
                    print("Выберите марковку:\n 1:Марковка по корейски: +30 рублей \n 2:Марковка вареная: +15 рублей")
                    potato = int(input())
                    match potato:
                        case 1: 
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                        jjdict=i.to_dict()
                            if jjdict['CarrotsKorean'] <= 0:
                                print("На складе не достаточно товара")
                            else:   
                                price+=30       
                                ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean']-1,jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                                main.Ingridient.UpdateIngrid(ingridupdate)
                                vibrano = True 
                        case 2: 
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                        jjdict=i.to_dict()
                            if jjdict['CarrotBoiled'] <= 0:
                                print("На складе не достаточно товара")
                            else:   
                                price+=15       
                                ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled']-1,jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                                main.Ingridient.UpdateIngrid(ingridupdate)
                                vibrano = True 
                vibrano = False
                while vibrano==False:
                    print("Выберите колбасу:\n 1:Сырокопченая колбаса: +40 рублей \n 2:Доктораская колбаса: +10 рублей")
                    potato = int(input())
                    match potato:
                        case 1: 
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                        jjdict=i.to_dict()
                            if jjdict['SmokedSausage'] <= 0:
                                print("На складе не достаточно товара")
                            else:   
                                price+=40       
                                ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage']-1,jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                                main.Ingridient.UpdateIngrid(ingridupdate)
                                vibrano = True 
                        case 2: 
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                        jjdict=i.to_dict()
                            if jjdict['DoctorSausage'] <= 0:
                                print("На складе не достаточно товара")
                            else:   
                                price+=10       
                                ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage']-1,jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                                main.Ingridient.UpdateIngrid(ingridupdate)
                                vibrano = True
                vibrano = False
                while vibrano==False:                 
                    print("Выберите горошек:\n 1:Бандюэль: +30 рублей \n 2:Горох от Иваныча: +5 рублей")
                    potato = int(input())
                    match potato:
                        case 1: 
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                        jjdict=i.to_dict()
                            if jjdict['Banduel'] <= 0:
                                print("На складе не достаточно товара")
                            else:   
                                price+=30       
                                ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel']-1,jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                                main.Ingridient.UpdateIngrid(ingridupdate)
                                vibrano = True
                        case 2: 
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                        jjdict=i.to_dict()
                            if jjdict['otIvanicha'] <= 0:
                                print("На складе не достаточно товара")
                            else:   
                                price+=5       
                                ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha']-1,jjdict['EggsChiken'],jjdict['EggsQuail'])
                                main.Ingridient.UpdateIngrid(ingridupdate)
                                vibrano = True
                vibrano = False
                while vibrano==False:    
                    print("Выберите яйца:\n 1:Перепелиные: +20 рублей \n 2:Куриные: +10 рублей")
                    potato = int(input())
                    match potato:
                        case 1: 
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                        jjdict=i.to_dict()
                            if jjdict['EggsQuail'] <= 0:
                                print("На складе не достаточно товара")
                            else:   
                                price+=20       
                                ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail']-1)
                                main.Ingridient.UpdateIngrid(ingridupdate)
                                vibrano = True
                        case 2: 
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                        jjdict=i.to_dict()
                            if jjdict['EggsChiken'] <= 0:
                                print("На складе не достаточно товара")
                            else:   
                                price+=20       
                                ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken']-1,jjdict['EggsQuail'])
                                main.Ingridient.UpdateIngrid(ingridupdate)
                                vibrano = True
                code = random.randint(1, 6)
                priceDosntskidka +=price
                nameAllDish= nameAllDish+ nameDish
                if code == 5:
                    tarakan+=1
                    
                    percentage = 30
                    sale += price * (percentage / 100)
                    price = price - (price * (percentage / 100))

        ff = main.UsersAdd.GetUserInfo(mail)
        for i in ff:
            ffdict=i.to_dict()
            card = ffdict['cardLoyalty']
        match card:
            case "not":
                price=price
                if int(ffdict['moneySpent'])>5000:
                    card="bronze"
            case "bronze":
                price = price - (price * (5 / 100))
                if int(ffdict['moneySpent'])>10000:
                    card="silver"
            case "silver":
                price = price - (price * (10 / 100))
                if int(ffdict['moneySpent'])>15000:
                    card="gold"
            case "gold":
                price = price - (price * (20 / 100))
        mon = int(ffdict['money'])-price
        if mon<0:
            print("У вас не хватает денег")
        else:
            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-price, int(ffdict['moneySpent'])+price,card) 
            main.UsersAdd.UpdateUser(id,userupdate)     
            print("Итоговая сумма заказа " + str(price)+"\n"+"Колличество тараканов в ваших блюдах" + str(tarakan))        
            current_time = str(datetime.datetime.now().time()) 
            tt = main.UsersAdd.GetUserInfo("test@test.test")
            for i in tt:
                ttdict=i.to_dict()
                idadm=i.id
            userupdate =table.Users("test@test.test",ttdict['password'],ttdict['role'],int(ttdict['money'])+price, int(ttdict['moneySpent']),ttdict['cardLoyalty']) 
            main.UsersAdd.UpdateUser(idadm,userupdate)  
            
        
            myZakaz = table.Zakaz(mail,nameAllDish,countDish,sale,price,priceDosntskidka,tarakan,current_time)
            main.ZakazAdd.ZakazAdd(myZakaz)
            
# addzakazik.sobrat("onlidan545545@mail.ru","LC1ocs0liqFOg3krIZcM")               