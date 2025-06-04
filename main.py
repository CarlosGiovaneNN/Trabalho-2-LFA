epsilon = 'ε'

class Machine:
    def __init__(self, q, sigma, delta, q0, f):
        self.q = q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.f = f

def removeFromStack(stack: list, symbol: str):
    if symbol != epsilon:
        stack.pop()

def addToStack(stack: list, symbol: str):
    if symbol != epsilon:
        stack.append(symbol)
        
def printInfo(qCurrent: str, currentSymbol: str, stack: list, delta: dict, epsilon: str = None):
    print('\n-------------------\n')
    print("Current symbol", currentSymbol)
    print("Current state", qCurrent)
    print("Current stack", stack)
    print('Next State, Symbol to add', delta[(qCurrent, currentSymbol, stack[-1] if epsilon == None else epsilon)])


def AFD(machine: Machine, string: list):
    
    qCurrent = machine.q0
    stack = []
    currentSymbol = string.pop(0)
    
    while currentSymbol in machine.sigma:
    
        if (qCurrent, epsilon, epsilon) in machine.delta :
            # empty path
            printInfo(qCurrent, epsilon, stack, machine.delta, epsilon)
            qCurrent, stackSymbol = machine.delta[(qCurrent, epsilon, epsilon)]
            addToStack(stack, stackSymbol)
            
        elif (qCurrent, currentSymbol, epsilon) in machine.delta:
            # path to add nothing to stack
            printInfo(qCurrent, currentSymbol, stack, machine.delta, epsilon)
            qCurrent, stackSymbol = machine.delta[(qCurrent, currentSymbol, epsilon)]
            addToStack(stack, stackSymbol)
            currentSymbol = string.pop(0) if string else epsilon
            
        elif (qCurrent, currentSymbol, stack[-1] if len(stack) > 0 else epsilon) in machine.delta:
            # path to add something to stack
            printInfo(qCurrent, currentSymbol, stack, machine.delta)
            qCurrent, stackSymbol = machine.delta[(qCurrent, currentSymbol, stack[-1])]
            removeFromStack(stack, stack[-1])
            addToStack(stack, stackSymbol)
            currentSymbol = string.pop(0) if string else epsilon
        
        elif string == []:
            break
            
        else:
            break
        
    return qCurrent in machine.f


def getMachine():
    q = {'q0', 'q1', 'q2', 'q3', 'q4'}
    sigma = { epsilon, 'A', 'C', 'G', 'T', '#'}

    # CURRENT STATE - READ SYMBOL - SYMBOL TO REMOVE : NEXT STATE - SYMBOL TO ADD
    delta = {
        ('q0', epsilon, epsilon): ['q1', '$'],
        ('q1', 'C', epsilon): ['q1', epsilon],
        ('q1', 'G', epsilon): ['q1', epsilon],
        ('q1', 'A', 'T'): ['q1', epsilon],
        ('q1', 'T', 'A'): ['q1', epsilon],
        ('q1', 'A', 'A'): ['q2', 'A'],
        ('q1', 'A', '$'): ['q2', '$'],
        ('q1', 'T', 'T'): ['q3', 'T'],
        ('q1', 'T', '$'): ['q3', '$'],
        ('q1', '#', '$'): ['q4', epsilon],
        ('q2', epsilon, epsilon): ['q1', 'A'],
        ('q3', epsilon, epsilon): ['q1', 'T'],
    }
    q0 = 'q0'
    f = {'q4'}
    
    return Machine(q, sigma, delta, q0, f)
        

def main ():
    machine = getMachine()

    while True:
        string = input("Enter a string: ")
        
        if string == '/exit;': break
        
        try: 
            if AFD(machine, list(string)):
                print("Accepted")
            else:
                print("Rejected") 
        except:
            print("Rejected")
    
    
main ()