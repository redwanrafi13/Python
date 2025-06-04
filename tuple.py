def palindrom(r):
    start=0
    end= len(r) - 1
    
    while (start > end):
        if (r[start] != r[end]):
            return("the tuple is not palindrom" )
        start= start + 1
        end= end - 1
    return("the tuple is palindrome")

d = (3,3,2,7,9,1,6)
print(palindrom(d))