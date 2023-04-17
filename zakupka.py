import main
import table
class Zalup:
    def kup(mail):
        j = main.UsersAdd.GetUserInfo(mail)
        for i in j:
            jdict=i.to_dict()
            id = i.id    
        print("Доступные действия \n 1.Вывести все ингридиенты со скалада \n 2.Закупить ингридиенты")
        diest = int(input("Ввведите цифру действия: "))
        match diest:
            case 1:
                jj = main.Ingridient.GetIngrid()
                for i in jj:
                    jjdict=i.to_dict()
                
                print("Ингридиенты на складе:\n 1.Картошка фри "+str(jjdict['PotatFrice'])+" \n 2.Вареная картошка "+str(jjdict['PotatoBoiled'])+" \n 3.Марковка по корейски "+str(jjdict['CarrotsKorean'])+" \n 4. Вареная марковка "+str(jjdict['CarrotBoiled'])+" \n 5.Сырокопченая колбаса "+str(jjdict['SmokedSausage'])+" \n 6.Докторская колбаса "+str(jjdict['DoctorSausage'])+" \n 7.Горох Бандюэль "+str(jjdict['Banduel'])+" \n 8.Горох от Иваныча "+str(jjdict['otIvanicha'])+"\n 9.Перепелиные яйца "+str(jjdict['EggsQuail'])+"\n 10.Куриные яйца "+str(jjdict['EggsChiken']))    
            case 2:
                print("Выбирете ингридиент для закупки \n 1.Картошка фри \n 2.Вареная картошка \n 3.Марковка по корейски \n 4. Вареная марковка \n 5.Сырокопченая колбаса \n 6.Докторская колбаса \n 7.Горох Бандюэль \n 8.Горох от Иваныча \n 9.Перепелиные яйца \n 10.Куриные яйца")
                ingr = int(input("Ввведите цифру действия: "))
                ff = main.UsersAdd.GetUserInfo(mail)
                for i in ff:
                      ffdict=i.to_dict()
                      money = ffdict['money']
                match ingr:
                    case 1:
                        count = int(input("Введите колличество ингридиентов"))
                        if money-(count*5)<0:
                            print("Недостаточно средств")
                        else:
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                jjdict=i.to_dict()
                                
                            ingridupdate =table.ingridienticdobav(jjdict['PotatFrice']+count,jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                            main.Ingridient.UpdateIngrid(ingridupdate)   
                            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-count*5, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
                            main.UsersAdd.UpdateUser(id,userupdate)  
                    case 2:
                        count = int(input("Введите колличество ингридиентов"))
                        if money-(count*5)<0:
                            print("Недостаточно средств")
                        else:
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                jjdict=i.to_dict()
                                
                            ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled']+count,jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                            main.Ingridient.UpdateIngrid(ingridupdate)   
                            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-count*5, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
                            main.UsersAdd.UpdateUser(id,userupdate)    
                    case 3:
                        count = int(input("Введите колличество ингридиентов"))
                        if money-(count*5)<0:
                            print("Недостаточно средств")
                        else:
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                jjdict=i.to_dict()
                                
                            ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean']+count,jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                            main.Ingridient.UpdateIngrid(ingridupdate)   
                            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-count*5, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
                            main.UsersAdd.UpdateUser(id,userupdate)
                    case 4:
                        count = int(input("Введите колличество ингридиентов"))
                        if money-(count*5)<0:
                            print("Недостаточно средств")
                        else:
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                jjdict=i.to_dict()
                                
                            ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled']+count,jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                            main.Ingridient.UpdateIngrid(ingridupdate)   
                            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-count*5, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
                            main.UsersAdd.UpdateUser(id,userupdate)
                    case 5:
                        count = int(input("Введите колличество ингридиентов"))
                        if money-(count*5)<0:
                            print("Недостаточно средств")
                        else:
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                jjdict=i.to_dict()
                                
                            ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage']+count,jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                            main.Ingridient.UpdateIngrid(ingridupdate)   
                            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-count*5, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
                            main.UsersAdd.UpdateUser(id,userupdate)
                    case 6:
                        count = int(input("Введите колличество ингридиентов"))
                        if money-(count*5)<0:
                            print("Недостаточно средств")
                        else:
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                jjdict=i.to_dict()
                                
                            ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage']+count,jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                            main.Ingridient.UpdateIngrid(ingridupdate)   
                            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-count*5, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
                            main.UsersAdd.UpdateUser(id,userupdate)
                    case 7:
                        count = int(input("Введите колличество ингридиентов"))
                        if money-(count*5)<0:
                            print("Недостаточно средств")
                        else:
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                jjdict=i.to_dict()
                                
                            ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel']+count,jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail'])
                            main.Ingridient.UpdateIngrid(ingridupdate)   
                            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-count*5, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
                            main.UsersAdd.UpdateUser(id,userupdate)                
                    case 8:
                        count = int(input("Введите колличество ингридиентов"))
                        if money-(count*5)<0:
                            print("Недостаточно средств")
                        else:
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                jjdict=i.to_dict()
                                
                            ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha']+count,jjdict['EggsChiken'],jjdict['EggsQuail'])
                            main.Ingridient.UpdateIngrid(ingridupdate)   
                            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-count*5, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
                            main.UsersAdd.UpdateUser(id,userupdate)
                    case 9:
                        count = int(input("Введите колличество ингридиентов"))
                        if money-(count*5)<0:
                            print("Недостаточно средств")
                        else:
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                jjdict=i.to_dict()
                                
                            ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken'],jjdict['EggsQuail']+count)
                            main.Ingridient.UpdateIngrid(ingridupdate)   
                            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-count*5, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
                            main.UsersAdd.UpdateUser(id,userupdate)                
                    case 10:
                        count = int(input("Введите колличество ингридиентов: "))
                        if money-(count*5)<0:
                            print("Недостаточно средств")
                        else:
                            jj = main.Ingridient.GetIngrid()
                            for i in jj:
                                jjdict=i.to_dict()
                                
                            ingridupdate =table.ingridienticdobav(jjdict['PotatFrice'],jjdict['PotatoBoiled'],jjdict['CarrotsKorean'],jjdict['CarrotBoiled'],jjdict['SmokedSausage'],jjdict['DoctorSausage'],jjdict['Banduel'],jjdict['otIvanicha'],jjdict['EggsChiken']+count,jjdict['EggsQuail'])
                            main.Ingridient.UpdateIngrid(ingridupdate)   
                            userupdate =table.Users(mail,ffdict['password'],ffdict['role'],int(ffdict['money'])-count*5, int(ffdict['moneySpent']),ffdict['cardLoyalty']) 
                            main.UsersAdd.UpdateUser(id,userupdate)                      
            case 99:
                gg = table.ingridienticdobav(1,1,1,1,1,1,1,1,1,1)
                

                main.Ingridient.IngridAdd(gg)
                
                
