def second_largest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()
  return  uniq_items[-2]

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input())
    a.append(b)
print(second_largest(a))