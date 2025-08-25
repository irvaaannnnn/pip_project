# # mengkonversi suhu

print("\n=========PROGRAM KONVERSI SUHU=========\n")

celcius = float(input("Masukan suhu celcius = "))
print("Suhu celcius adalah = ",celcius)

reamur = (4/5) * celcius
print("Suhu reamur nya adalah = ",reamur)

fahrenheit = ((9/5) * celcius) + 32
print("Suhu fahrenheit nya adalah = ",fahrenheit)

kelvin = celcius + 273
print("Suhu kelvin nya adalah = ", kelvin)

print("===========================================")
#Latihan dari kelvin ke fahrenheit
k = float(input("INPUT KELVIN = ")) #10
c = k - 273.15 #mendapatkan celcius 283
f = ((9/5) * c) +32 
print("Jadi", k, "kelvin, sama dengan", f,"fahrenheit") 

#Latihan dari fahrenheit ke kelvin
f = float(input("INPUT FAHRENHEIT = "))
c = (f - 32) * 5/9
k = c + 273.15
print("Jadi", f, "fahrenheit, sama dengan", k,"Kelvin")

#Latohan dari reamur ke kelvin
re = float(input("INPUT REAMUR = "))
ke = (5/4) * re + 273
print(re, "adalah", ke, "kelvin")