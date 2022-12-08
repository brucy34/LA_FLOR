import random
# 3.-kod  aleyatwa alfabetik san repetisyon
alfa1="abcdefghijklmnopqrstuvwxyz"

def aleyatwa1(alfa,nomb):
    return "".join(random.sample(alfa,nomb))


kod1=aleyatwa1(alfa1,10)
print(kod1)
print(len(kod1))


# 4.-kod aleyatwa alfanimerik san repetisyon

alfa2="abcdefghijklmnopqrstuvwxyz1234567890"

def aleyatwa2(alfa,nomb):
    return "".join(random.sample(alfa,nomb))


kod2=aleyatwa2(alfa2,36)
print(kod2)
print(len(kod2))

# 5.-jenere yon SLUG 

alfa3="yon chenn pou fe slug"

def aleyatwa(alfa):
    return "".join(random.sample(alfa,nomb))


kod2=aleyatwa(alfa2,36)
print(kod2)
print(len(kod2))