class human:
    def __init__(self, n, o):
        self.name = n
        self.ocupation = o
    def do_work(self):
        if self.ocupation == "tennis Player":
            print(self.name,"plays tennis")
        elif self.ocupation == "actor":
            print(self.name,"shoot a filim")

    def speaks(self):
        print(self.name,"says how are you")


tom = human("tom cruise","actor")
tom.do_work()
tom.speaks()

maria = human("maria","tennis Player")
maria.do_work()
maria.speaks()