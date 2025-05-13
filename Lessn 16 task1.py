class Kassa (object):
    money = 0
    def top_up(self,x):
        self.money +=x
        print(self.money)
    def count_1000(self):
        print (self.money//1000)
    def take_away(self,x):
        if self.money >=x:
            self.money-=x
            print(self.money)
        else:
            print("Количество денег в кассе меньше запрошенного")
h1=Kassa()
h1.top_up(3546)
h1.count_1000()
h1.take_away(3570)