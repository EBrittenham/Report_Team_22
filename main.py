# group 22: Mason Cervi, Emma Brittenham
# this is Emma's code
def menu():
	print('Menu')
	print('1. Encode')
	print('2. Decode')
	print('3. Quit')


def encode(password):
	string = ''
	for i in password:
		new = (int(i) + 3) % 10
		string += str(new)
	return string

def decode(password):
	string = ''
	for i in password:
		new = (int(i) + 7) % 10
		string += str(new)
	return string

def main():
	choice = 0
	while choice != 3:
		menu()
		choice = int(input('Please enter an option: '))
		if choice == 1:
			password = input('Please enter your password to encode: ')
			encoded_pass = encode(password)
			print('Your password has been encoded and stored!\n')
			continue
		elif choice == 2:
			print(f'The encoded password is {encoded_pass}, the original password is {decode(encoded_pass)}.\n')
			continue


if __name__ == '__main__':
	main()
