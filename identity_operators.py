#package for command line variables
import sys

def check(n1,n2):
    if n1 is not n2:
        output="Hooray"
    else:
        output="Oops, Sorry" 
    return output  

#Uses command line variables
n1=sys.argv[1]   
n2=sys.argv[2]
results=check(n1,n2)
print(results)
#  result=  n1 is n2 
#  if result is True:
#     print("Horray")
#  else:
#     print("Oops") 
#  return result 

# n1=int(sys.argv[1])
# n2=int(sys.argv[2])  
# output=sys.argv[3]

# output=check(n1,n2)
# print(output)


