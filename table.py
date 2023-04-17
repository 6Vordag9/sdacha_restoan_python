class Users:
    def __init__(self,mail,password,role,money,moneySpent,cardLoyalty):
        self.mail = mail
        self.password = password
        self.role=role
        self.money = money
        self.moneySpent=moneySpent
        self.cardLoyalty = cardLoyalty

    def returnUser(self):
        return self.__dict__
class Zakaz:
    def __init__(self,mailUser,nameDish,countDish,sale,priceWhitchskidka, priceWhithOutSkidka, countHeadRat,datatimeZakaza):
        self.mailUser = mailUser
        self.nameDish = nameDish
        self.countDish=countDish
        self.sale = sale
        self.priceWhitchskidka = priceWhitchskidka
        self.priceWhithOutSkidka = priceWhithOutSkidka
        self.countHeadRat = countHeadRat
        self.datatimeZakaza = datatimeZakaza
    def returnZakaz(self):
        return self.__dict__
    
class ingridienticdobav:
    def __init__(self,PotatFrice,PotatoBoiled,CarrotsKorean,CarrotBoiled,SmokedSausage, DoctorSausage, Banduel,otIvanicha,EggsChiken,EggsQuail):
        self.PotatFrice = PotatFrice
        self.PotatoBoiled = PotatoBoiled
        self.CarrotsKorean=CarrotsKorean
        self.CarrotBoiled = CarrotBoiled
        self.SmokedSausage = SmokedSausage
        self.DoctorSausage = DoctorSausage
        self.Banduel = Banduel
        self.otIvanicha = otIvanicha
        self.EggsChiken = EggsChiken
        self.EggsQuail = EggsQuail
    def returnIngrid(self):
        return self.__dict__
    
        