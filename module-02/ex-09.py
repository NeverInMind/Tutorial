first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
if first >= second:
    gcd = first
else:
    gcd = second
while first % gcd  or second % gcd :
    gcd -= 1 
    