"""
print("Hello, Django girls!")

if 3 > 2:
	print('hurrra!')




name = 'Sonja' #test
if name == 'Ola':
    print('Hej Ola!')
elif name == 'Sonja':
    print('Hej Sonja!')
else:
    print('Hej anonimie!')
"""
"""
def hi():
    print('Hej!')
    print('Jak się masz?')
hi()


def helo(imie):
	if imie == 'Ola':
		print('Hej Ola')
	elif imie == 'Sonja':
		print('Hej Sonja')
	else:
		print('Hej nieznajoma')

helo('Ola')
"""

def hi(imie):
    print('Witaj ' + kwiatki + '!')

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
for kwiatki in dziewczyny:
    hi(kwiatki)
    print('Kolejna dziewczyna')
