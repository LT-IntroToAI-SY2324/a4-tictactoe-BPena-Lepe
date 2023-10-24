# object oriented programming

# (define-struct dog [fur_color name age favorite_food])
class dog:
    # functions that start with __ are not intended to be called directly
    def __init__(self, fc="",a=0, w=0.0, n="") -> None:
        pass


        self.furcolor=fc
        self.age=a
        self.weight=w
        self.name=n
        self.fetch=0
    
    def __str__(self) -> str:
        s="The dog's name is " + self.name +"\n"
        s+="the dogs color is"+ self.furcolor +"\n"
        return s
    def playfetch(self, numtimes) :
        self.fetch += numtimes
        
bergdog=dog("black",7,78.2,"logan")
ninadog=dog("brown",3,100.0,"hobbes")