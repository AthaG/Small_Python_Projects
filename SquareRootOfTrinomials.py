# Square-Root of Trinomials
import math


print("Έχουμε ένα τριώνυμο ax²+bx+c. Δώστε μία θετική ή αρνητική τιμή σε κάθε σταθερά!")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

D= b**2-4*a*c

print("Η Διακρίνουσα ειναι: " + str(D))

if D>0:
    x1=(-b+math.sqrt(D))/(2*a)
    print("Η πρώτη ρίζα ειναι: " + str(x1))
    x2=(-b-math.sqrt(D))/(2*a)
    print("Η δεύτερη ρίζα ειναι: " + str(x2))
elif D==0:
    x=(-(b/(2*a)))
    print("Η διπλή ρίζα ειναι: " + str(x))
elif D<0: # else:
    print("Δεν υπάρχει ρίζα")
