# User menginputkan data

#apapun yg diinputkan pasti isi nya sting
data = input("Input your data str = ")

#print("Data =", data, "Type =",type(data))

#===============================
# jika ingin mengambil int ,maka
number = int(input("Input your number int ="))
#print("Data =",number, "Type =",type(number))


number_float = float(input("Input your number_float float ="))
#print("Data =",number_float, "Type =",type(number_float))


#================================
#boolean / binner
biner = bool(int(input("Input your binner = ")))
print("Hasil adalah..............")
print("Data = ", data,"Type = ",type(data) , 
      "\nData = ", number,"Type = ",type(number),
      "\nData = ", number_float,"Type = ",type(number_float),
      "\nData = ", biner,"Type = ",type(biner))
