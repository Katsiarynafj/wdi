import random


file = 'C:\\Users\\Kasia\\Documents\\python learning\\slownik10k.txt'

def wcztywanie_pliku(file):
	with open(file, encoding='utf-8') as f:
	    tekst = f.read().splitlines()
	return tekst

# print(len(wcztywanie_pliku(file)))


def anagram_dictionary(file):
	tekst = wcztywanie_pliku(file)
	anag_dict = {}
	length = len(tekst)
	for i in range(length): 
		a = " ".join(sorted(tekst[i]))
		if a not in anag_dict:
			anag_dict[a] = [tekst[i]] 
		elif a in anag_dict:
			anag_dict[a].append(tekst[i])
	for a in list(anag_dict.keys()):
	    if len(anag_dict[a]) < 2:
	        anag_dict.pop(a)

	return anag_dict

# print(anagram_dictionary(file))

def wybór_słowa(dict):
	keys = anagram_dictionary(file).keys()
	# print(keys)
	return random.choice(list(keys))

wybór_słowa(file)

def gra(file):
	słowo = wybór_słowa(file)
	a = anagram_dictionary(file)[słowo]
	print(a)
	print ("Twój zestaw liter:", słowo.upper())
	inp = input("pierwsza próba: ")
	if inp in a:
		# a.remove(inp)
		print("congrats")
		print("posostało ci:", len(a))
	else:
		print("boooo")
	print(a)


gra(file)

