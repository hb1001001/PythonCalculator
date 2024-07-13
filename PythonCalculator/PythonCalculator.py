#
# TOP OF APPLICATION
#
# CALCULATOR APP


def Calculator():
  
    # programme loop + initial input
  while True:
        calcInput = input("ADD/SUBTRACT/DIVIDE/MULTIPLY?")


        #Calculation Function's ADDITION/SUBTRACTION/DIVISION/MULTIPLICATION
        def ADDITION():
            addInputA = input("first number to add?")
            addInputB = input("second number to add?")
        
            numA = int(addInputA)
            numB = int(addInputB)
    
            sum = numA + numB
            print(sum)
        
        def SUBTRACTION():
            subInputA = input("first number ?")
            subInputB = input("number to subtract?")
        
            numA = int(subInputA)
            numB = int(subInputB)
    
            sum = numA - numB
            print(sum)
        
        def DIVISION():
            subInputA = input("first number? ")
            subInputB = input("second number? ")
    
            A = int(subInputA)
            B = int(subInputB)
            if B == 0:
                raise ValueError("Cannot divide by zero")

            CounterLoop = 0
        
            while A >= B:
                A -= B
                CounterLoop += 1
  
            print(CounterLoop)
            print("The remainder: ", A)

        def MULTIPLICATION():
            subInputA = input("first number? ")
            subInputB = input("second number? ")
    
            A = int(subInputA)
            B = int(subInputB)
            CounterLoop = 0
    
            for i in range(B):  
                CounterLoop += A  
            
            print(CounterLoop)
   


        #calculation type decision tree
        if calcInput == "ADD":
            ADDITION()
        elif calcInput == "SUBTRACT":
            SUBTRACTION()
        elif calcInput == "DIVIDE":
            DIVISION()
        elif calcInput == "MULTIPLY":
            MULTIPLICATION()
        else:
            print("Wrong input.")
        
  # Main Function       
Calculator()

#
# BOTTOM OF APPLICATION
#
