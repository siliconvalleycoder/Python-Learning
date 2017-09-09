
"""
todo tasks: 
- write a input loop  
- add support for other operations (divide by zero)
- add support for graceful exit 
- handle scenario where operation other than (1-5) value range 
- add validation to allow only numeric values (int, float)
- print user friendly result 

things to learn: functions, loop, data type validation , exception handling 

"""
def add (op1, op2):
    if is_float(op1):
        op1 = float (op1)

    if is_float(op2):
        op2 = float (op2)

    if is_int(op1):
        op1 = int (op1)

    if is_int(op2):
        op2 = int (op2)

        return op1 + op2

def sub (op1, op2):
    return int(op1) - int(op2)

def mult (op1, op2):
    return int(op1) * int(op2)

def div (op1, op2):
    return int(op1)/int(op2)

def TakeInput (message):
    o = input (message) ;
    return o; 

def Validate_operation(operation):
    if int(operation) < 1 or int(operation) > 4:
        return False
    else:
        return True

def is_int(s):
    try:
        int(s) # for int
    except ValueError:
        return False

    return True

def is_float(s):
    try:
        float(s) # float
    except ValueError:
        return False

    return True

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False

    return True

def Validate_divisor_non_zero(operand):
    pass 

def run_calc ():
    operand1 = 0
    operand2 = 0

    while True:
        operation = TakeInput("please enter the operation 1(add), 2(Subtract), 3(multiply), 4(divide) : ")
        if (not Validate_operation(operation)):
            print ("invalid operation")
        else:
            break;

    while True:
        operand1 = TakeInput("Enter operand 1: ")
        if (is_number(operand1) == False):
            print ("[%s] is not a number:" %  operand1)
        else:
            break

    while True:
        operand2 = TakeInput("Enter operand 2: ")
        if (is_number(operand2) == False):
            print ("[%s] is not a number:" %  operand2)
        else:
            break

    result = "";
    action = "";

    if operation == "1":
        result = str(add (operand1, operand2))

    else:
        if operation == "2":
            result = str(sub (operand1, operand2))
        
        else:
            if operation == "3":
                result = str(mult (operand1, operand2))

            else:
                if operation == "4":
                    if operand2 == "0":
                        result = "Divide by zero is not allowed"
                    else:
                        result = str(div (operand1, operand2))
                else:
                    result  = "Invalid operation"

    print (result)
    action = input ("Press Enter to continue; Type Exit and and Enter to Exit :");
    if action == "Exit":
        exit();
    
if __name__ == "__main__":
    action = "";
    while True:
        run_calc()
        



'''
    while True:
        operation = input ("please enter the operation 1(add), 2(Subtract), 3(multiply), 4(divide) : ");
        if int(operation) < 1 or int(operation) > 4:
            print ("invalid operation")
        else:
            break
    
    while True:
        o1 = input ("please enter operand 1: ")
        try:
            operand1 = float(o1)
            break
        except ValueError:
            print ("That is not a number:")


    

    while True:
        o2 = input ("please enter operand 2: ")
        try:
            operand2 = float(o2)
            break
        except ValueError:
            print ("That is not a number:")
'''
