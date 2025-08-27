#Operasi komparasi (perbandingan)
#Setiap hasil nya mutlak binner(boolean) (True/False)
# >, <, >=, <=, ==, !=, is, isnot

a = 5
b = 9

print("================================")
print("== Berikut variabel dan value ==")
print("================================")
print("a = ",(a))
print("b = ",(b))

# > 
print("===== besar dari (>) ===== ")
hasil = a > b
print("hasil a > b = ",hasil)
hasil = a > 10
print("hasil a > 10 = ",hasil)
print("")

# <
print("====== kurang dari (<) =====")
kudar = a < b
print("hasil a < b =", kudar)
kudar = a < -11
print("hasil a < -11 =", kudar)
print("")

# >= 
print("======= besar sama dari (>=) =====")
hasil = a >= b
print("hasil a >= b = ",hasil)
hasil = a >= 5
print("hasil a >= 5 = ",hasil)
print("")

# <= 
print("======= kurang sama dari (<=) =====")
hasil = a <= b
print("hasil a <= b = ",hasil)
hasil = a <= 5
print("hasil a <= 5 = ",hasil)
print("")

# == 
print("======= kurang sama dari (==) =====")
hasil = a == b
print("hasil a == b = ",hasil)
hasil = a == 5
print("hasil a == 5 = ",hasil)
print("")

# != 
print("======= kurang sama dari (!=) =====")
hasil = a != b
print("hasil a != b = ",hasil)
hasil = a != 5
print("hasil a != 5 = ",hasil)
print("")

# is (komparasi object identity)
print("======= object identity (is)")
x = 5
y = 10
print("nilai x = ",x, ",id = ",hex(id(x)))
print("nilai x = ",y, ",id = ",hex(id(y)))
hasil = x is y
# hasil = x is 5
# is jangan pake literal , literal seperti kode diatas
# untuk literal gunakan ==
# literal adalah nilai yg langsung ditulis
# sementara is / is not digunakan untuk membandingkan variabel
print("hasil nya adalah = ", hasil)
print("")

# is not (komparasi object identity)
print("======= object identity (is not)")
x = 5
y = 10
print("nilai x = ",x, ",id = ",hex(id(x)))
print("nilai x = ",y, ",id = ",hex(id(y)))
hasil = x is not y
print("hasil nya adalah = ", hasil)