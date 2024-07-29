n=1212
sumofdigits=0
while (n>0):
        digit= n%10
sumofdigits+=digit
n=n/n/10
print("the sum of digits :",sumofdigits)
