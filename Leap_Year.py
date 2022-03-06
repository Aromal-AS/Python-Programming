startyear = int(input("Enter the first year: "))
endyear = int(input("Enter the last year: "))
for x in range(startyear, endyear):
    if((x % 400 == 0) or (x % 100 != 0) and (x % 4 == 0)):
        print(x)
