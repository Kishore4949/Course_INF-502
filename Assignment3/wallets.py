# Each number is seperated by ",".
# Example:
# input is: 1,2,3,4,5,6
def fattest(list1):
    return max(list1)

def skinniest(list1):
    return min(list1)

def totalvalue(list1):
    return sum(list1)

def dimes(list1):
    return sum(list1)*10


given_list=list(map(int,input().split(",")))
print("fattest value in wallet is",fattest(given_list))
print("skinniest value in wallet is",skinniest(given_list))
print("Total value of the given wallet is: ",sum(given_list))
print("The total value of these wallets in dimes is: ",sum(given_list)*10)