print ("Hello World..")
print("11 500 001 504 = 1504 ans sur Terre")
date=int(input("Choisir la date depuis une horloge terrienne : "))
print (date)

arc1=200000000/26
arc2=arc1/26
arc3=arc2/26
arc4=arc3/26
arc5=arc4/26
Alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

nbrtour=int(date/200000000)
reste1 = date%200000000

position1=int(reste1/arc1)
reste2 = reste1%arc1

position2=int(reste2/arc2)
reste3 = reste2%arc2

position3=int(reste3/arc3)
reste4 = reste3%arc3

position4=int(reste4/arc4)
reste5 = reste4%arc4

position5=int(reste5/arc5)
reste6 = reste5%arc5

print(nbrtour ,'.', Alphabet[position1] ,'.', Alphabet[position2] ,'.', Alphabet[position3] ,'.', Alphabet[position4] ,'.', Alphabet[position5])
end=input()