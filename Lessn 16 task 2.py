class   turtle(object):
    x=0
    y=0
    s=1
    def go_up(self):
        self.y+=self.s
    def go_down(self):
        self.y-=self.s
    def go_left(self):
        self.x-=self.s
    def go_right(self):
        self.x+=self.s
    def evolve(self):
        self.s+=1
    def degrade(self):
        if self.s >1:
            self.s-=1
        elif self.s ==1:
            print("Значение шага черепашки минимально")
    def count_moves(self,x2,y2):
        tmpx=x2
        tmpy=y2
        step=0
        if x2>self.x:
            x2-=self.x
            if x2%self.s == 0:
                 step = step +(x2//self.s)
            else:
                step = step +(x2//self.s)
                step+=1
        else:
            if x2<self.x:
                x2-=self.x
                x2= abs(x2)
            if x2%self.s == 0:
                 step = step+(x2//self.s)
            else:
                step = step+(x2//self.s)
                step+=1
                0
        if y2>self.y:
            y2-=self.y
            if y2%self.s == 0:
                 step = step+(y2//self.s)
            else:
                step = step+(y2//self.s)
                step+=1
        else:
            if y2<self.y:
                y2-=self.y
                y2=abs(y2)
            if y2%self.s == 0:
                 step = step+(y2//self.s)
            else:
                step = step+(y2//self.s)
                step+=1
        print(f"Минимально количесвто шагов черепашки чтобы достичь",tmpx,tmpy,"=", step)
t1=turtle()
t1.go_up()
t1.go_up()
t1.go_right()
t1.go_right()
t1.evolve()
t1.go_up()
t1.go_up()
t1.go_right()
t1.go_right()
print(t1.x)
print(t1.y)
t1.count_moves(15,17)