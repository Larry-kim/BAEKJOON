test = [5, 5, 2, 3, 4, 1]

for i in range(len(test) - 1):
    if test[i] > test[i + 1]:
        test[i], test[i + 1] = test[i + 1], test[i]
        for s in range(i, 0, -1):
            if test[s] < test[s - 1]:
                test[s], test[s - 1] = test[s - 1], test[s]

#result = list(set(test)) 
# print(result)로 할 시 요소의 중복을 제거할 수 있음
print(test)
