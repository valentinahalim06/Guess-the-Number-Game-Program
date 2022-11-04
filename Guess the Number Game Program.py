import random

number = random.randint(0, 100) #untuk menentukan batas angka dari 0 - 100

print ('======================')
print ('    GAME TEBAK ANGKA    ')
print ('Tebak angkanya sampai benar!')
print ('======================')

attempt = 1 #menunjukkan kesempatan menebak mulai dari 1

while attempt != 0 :

    tebakan = int(input('Masukkan angka :'))
    if attempt < 10 :
        if tebakan == number: #jika tebakannya sesuai
            print(f'Angka anda benar setelah menebak', {attempt}, 'kali')
            break #program berhenti dijalankan karena tebakan sudah benar
        elif tebakan > number: #jika tebakan yang dimasukkan terlaku besar nilainya
            print('Angka terlalu besar. Gunakan kesempatanmu lagi!')
            attempt += 1
            continue #jika kesempatan masih ada maka pemain akan diminta kembali ke entri tebakan
        else:
            print('Angka terlalu kecil. Coba tebak lagi!')
            attempt += 1
    if attempt == 10 :
        print('Anda kurang beruntung. Better luck next time!')
        break #program berhenti dijalankan karena kesempatan menebak sudah 10 kali dan masih salah

