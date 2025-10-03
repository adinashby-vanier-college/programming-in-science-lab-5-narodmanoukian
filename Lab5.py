# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    
    result=""
    if n >= 1:
        for i in range(n):
            result += "*"
    result += "\n"
    for i in range(n-2):
        result += "*"
        for i in range(n-2):
            result += " "
        result += "*\n"
    if n > 1:
        for i in range(n):
            result +="*"
    return result.rstrip()

              
# 1
# 12
# 123
# 1234
def number_pattern(n):
    result=""

    for i in range (1, n + 1):
        for j in range (1, i + 1):
            result += str(j) 
        result += "\n"
    return result.rstrip()

print(number_pattern(5))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
  
    result =0
    i = 1
    while i <= n:
        result += i
        i += 1 

    
    return result




# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    
    result = ""
    stars=1
    spaces = n - 1

    for i in range(n):
        count = 0
        while count < spaces:
            result += " "
            count +=1


        count = 0
        while count < stars:
            result += "*"
            count += 1

        result +="\n"
        
        stars +=2
        spaces -= 1



    return result.rstrip()