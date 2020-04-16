#print("Hello World")
#import para limpiar consola
import os


phrase = "THERE ONCE WAS A MAN NAMED"
character_name = "Jhon Cena"
character_age = "35"
is_male = True

#Para limpiar concola 
os.system ("cls") 

print("\n", phrase.capitalize(),character_name ,",\nhe was" , character_age ,"years old.")

print("He really liked the name" , character_name ,",\nbut didn't like being", character_age ,".")

#Workin with Strings in Python
print("The name", character_name, "has", len(character_name), "letters.")

print("The name", character_name, "has the letter", character_name[0])

print(phrase.index("O"))

print(phrase.replace("THERE ONCE", "ONCE THERE"))

#Working with  Numbers in Python
my_num = 2

print(my_num + my_num)

print(2 * 2)
print(2 / 2)
print(2 - 2)
print(10 % 3)

print(2 * (5 + 5))
