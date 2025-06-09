
# 🧠 PDA Simulator em Python (Comentado)

Este projeto implementa um **autômato com pilha (Pushdown Automaton - PDA)** com suporte a transições epsilon (`ε`). Ele simula o comportamento de uma linguagem formal baseada em pilha, útil para análise de cadeias com estrutura hierárquica (ex: linguagens de DNA, expressões balanceadas, etc).

---

### 🔰 Definições iniciais

```python
epsilon = 'ε'
```
- Define o símbolo `ε` (epsilon), que representa **transições sem leitura de símbolo da entrada**.

---

### ⚙️ Classe da Máquina

```python
class Machine:
    def __init__(self, q, sigma, delta, q0, f):
        self.q = q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.f = f
```

- Define a estrutura da máquina:
  - `q`: conjunto de estados
  - `sigma`: alfabeto de entrada
  - `delta`: função de transição (dicionário de regras)
  - `q0`: estado inicial
  - `f`: conjunto de estados finais

---

### 📦 Operações com a Pilha

```python
def removeFromStack(stack: list, symbol: str):
    if symbol != epsilon:
        stack.pop()
```
- Remove o topo da pilha (somente se o símbolo **não for ε**).

```python
def addToStack(stack: list, symbol: str):
    if symbol != epsilon:
        stack.append(symbol)
```
- Adiciona um símbolo à pilha (desde que não seja ε).

---

### 🧾 Impressão de informações (opcional)

```python
def printInfo(qCurrent: str, currentSymbol: str, stack: list, delta: dict, epsilon: str = None):
    print('\n-------------------\n')
    print("Current symbol", currentSymbol)
    print("Current state", qCurrent)
    print("Current stack", stack)
    print('Next State, Symbol to add', delta[(qCurrent, currentSymbol, stack[-1] if epsilon == None else epsilon)])
```
- Esta função **mostra o estado atual da simulação**, mas está comentada no código principal.
- Pode ser usada para depuração (debug).

---

### 🔁 Simulador da Máquina

```python
def AFD(machine: Machine, string: list):
```
- Simula a execução da máquina `machine` com a string fornecida (como lista de caracteres).

```python
    qCurrent = machine.q0
    stack = []
    currentSymbol = string.pop(0)
```
- Começa do estado inicial `q0`, pilha vazia, e lê o primeiro símbolo da string.

```python
    while currentSymbol in machine.sigma:
```
- Enquanto houver símbolos válidos no alfabeto...

---

### 🔄 Bloco de transições:

```python
        if (qCurrent, epsilon, epsilon) in machine.delta :
```
- Se há uma transição `ε, ε` (sem ler da string e sem depender da pilha), ela é usada.

```python
            qCurrent, stackSymbol = machine.delta[(qCurrent, epsilon, epsilon)]
            addToStack(stack, stackSymbol)
```
- Transição aplicada: novo estado + empilha símbolo (se não for ε).

---

```python
        elif (qCurrent, currentSymbol, epsilon) in machine.delta:
```
- Se há uma transição que lê o símbolo **mas não depende da pilha**, aplica.

```python
            qCurrent, stackSymbol = machine.delta[(qCurrent, currentSymbol, epsilon)]
            addToStack(stack, stackSymbol)
            currentSymbol = string.pop(0) if string else epsilon
```
- Realiza a transição e avança na string.

---

```python
        elif (qCurrent, currentSymbol, stack[-1] if len(stack) > 0 else epsilon) in machine.delta:
```
- Se a transição depende do topo da pilha...

```python
            qCurrent, stackSymbol = machine.delta[(qCurrent, currentSymbol, stack[-1])]
            removeFromStack(stack, stack[-1])
            addToStack(stack, stackSymbol)
            currentSymbol = string.pop(0) if string else epsilon
```
- Realiza desempilhamento + empilhamento e avança a leitura.

---

```python
        else:
            break
```
- Se nenhuma transição for possível, a execução termina.

---

### ✅ Verificação de aceitação

```python
    if(len(string) > 0): return False
    return qCurrent in machine.f
```
- A cadeia é aceita se **toda a entrada foi consumida** e o **estado atual é final**.

---

### 🏗️ Construção da Máquina

```python
def getMachine():
    q = {'q0', 'q1','q2', 'q3', 'q4', 'q5'}
    sigma = { epsilon, 'A', 'C', 'G', 'T', '#'}
```
- Define estados e alfabeto.

```python
    delta = {
        ('q0', ε, ε): ['q1', '$'],
        ('q1', 'A', ε): ['q3', ε],
        ('q1', 'C', ε): ['q2', ε],
        ('q1', 'G', ε): ['q2', ε],
        ('q1', 'T', ε): ['q4', ε],
        ...
    }
```
- `delta`: regras de transição.
  - Exemplo: `('q1', 'A', ε) → ('q3', ε)` significa que ao ler 'A', vai para `q3` e não mexe na pilha.

```python
    q0 = 'q0'
    f = {'q5'}
    return Machine(q, sigma, delta, q0, f)
```
- Retorna uma máquina configurada.

---

### ▶️ Função Principal

```python
def main ():
    machine = getMachine()
```
- Obtém a máquina configurada.

```python
    while True:
        string = input("Enter a string: ")

        if string == '/exit;': break
```
- Loop principal: recebe entrada do usuário. Para com `/exit;`.

```python
        try: 
            if AFD(machine, list(string)):
                print("Accepted")
            else:
                print("Rejected") 
        except:
            print("Rejected")
```
- Executa a máquina com a entrada e mostra se foi aceita ou rejeitada.
- Usa `try/except` para evitar travamento se a cadeia for inválida.

---

## 📌 Observações

- O autômato pode ser usado para simular linguagens como:
  - Palíndromos
  - Padrões genéticos
  - Balanceamento de símbolos
- Transições `ε` são **muito poderosas** e permitem modificar a pilha sem consumir a entrada.
