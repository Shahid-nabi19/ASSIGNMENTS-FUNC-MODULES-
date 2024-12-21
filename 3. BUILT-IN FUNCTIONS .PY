#  USING LEN()

def longest_word(words):
    longest = max(words, key=len)
    return longest, len(longest)
result = longest_word(["apple", "grapes", "banana", "cherry","pineapple"])
print(result)  


# USING TYPE()

def type_checker(value):
    return type(value)
print(type_checker(16))         
print(type_checker("SHAHID")) 


# USING RANGE ()

def sum_of_evens(n):
    sum=0
    for i in range(0,n+1):
        if i%2==0:
            sum=sum+i
        i+=1
    return sum
print(sum_of_evens(10))
