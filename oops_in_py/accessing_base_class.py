# ABC ACCESSINF BASE Class

#3 types 
# code dubicalton , explicit , super()

class Coffee:
    def __init__ (self,suger,milk):
        self.suger= suger
        self.milik= milk

class Black(Coffee):
    def __init__(self,suger,milk,water):
          self.suger= suger
          self.milik= milk
          self.water= water


# call code dublication 

#now explict

class Coffee:
    def __init__ (self,suger,milk):
        self.suger= suger
        self.milik= milk

class Black(Coffee):
    def __init__(self,suger,milk,water):
          Coffee.__init__(self,suger,milk)
          self.water= water

# call explict

#now super ()

class Coffee:
    def __init__ (self,suger,milk):
        self.suger= suger
        self.milik= milk

class Black(Coffee):
    def __init__(self,suger,milk,water):
          super().__init__(suger,milk)
          self.water= water