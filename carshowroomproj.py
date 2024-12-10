class carshowroom:
    def __init__(self):
        self.cgst=0.18
        self.sgst=0.18
        self.insurance=100000
    def company(self):
        while True:
            print("mahindra","mercedies","toyota")
            self.c=input("Enter car company name=")
            if self.c=="mahindra":
                print("Welcome to mahindra family")
                self.model()
                break
            elif self.c=="mercdies":
                print("Welcome to mercedies family")
                self.model()
                break
            elif self.c=="toyota":
                print("Welcome to toyata family")
                self.model()
                break
            else:
                print("Enter valid company")
    def model(self):

            if self.c=="mahindra":
                while True: 
                    print("available models are thar and scorpio")
                    self.choice=input("Enter car model")
                    if self.choice=="thar":
                        self.price(self.choice)
                        break
                    elif self.choice=="scorpio":
                        self.price(self.choice)
                        break
                    else:
                        print("enter valid model")
            elif self.c=="mercedies":
                while True:
                    print("available models are gw and agm")
                    self.choice=input("Enter car model")
                    if self.choice=="gw":
                        self.price(self.choice)
                        break
                    elif self.choice=="agm":
                        self.price(self.choice)
                        break
                    else:
                        print("enter valid model")
            elif self.c=="toyota":
                while True:
                    print("available models are innova and fortuner")
                    self.choice=input("Enter car model")
                    if self.choice=="innova":
                        self.price(self.choice)
                        break
                    elif self.choice=="fortuner":
                        self.price(self.choice)
                        break
                    else:
                        print("enter valid model")
    def price(self,choice):
        if self.choice=="thar":
            self.price=1800000
        if self.choice=="scorpio":
            self.price=1358000
        if self.choice=="gw":
            self.price=1300000
        if self.choice=="agm":
            self.price==8700000
        if self.choice=="innova":
            self.price=1999000
        if self.choice=="fortuner":
            self.price==3343000
        self.totalprice=self.price+(self.price*self.cgst)+(self.price*self.sgst)+self.insurance
        print(self.totalprice)
obj=carshowroom()
obj.company()
        

                
   