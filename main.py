# Write a program to remove all vowels from a given string
i=input()
c=""
vovel=["a","e","i","o","u","A","E","I","O","U"]
for x in i:
  
    if x not in vovel:
      c=c+x


print(c)

      