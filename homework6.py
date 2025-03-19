# дз №1
def binary_search(A, Val):
    N = len(A)
    ResultOk = False
    First = 0
    Last = N - 1
    Pos = -1

    while First <= Last:
        Middle = (First + Last) // 2

        if Val == A[Middle]:
            ResultOk = True
            Pos = Middle
            break
        elif Val > A[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk:
        print(f"элемент найден на позиции {Pos}")
    else:
        print("элемент не найден :(")


A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
binary_search(A, 28)

# дз №2
def bubble_sort(A):
    N = len(A)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


A = [9, 3, 7, 1, 13, 11, 5]
sorted_A = bubble_sort(A)
print(sorted_A)