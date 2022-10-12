# Each number is seperated by ",".
# Example:
# input is: 1,2,3,4,5,6
given_list=list(map(int,input().split(",")))
print("fattest value in wallet is",max(given_list))
print("skinniest value in wallet is",min(given_list))
print("Total value of the given wallet is: ",sum(given_list))
print("The total value of these wallets in dimes is: ",sum(given_list)*10)