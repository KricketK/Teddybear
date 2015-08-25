class Glass:
    size = 0
    clarity = "clear"
    max_volume = 0
    current_volume = 0

    def __init__(self, max_volume):
        self.max_volume = max_volume

    def fill(self, volumn_amt):
        if volumn_amt > self.max_volume:
            print 'overflowed!!'
            self.current_volume = self.max_volume
        else:
            self.current_volume = volumn_amt

    def pour(self, amount):
        if amount > self.current_volume:
            self.current_volume = 0
        else:
            self.current_volume -= amount


class Cat:
    def __init__(self, name, color, attackPower):
        self.name = name
        self.color = color
        self.attackPower = attackPower


    def walk(self):
        pass

    def jump(self):
        pass

    def actLikeAfuckingShit(self):
        pass

    def attack(self, otherCat):
        print "im going to fuck up that cat", otherCat.name
        if self.attackPower > otherCat.attackPower:
            print "I kicked his fucking ass!!"
        else:
            print 'RUN AWAY!!!'


    def speak(self, volume):
        if volume > 5:
            print "MY NAME IS", self.name.upper()
        else:
            print "my name is", self.name
