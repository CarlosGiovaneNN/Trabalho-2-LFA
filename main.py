def removeFromStack(stack, symbol):
    if symbol != emp:
        stack.pop()

def addToStack(stack, symbol):
    if symbol != emp:
        stack.append(symbol)


def AFD(machine, string):
    (q, sigma, delta, q0, f) = machine

    stack = []
    qNext= q0
    
    # for char in string:
    #     qA= delta[(qA, char)]
    # return qA in f
    
    currentSymbol = string.pop(0)
    while True:
        if qNext in f:
            return True
        
        elif (qNext, emp, emp) in delta :
            # empty path
            # print('\n-------------------')
            # print("Current symbol", currentSymbol)
            # print("Current state", qNext)
            # print("Current stack", stack)
            # print('Next State, Symbol to add', delta[(qNext, emp, emp)])
            qNext, stackSymbol = delta[(qNext, emp, emp)]
            addToStack(stack, stackSymbol)
            
        elif (qNext, currentSymbol, emp) in delta:
            # path to add nothing to stack
            # print('\n-------------------')
            # print("Current symbol", currentSymbol)
            # print("Current state", qNext)
            # print("Current stack", stack)
            # print('Next State, Symbol to add', delta[(qNext, currentSymbol, emp)])
            qNext, stackSymbol = delta[(qNext, currentSymbol, emp)]
            addToStack(stack, stackSymbol)
            currentSymbol = string.pop(0) if string else emp
            
        elif (qNext, currentSymbol, stack[-1]) in delta:
            # path to add something to stack
            # print('\n-------------------')
            # print("Current symbol", currentSymbol)
            # print("Current state", qNext)
            # print("Current stack", stack)
            # print('Next State, Symbol to add', delta[(qNext, currentSymbol, stack[-1])])
            qNext, stackSymbol = delta[(qNext, currentSymbol, stack[-1])]
            removeFromStack(stack, stack[-1])
            addToStack(stack, stackSymbol)
            currentSymbol = string.pop(0) if string else emp
            
        else:
            return False
            

emp = ''

q = {'q0', 'q1', 'q2', 'q3', 'q4'}
sigma = {'A', 'C', 'G', 'T', '#'}

# CURRENT STATE - READ SYMBOL - SYMBOL TO REMOVE : NEXT STATE - SYMBOL TO ADD
delta = {
    ('q0', emp, emp): ['q1', '$'],
    ('q1', 'C', emp): ['q1', emp],
    ('q1', 'G', emp): ['q1', emp],
    ('q1', 'A', 'T'): ['q1', emp],
    ('q1', 'T', 'A'): ['q1', emp],
    ('q1', 'A', 'A'): ['q2', 'A'],
    ('q1', 'A', '$'): ['q2', '$'],
    ('q1', 'T', 'T'): ['q3', 'T'],
    ('q1', 'T', '$'): ['q3', '$'],
    ('q1', '#', '$'): ['q4', emp],
    ('q2', emp, emp): ['q1', 'A'],
    ('q3', emp, emp): ['q1', 'T'],
}
q0 = 'q0'
f = {'q4'}

machine = (q, sigma, delta, q0, f)

teste = ['A', 'G', 'C', 'T', '#']

print(AFD(machine, list('AGCTT#')))