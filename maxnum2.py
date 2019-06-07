test_list1 = []
test_list2 = []

n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input())
    test_list1.append(b)

print("Second Array")
for i in range(1,n+1):
    b=int(input())
    test_list2.append(b)

max_all = max(test_list1 + test_list2)

print("The maximum of both lists is : " + str(max_all))