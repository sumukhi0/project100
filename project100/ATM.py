class Atm:
    def __init__(self, name, phonenumber, pinnumber, adress):
        self.n = name
        self.phn = phonenumber
        self.pn = pinnumber
        self.a = adress
    
    def details(self):
        print("details")
        print(self.n)
        print(self.phn)
        print(self.pn)
        print(self.a)

withdrawl = Atm("Aanandhi",7086569325,9466896454231154,"HouseNo 2, LaneNo 5 Jammu")
withdrawl.details() 