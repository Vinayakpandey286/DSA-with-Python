class computer:

    def __init__(self,brand,cpu,ram) -> None:
        self.cpu=cpu
        self.ram=ram
        self.brand=brand

    def config(self):
        print("config is:",self.brand,self.cpu,self.ram)

com1=computer("hp","i5",8)
com2=computer("lenovo","i7",16)
com1.config()
com2.config()
