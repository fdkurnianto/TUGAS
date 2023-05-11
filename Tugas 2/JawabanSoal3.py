if __name__ == '__main__':
# Tulis jawaban
angka = input('Enter a starting number (greater than 0) or QUIT:')
 
n = int(angka)

while n != 1:
    if n % 2 == 0:  
        n = n // 2
    else:  
        n = 3 * n + 1
    print(', ' + str(n))
    