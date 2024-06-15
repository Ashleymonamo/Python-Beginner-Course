#RegEx 
import re
str="The river is leading to the main dam which is located in Lepelle,Groblesdal"
answer=re.findall("is",str)
print(answer)

if(answer):
    print("The word 'is' was found atleast once in the sentence")
else:
   print("Not found")       


   