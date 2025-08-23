#casting (mengubah type data) 


##INTEGER
print("=================INTEGER====================")
data_int = 9;
print("data = ", data_int, ",type = ",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai = 0
print("data = ", data_float, ",type = ",type(data_float))
print("data = ", data_str,  ",type = ",type(data_str))
print("data = ", data_bool, ",type = ",type(data_bool))


print("")
##FLOAT
print("=================FLOAT====================")
data_float = 10.5;
print("data = ", data_float, ",type = ",type(data_float))

data_int = int(data_float) #akan dibulatkan kebawah, misal value 9.9 maka hasilnya adalah 9 bukan 10
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai = 0
print("data = ", data_int, ",type = ",type(data_int))
print("data = ", data_str,  ",type = ",type(data_str))
print("data = ", data_bool, ",type = ",type(data_bool))


print("")
##BOOLEAN
print("=================BOOLEAN====================")
data_bool = True;
print("data = ", data_bool, ",type = ",type(data_bool))

data_int = int(data_bool) #akan dibulatkan kebawah, misal value 9.9 maka hasilnya adalah 9 bukan 10
data_str = str(data_bool)
data_float = float(data_bool) #akan false jika nilai = 0
print("data = ", data_int, ",type = ",type(data_int))
print("data = ", data_str,  ",type = ",type(data_str))
print("data = ", data_float, ",type = ",type(data_float))


print("")
##STRING
print("=================STRING====================")
data_str = "hallo"
print("data = ", data_str, ",type = ",type(data_str))

#data_int = int(data_str) #akan dibulatkan kebawah, misal value 9.9 maka hasilnya adalah 9 bukan 10
#data_float = float(data_str) #akan false jika nilai = 0
data_bool = bool(data_str)
#print("data = ", data_int, ",type = ",type(data_int))
#print("data = ", data_float, ",type = ",type(data_float))
print("data = ", data_bool,  ",type = ",type(data_bool))
