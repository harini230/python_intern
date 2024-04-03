"'create a class,functions with init function '"

class studentDetails:
    def __init__(self,student_id,fees=2000):
        self.student_id = student_id 
        self.fees = fees

    def oldfees(self,amount):
        self.fees += amount 
        print(f"oldfees {amount}. paidfees is {self.fees}.")

    def newfees(self,amount):
        if amount <= self.fees:
            self.fees -= amount 
            print(f"newfees {amount}.paidfees is  {self.fees}.")
        else:
            print('Not paid.')

#Example usage:
student_id1 = studentDetails("5135212430")
student_id1 =oldfees(2000)
student_id1=newfees(3000)


" ' Add match case,try and exception, if else condition to the functions' "

class Bike:
    def __init__(self,make,model,year):
        self.make = make
        self.model =model
        try:
            if isinstance(year, int) and year > 0:
                self.year = year
            else:
                raise ValueError("Year must be a positive integer.")
        except ValueError as e:
            print(e)
            self.year =None 

    def info(self):
        if self.year:
            print(f"This Bike is a {self.year}  {self.make} {self.model}.")
        else:
            print("Year information is not available.")


"'Call the functions inside the code '"

Bike1 =Bike("NS200","Pulsar", 2020)
Bike1.info()


Bike2 = Bike("Royal Enfield","Fiesta", -2000)
Bike2.info()



 "' oldfees 2000. paidfees is 3000.
newfees 3000. paidfees is 2500 
This bike is a 2020 NS200 Pulsar.
Yearr must be a positive integer.
Year information not available.'"
