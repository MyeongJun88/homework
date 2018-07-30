star= "*"
blank = " "

for n in range(1,6):
   if n == 1 or n==5:
    print((blank*(5-n)+star)
   else:
    print(blank*(5-n)+star + blank(2*n-1) + star)
