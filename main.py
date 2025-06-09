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
    
    qCurrent = machine.q0                                                                           # ESTADO INICIAL
    stack = []                                                                                      # PILHA INICIA VAZIA
    currentSymbol = string.pop(0)                                                                   # PEGA O PRIMERO SIMBOLO DA STRING E REMOVE DO ARRAYT
    
    while currentSymbol in machine.sigma:                                                           # FAZ LOOP ENQUANTO A STRING NAO ESTIVER VAZIA OU FOR DIFERENTE DO ALFABETO
    
        if (qCurrent, epsilon, epsilon) in machine.delta:                                           # VERIFICA SE EXISTE UMA TRANSICAO SEM LER O SIMBOLO E COM NADA NA PILHA(SEM TIRAR NADA DA PILHA)
            qCurrent, stackSymbol = machine.delta[(qCurrent, epsilon, epsilon)]                     # PEGA A PROXIMA TRANSICAO
            addToStack(stack, stackSymbol)                                                          # ADICIONA O SIMBOLO NA PILHA
            
        elif (qCurrent, currentSymbol, epsilon) in machine.delta:                                   # VERIFICA SE EXISTE UMA TRANSICAO LENDO O SIMBOLO E COM NADA NA PILHA(SEM TIRAR NADA DA PILHA)
            qCurrent, stackSymbol = machine.delta[(qCurrent, currentSymbol, epsilon)]               # PEGA A PROXIMA TRANSICAO
            addToStack(stack, stackSymbol)                                                          # ADICIONA O SIMBOLO NA PILHA
            currentSymbol = string.pop(0) if string else epsilon                                    # COLOCA O PROXIMO SIMBOLO, CASO TENHA ALGO PARA TIRAR TIRA SE NAO DEIXA COM EPSILON
            
        elif (qCurrent, currentSymbol, stack[-1] if len(stack) > 0 else epsilon) in machine.delta:  # VERIFICA SE EXISTE UMA TRANSICAO LENDO O SIMBOLO E COM ALGO NO TOPO DA PILHA E RETIRANDO
            qCurrent, stackSymbol = machine.delta[(qCurrent, currentSymbol, stack[-1])]             # PEGA A PROXIMA TRANSICAO
            removeFromStack(stack, stack[-1])                                                       # REMOVE O SIMBOLO NA PILHA
            addToStack(stack, stackSymbol)                                                          # ADICIONA O SIMBOLO NA PILHA
            currentSymbol = string.pop(0) if string else epsilon                                    # COLOCA O PROXIMO SIMBOLO, CASO TENHA ALGO PARA TIRAR TIRA SE NAO DEIXA COM EPSILON
            
        else:
            break
    
    if(len(string) > 0 or currentSymbol != epsilon): return False                                   # SE A STRING NAO ESTIVER VAZIA OU O SIMBOLO FOR DIFERENTE DE EPSILON RETORNA FALSO

    return qCurrent in machine.f                                                                    # VERIFICA SE O ESTADO ATUAL ESTA NO FINAL


def getMachine():
    q = {'q0', 'q1','q2', 'q3', 'q4', 'q5'}             # ESTADOS
    sigma = { epsilon, 'A', 'C', 'G', 'T', '#'}         # ALFABETO

    # CURRENT STATE - READ SYMBOL - SYMBOL TO REMOVE : NEXT STATE - SYMBOL TO ADD
    delta = {
        ('q0', epsilon, epsilon): ['q1', '$'],
        ('q1', 'A', epsilon): ['q3', epsilon],
        ('q1', 'C', epsilon): ['q2', epsilon],
        ('q1', 'G', epsilon): ['q2', epsilon],
        ('q1', 'T', epsilon): ['q4', epsilon],
        ('q2', 'C', epsilon): ['q2', epsilon],
        ('q2', 'G', epsilon): ['q2', epsilon],
        ('q2', 'A', 'T'): ['q2', epsilon],
        ('q2', 'T', 'A'): ['q2', epsilon],
        ('q2', 'A', 'A'): ['q3', 'A'],
        ('q2', 'A', '$'): ['q3', '$'],
        ('q2', 'T', 'T'): ['q4', 'T'],
        ('q2', 'T', '$'): ['q4', '$'],
        ('q2', '#', '$'): ['q5', epsilon],
        ('q3', epsilon, epsilon): ['q2', 'A'],
        ('q4', epsilon, epsilon): ['q2', 'T'],
    }                                                   # TRANSICOES
    q0 = 'q0'                                           # ESTADO INICIAL
    f = {'q5'}                                          # ESTADOS FINAIS
    
    return Machine(q, sigma, delta, q0, f)
        

def main ():
    machine = getMachine()                              # CONFIGURA A MAQUINA

    while True:
        string = input("Enter a string: ")              # RECEBE A STRING
        
        if string == '/exit;': break                    # SAIDA
        
        try:                                            # TRY CATCH USADO PARA ALGUM ERRO NO STACK PARA NAO PARAR O PROGRAMA
            if AFD(machine, list(string)):              # SE A STRING FOR ACEITA
                print("Accepted")
            else:                                       # SE A STRING FOR REJEITADA
                print("Rejected") 
        except:
            print("Rejected")
    
    
main ()