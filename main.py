"""
Program Integrasi Numerik Menggunakan Metode Rectangle Rule untuk Menghitung Luas Daerah Tidak Beraturan
"""
print("--Program Metode Rectangle Rule untuk Menghitung Luas Daerah Tidak Beraturan--")
print("==============================================================================")
print("Masukkan rentang daerah yang akan dihitung!")
bottom = float(input("Titik batas bawah: "))
top = float(input("Titik batas atas: "))
div = int(input("Berapa pias yang diinginkan: "))

longArea = (top - bottom)/div
datax = []
datafx = []
datax.insert(0, bottom)
buff = float(input("Masukkan nilai f(x0): "))
datafx.insert(0, buff)
for i in range(0, div):
    datax.insert(i + 1, datax[i] + longArea)
    buff = float(input("Masukkan nilai f(x%d): " %(i+1)))
    datafx.insert(i + 1, buff)

print("Data x0 hingga x%d:" %div, datax)
print("Data f(x0) hingga f(x%d):" %div, datafx)

subArea = 0
for i in range(0, div + 1):
    if i == 0:
        subArea += datafx[0]
    elif i == div:
        subArea += datafx[div]
    else:
        subArea += 2*datafx[i]

luasArea = (longArea*subArea)/2
print("Luas Daerah: %f cm^2" %luasArea)

fa = (datafx[1] - datafx[0])/(datax[1] - datax[0])
fb = (datafx[div] - datafx[div-1])/(datax[div] - datax[div-1])
Err = -((longArea**2)*(fb - fa)/12)

print("Error: %f cm^2" %Err)


