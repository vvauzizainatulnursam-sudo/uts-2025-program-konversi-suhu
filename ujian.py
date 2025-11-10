def konversi_suhu(celsius):
    # Konversi suhu ke Fahrenheit, Kelvin, dan Reamur
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    reamur = celsius * 4/5
    return fahrenheit, kelvin, reamur

print("Program Konversi Suhu Multiple")
print("Input suhu dalam Celcius, program akan konversi ke Fahrenheit, Kelvin, dan Reamur")

while True:
    try:
        suhu_c = float(input("\nMasukkan suhu dalam Celcius: "))
    except ValueError:
        print("Input tidak valid, masukkan angka.")
        continue

    # For loop untuk menampilkan suhu dan hasil konversi dalam tabel
    satuan = ["Celcius", "Fahrenheit", "Kelvin", "Reamur"]
    hasil = [suhu_c]
    f, k, r = konversi_suhu(suhu_c)
    hasil.extend([f, k, r])

    print("\nTabel Konversi Suhu")
    print("{:<12} | {:>10}".format("Satuan", "Nilai"))
    print("-" * 25)
    for i in range(len(satuan)):
        print("{:<12} | {:>10.2f}".format(satuan[i], hasil[i]))

    # Do-while dengan cara tanya ke user apakah mau ulangi
    lagi = input("\nApakah ingin konversi suhu lagi? (y/n): ").lower()
    if lagi != 'y':
        print("Terima kasih sudah menggunakan program ini.")
        break
