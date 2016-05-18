sum = 0

for a in range(1, 1000) :
    if a%3 == 0 :
        print ("There is %d!!" %a)
        sum = sum + a
        print ("Now sum is %d" %sum)
    elif a%5 == 0 :
        print( "There is %d!!" %a)
        sum = sum + a
        print ("Now sum is %d" %sum)

print ("Finally, Sum is %d" %sum)