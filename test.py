no_of_sat = input()
list1 = list(no_of_sat)
k = input()
even = []
even.append(k)
count = 0
for i in range(len(no_of_sat)):
    if int(no_of_sat[i])%2 != 0:
        list1[i] = even[count]
        print(no_of_sat[i])
        count += 1
    else:
        even.append(no_of_sat[i])
print("".join(list1))