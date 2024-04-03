def Psyco(input_student):
    return input_student
print(Psyco("pavi")) #pavi
def ds(input_students):
    return input_students + 15
print(ds(15))  #25
def ds(input_students):
    return input_students + 'string'
print(ds("pavi")) #pavistring
def ds(input_students):
    return input_students + 10
try:
    ds("pavi")
except:
    print("string+int are not concadenate") #string+int are not concadenate
''' ouput
pavi
20
pavistring
string+int are not concadenate
'''

class Calculation:
    def __init__(self,num1,num2):
       self.num1=num1
       self.num2=num2
    def add(self):
        return self.num1+self.num2 #Addition 15
    def sub(self):
        return self.num1-self.num2 #subtraction 6
    def multi(self):
        return self.num1*self.num2 #multiplication 23
    def div(self):
        return self.num1/self.num2 #Division 2.3333
    

performance=Calculation(23,28)
print("Addition",performance.add())
print("subtraction",performance.sub())
print("Multiplication",performance.multi())
print("Division",performance.div())
''' output
Addition 15
Subtraction 6
Multiplication 23
Division 2.3333'''

def Psyco(input_students):
    return input_students + 15
try:
    Psyco("pavi")
except (ValueError,TypeError):
    print('not clear')

    """OUTPUT :
    not clear"""

def Email(name,age,year,college,department):
    print("My name is", name)
    print("Hi,I am",age)
    print("I was studying",year,"year")
    print("From",college)
    print("And about my department",department)
#you will get correct output because argument is given in order
print("Case-1:")
Email("Harini",23,5,"AnnaiMira college of engineering and technology","AI&DS")
"""
My name is Harini 
Hi,I am 20
I was Studying 3rd year
From AnnaiMira college of engineering and technology
And about my department AI&DS
"""
def BODMAS(val1,val2):
    return val1-val2
val1,val2=22,20
result=BODMAS(val1,val2)
print(result) #output:2

#defining pen class 
class pen():
    #arfs receives unlimited no.of arguments as an array
    def __init__(self, *args):
    #access args index like array does
     self.type = args[0]
     self.color = args[1]
#creating objects of pen class
Rorito = pen('Gel','Black')
Renolds = pen('Ballpoint','Blue')
Parker = pen('Ink','Red')
#printing the color and type of the pens 
print(Rorito.color)
print(Renolds.type)
'''
output:
Black
Ballpoint'''
#defining Sneakers class
class Sneakers():
    #args receives umlimited no.of arguments an array
    def __init__(self, **kwargs):
    #access args index like array does
     self.type = kwargs['w']
     self.color = kwargs['c']


#creating objects of Sneakers class
Pride = Sneakers(w='Formal Sneakers',c='White')
Bata = Sneakers(w='Casual Sneakers',c='Yellow')
Walkaro =Sneakers(w='Dailywear Sneakers',c='Red')


#printing the color and type of bag

print(Bata.color)
print(Walkaro.type)
'''
output:
Yellow
Dailywear Sneakers'''