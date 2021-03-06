# Шифр Плейфера
# Принцип работы данного метода шифрования:
# Есть исходное сообщение: HELL
# Если в сообщении есть символ 'J' - заменить его на символ 'I'
# Если в данной сообщении есть рядом стоящие одинаковые символы:
# Между ними поставить символ 'X':
# Получим сообщение HELXL
# Далее разделяем сообщение по 2 символа
# Получим сообщение: HE LX L
# Если сообщение нечётное- добавить в конец символ 'X'
# Получим сообщение: HE LX LX
# Далее создаём какой-либо ключ и заносим его в матрицу алфавита
# (Используем ключ SOMETHING)
# МАТРИЦА:
#   ['S','O','M','E','T']
#	['H','I','N','G','A']
#	['B','C','D','F','K']
#	['L','P','Q','R','U']
#	['V','W','X','Y','Z']
# Если в матрице появляются одинаковые символы:
# Удалять одинаковые символы с конца матрицы
# Далее идёт два способа шифрования:
# 1) Если пара символов находится на одной строке матрицы:
# - Передвинуть индекс значений на +1
# (В слове HELL все символы подчиняются второму способу шифрования)
# 2) Если пара символов находится на разных строках матрицы:
# - Если находятся на разных строках, значит может получится прямоугольник
# - Создать соостветственно этот прямоугольник
# - И поменять значения символов на противоположные углы прямоугольника
# В итоге мы получаем следующее: SG VQ VQ
# Складываем все символы в одну строку и получаем зашифрованное сообщение:
# SGVQVQ

# Открытое сообщение
text = "IAMCRYPTTOANALITICWITHBIGDICK"

# Создание списка
text = [x for x in text]

# Поиск на одинаковые символы
for i in range(1,len(text)):
	
	if text[i] == text[i-1]:
		
		text.insert(i,"X")

# Если символов нечётное количество - прибавить 'X'
if len(text)%2 != 0:
	
	text.append("X")

# Если в текста символ 'J' - заменить на 'I'
for i in range(len(text)):
	
	if text[i] == "J":
		
		text[i] = "I"

# Создание матрицы с ключом 'SOMETHING'
matrix = [
	['S','O','M','E','T'],
	['H','I','N','G','A'],
	['B','C','D','F','K'],
	['L','P','Q','R','U'],
	['V','W','X','Y','Z']
]

# Деление текста по 2 символа
binary = []
k = ""

for i in text:
	
	k += i
	
	if len(k) == 2:
		
		binary.append(k)
		k = ""

print(binary)

# Шифрование
encrypt = ""; switch = 0

# Перебор двойных символов
for i in range(len(binary)):
	
	# k = 0 или k = 1 (Для разделения двойных символов)
	for k in range(2):
		
		# Перебор строк матрицы
		for x in range(len(matrix)):
			
			# Перебор символов в строке
			for y in range(len(matrix[x])):
				
				# Если символ из матрицы равен символу из открытого сообщения
				if matrix[x][y] == binary[i][k]:
					
					# Если 0 и 1 символы открытого сообщения находятся на одной строке в матрице
					if binary[i][0] in matrix[x] and binary[i][1] in matrix[x]:
						
						# Если символ в матрице не равен началу матричной строки
						if matrix[x][y] != matrix[x][-1]:
							
							# То добавить к encrypt значение символа матрицы с отступом +1
							encrypt += matrix[x][y+1]
						# Иначе если символы 0 и 1 находятся на разных строках матрицы
						else:
							# То добавить к encrypt значение символа матрицы с отступом -4
							encrypt += matrix[x][y-4]
					# Иначе если символы 0 и 1 находятся на разных строках матрицы
					else:
						# Перебор строк матрицы
						for a in range(len(matrix)):
							# Перебор символов в строке
							for b in range(len(matrix[a])):
								# Если символ из матрицы равен символу 0 из зашифрованного сообщения
								if matrix[a][b] == binary[i][0]:
									# Создать переменную x0, содержащую координату 0 символа
									x0 = a
								# Если символ из матрицы равен символу 1 из зашифрованного сообщения 
								if matrix[a][b] == binary[i][1]:
									# Создать переменную x1, содержащую координату 1 символа
									x1 = a
						# Если переменная 'switch' равна нулю
						if switch  == 0:
							# Добавить к переменной decrypt координаты значения матрицы x1/y
							encrypt += matrix[x1][y]
							switch  = 1
						# Иначе
						else:
							# Добавить к переменной decrypt координаты значения матрицы x0/y
							encrypt += matrix[x0][y]
							switch  = 0		
# Вывод зашифрованного сообщения на экран				
print("Encrypted message:",encrypt)

# Деление зашифрованного текста по 2 символа
binary = []
k = ""
for i in encrypt:
	k += i
	if len(k) == 2:
		binary.append(k)
		k = ""
print(binary)
# Расшифровка
decrypt = []; switch = 0
# Перебор двойных символов
for i in range(len(binary)):
	# k = 0 или k = 1 (Для разделения двойных символов)
	for k in range(2):
		# Перебор строк матрицы
		for x in range(len(matrix)):
			# Перебор символов в строке
			for y in range(len(matrix[x])):
				# Если символ из матрицы равен символу из зашифрованного сообщения
				if matrix[x][y] == binary[i][k]:
					# Если 0 и 1 символы зашифрованного сообщения находятся на одной строке в матрице
					if binary[i][0] in matrix[x] and binary[i][1] in matrix[x]:
						# Если символ в матрице не равен началу матричной строки
						if matrix[x][y] != matrix[x][0]:
							# То добавить к decrypt значение символа матрицы с отступом -1
							decrypt.append(matrix[x][y-1])
						# Иначе если символ в матрице равен началу матричной строки
						else:
							# То добавить к decrypt значение символа матрицы с отступом +4
							decrypt.append(matrix[x][y+4])
					# Иначе если символы 0 и 1 находятся на разных строках матрицы
					else:
						# Перебор строк матрицы
						for a in range(len(matrix)):
							# Перебор символов в строке
							for b in range(len(matrix[a])):
								# Если символ из матрицы равен символу 0 из зашифрованного сообщения
								if matrix[a][b] == binary[i][0]:
									# Создать переменную x0, содержащую координату 0 символа
									x0 = a
								# Если символ из матрицы равен символу 1 из зашифрованного сообщения 
								if matrix[a][b] == binary[i][1]:
									# Создать переменную x1, содержащую координату 1 символа
									x1 = a
						# Если переменная 'switch' равна нулю
						if switch  == 0:
							# Добавить к переменной decrypt координаты значения матрицы x1/y
							decrypt += matrix[x1][y]
							switch  = 1
						else:
							# Добавить к переменной decrypt координаты значения матрицы x0/y
							decrypt += matrix[x0][y]
							switch  = 0
# Удаление символов 'X'
for i in range(len(decrypt)-1):
	if decrypt[i] == "X":
		if decrypt[i] != decrypt[-1]:
			if decrypt[i-1] == decrypt[i+1]:
				decrypt.remove(decrypt[i])
		else:
			decrypt.remove(decrypt[i])
# Вывод расшифрованного сообщения на экран
print("Decrypted message:","".join(decrypt))