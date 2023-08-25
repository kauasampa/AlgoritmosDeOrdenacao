import random
import time

def bubbleSort(arrayg):
    comparisons = 0  # Contador de comparações
    start_time = time.time()  # Tempo inicial
    array = arrayg
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            comparisons += 1  # Atualiza o contador de comparações
    end_time = time.time()  # Tempo final
    execution_time = (end_time - start_time) * 1000  # Tempo de execução em milissegundos
    return array, execution_time, comparisons

def insertionSort(arrayg):
    comparisons = 0  # Contador de comparações
    start_time = time.time()  # Tempo inicial
    for J in range(1, len(arrayg)):
        key = arrayg[J]
        I = J - 1
        while I >= 0 and arrayg[I] > key:
            arrayg[I + 1] = arrayg[I]
            I -= 1
            comparisons += 1  # Atualiza o contador de comparações
        arrayg[I + 1] = key
    end_time = time.time()  # Tempo final
    execution_time = (end_time - start_time) * 1000  # Tempo de execução em milissegundos
    return arrayg, execution_time, comparisons

import time

def mergeSort(A):
    comparisons = 0  # Contador de comparações
    
    def merge(A, p, q, u):
        nonlocal comparisons
        comparisons += (u - p) * 2  # Atualiza o contador de comparações

    def mergeSortIntern(A, p, u):
        nonlocal comparisons
        if p < u:
            q = (p + u) // 2
            mergeSortIntern(A, p, q)
            mergeSortIntern(A, q + 1, u)
            merge(A, p, q, u)

    start_time = time.time()  # Tempo inicial
    mergeSortIntern(A, 0, len(A) - 1)
    end_time = time.time()  # Tempo final
    execution_time = (end_time - start_time) * 1000  # Tempo de execução em milissegundos
    return A, execution_time, comparisons


def heapSort(A):
    comparisons = 0  # Contador de comparações
    
    def constroiHeapMax(A):
        nonlocal comparisons
        tamHeap = len(A) - 1
        for i in range(len(A) // 2, -1, -1):
            refazHeapMax(A, i, tamHeap)

    def refazHeapMax(A, i, tamHeap):
        nonlocal comparisons
        esq = 2 * i + 1
        dir = 2 * i + 2
        maior = i
        if esq <= tamHeap and A[esq] > A[maior]:
            maior = esq
        if dir <= tamHeap and A[dir] > A[maior]:
            maior = dir
        if maior != i:
            A[i], A[maior] = A[maior], A[i]
            refazHeapMax(A, maior, tamHeap)
            comparisons += 1  # Atualiza o contador de comparações

    def heapSortIntern(A):
        nonlocal comparisons
        start_time = time.time()  # Tempo inicial
        constroiHeapMax(A)
        tamHeap = len(A) - 1
        for i in range(len(A) - 1, 0, -1):
            A[0], A[i] = A[i], A[0]
            tamHeap -= 1
            refazHeapMax(A, 0, tamHeap)
            comparisons += 1  # Atualiza o contador de comparações
        end_time = time.time()  # Tempo final
        execution_time = (end_time - start_time) * 1000  # Tempo de execução em milissegundos
        return A, execution_time, comparisons

    return heapSortIntern(A)

def quickSort(arr):
    comparisons = 0  # Contador de comparações
    
    def partition(arr, low, high):
        nonlocal comparisons
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                comparisons += 1  # Atualiza o contador de comparações

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    start_time = time.time()  # Tempo inicial
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    end_time = time.time()  # Tempo final
    execution_time = (end_time - start_time) * 1000  # Tempo de execução em milissegundos

    return arr, execution_time, comparisons

def hybridSort(A):
    comparisons = 0  # Contador de comparações

    def merge(A, p, q, u):
        nonlocal comparisons
        mergeSort(A[p:u+1])
        comparisons += (u - p) * 2  # Atualiza o contador de comparações

    def hybridSortIntern(A, p, u):
        nonlocal comparisons
        if u - p <= 10:  # Limite para alternar para o Insertion Sort
            insertionSort(A[p:u+1])
            comparisons += (u - p) * 2  # Atualiza o contador de comparações
        else:
            q = (p + u) // 2
            hybridSortIntern(A, p, q)
            hybridSortIntern(A, q + 1, u)
            merge(A, p, q, u)

    start_time = time.time()  # Tempo inicial
    hybridSortIntern(A, 0, len(A) - 1)
    end_time = time.time()  # Tempo final
    execution_time = (end_time - start_time) * 1000  # Tempo de execução em milissegundos

    return A, execution_time, comparisons


def criarVetorCrescente(length):
    ListaCrescente = list(range(length))
    return ListaCrescente

def criarVetorDecrescente(length):
    ListaDecrescente = list(range(length, 0, -1))
    return ListaDecrescente

def criarVetorAleatorio(length):
    ListaAleatoria = [random.randint(0, length) for _ in range(length)]
    return ListaAleatoria

def printMainMenuAlgorithm():
    print('Digite a opção desejada:\n1-Executar BubbleSort\n2-Executar InsertionSort\n3-Executar MergeSort\n4-Executar HeapSort\n5-Executar QuickSort\n6-Executar HybridSort(Merge+Insertion).')

def MainMenuOrder():
    change = int(input('Digite a opção desejada:\n1-Criar vetor crescente\n2-Criar vetor decrescente\n3-Criar vetor aleatório\n0-Sair\n: '))
    if change == 1:
        length = int(input('informe o tamanho do vetor: '))
        return criarVetorCrescente(length)
    elif change == 2:
        length = int(input('informe o tamanho do vetor: '))
        return criarVetorDecrescente(length)
    elif change == 3:
        length = int(input('informe o tamanho do vetor: '))
        return criarVetorAleatorio(length)
    else:
        print('1opção não encontrada, vetor está vazio, digite novamente...')

def printItensDoVetor(vetor):
    resultado = '[' + ', '.join(map(str, vetor)) + ']'
    print(resultado)

x = 0
while x == 0:
    VetorOrdenado = []
    VetorDesordenado = []
    printMainMenuAlgorithm()
    changeAlgorithm = int(input(": "))
    VetorDesordenado = MainMenuOrder()

    if changeAlgorithm == 1:
        VetorOrdenado, execution_time, comparacoes = bubbleSort(VetorDesordenado)
    elif changeAlgorithm == 2:
        VetorOrdenado, execution_time, comparacoes = insertionSort(VetorDesordenado)
    elif changeAlgorithm == 3:
        VetorOrdenado, execution_time, comparacoes = mergeSort(VetorDesordenado)
    elif changeAlgorithm == 4:
        VetorOrdenado, execution_time, comparacoes = heapSort(VetorDesordenado)
    elif changeAlgorithm == 5:
        VetorOrdenado, execution_time, comparacoes = quickSort(VetorDesordenado)
    elif changeAlgorithm == 6:
        VetorOrdenado, execution_time, comparacoes = hybridSort(VetorDesordenado)
    else:
        print('opção não encontrada, vetor está vazio, digite novamente...')
        VetorOrdenado = []

    # printItensDoVetor(VetorOrdenado)
    print("Tempo de execução:", format(execution_time, '.6f'), "milissegundos")
    print("Quantidade de comparações:", format(comparacoes))

    x = int(input('Deseja sair da aplicação? (0-não, 1-sim): '))