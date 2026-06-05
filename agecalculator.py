from datetime import date

#BUAT NGITUNG UMURNYA JIR
def calculate_age(day, month, year):
    today = date.today()
    birthdate = date(year, month, day)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

try:
    #BUAT LU MASUKIN TANGGAL, BULAN, TAHUNNYA
    day = input('Enter Day:')
    month = input('Enter Month:')
    year = input('Enter Year:')

    #MANGGIL FUNGSI DI ATAS TERUS DICONVERT DEH JADI INI
    age_result = calculate_age(int(day), int(month), int(year))
    #HASIL PRINTNYA KETAHUAN UMURNYA DAN MUNGKIN LU AKAN SADAR HIDUP LU GAK LAMA LAGI
    print(f'You are {age_result} years old')

#INI KALO LU SALAH MASUKIN TANGGAL BULAN TAHUNNYA
except:
    print(f'Wrong dipshit, thats not how u doin it')