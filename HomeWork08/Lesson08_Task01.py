A = str(input("Введите буквы или слова: "))

print("Строка \'%s\' имеет длину %d сиволов." % (A, len(A)))

subs_set = set()
for i in range(len(A)):
    for j in range(len(A)-1 if i == 0 else len(A), i, -1):
        subs_set.add(hash(A[i:j]))
print("Количество различных подстрок в этой строке:", len(subs_set))