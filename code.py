import random
import enchant 
from termcolor import colored
import re
file=r"C:\Users\Acer\Downloads\english2\english2.txt"
  
print("     WORDLE- word hurdle   ")
print("Green = same place; same alphabet")
print("Red = alphabet is guessed correctly; place is wrong")

cnt=0  
# Open the file in read mode
with open(file, "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    # print random string
    count = 0
    while (count == 0): 
        x=random.choice(words)
        if len(x)==5:
            print(x)
            break
        else:
            continue 
# w="....."
# e="....."
# f=""
# g="" 
for i in range(0,5):
    s=str(input())
    cnt=cnt+1
    dict = enchant.Dict("en_US")
    chk=dict.check(s)
    if chk==True:
        if s==x:
            print("Yay!You guessed it right in just "+str(cnt)+" attempts.")
            break
        else:
            for i,j in zip(range(len(s)),range(len(x))):
                if s[i]==x[j]:
                    if i==j:
                        position = i
                        new_character = (colored(s[i], 'green', attrs=['underline']))
                        #w= s[:position] + new_character + s[position+1:]
                        #f=re.sub(w[i],new_character,w)
                        print(new_character,end="")
                elif s[i] in x: 
                    position = i
                    new_character = (colored(s[i], 'red', attrs=['underline']))
                    e= s[:position] + new_character + s[position+1:]
                    #g=re.sub(e[i],new_character,e)
                    print(new_character,end="") 
                #elif s[i] not in x: 
           
            
                  
            
    else:
        print("Is this even a word?")
if cnt==5: 
    if s!=x:
        print("Oho " + x + " was the word:(")
        print("It's okay try again!!")

                    
                
        
        
                
            
    
        
