import random
# kod  aleyatwa alfabetik san repetisyon
alfa1="abcdefghijklmnopqrstuvwxyz"

def aleyatwa(alfa,nomb):
    return "".join(random.sample(alfa,nomb))


kod1=aleyatwa(alfa1,10)
print(kod1)
print(len(kod1))


#  kod aleyatwa alfanimerik san repetisyon

alfa2="abcdefghijklmnopqrstuvwxyz1234567890"

def aleyatwa(alfa,nomb):
    return "".join(random.sample(alfa,nomb))


kod2=aleyatwa(alfa2,36)
print(kod2)
print(len(kod2))