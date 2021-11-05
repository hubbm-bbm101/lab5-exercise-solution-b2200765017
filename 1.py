N = input("Please Enter a Dial:\n")
sum1 = 0
sum2 = 0
y = 0
for x in range(1,int(N)+1):
    if x % 2 != 0:
        sum1 += x
    elif x % 2 == 0:
        y += 1
        sum2 += x
text = "sum of odd numbers : {} \navarage of even numbers : {}".format(sum1, sum2/y)
print(text)