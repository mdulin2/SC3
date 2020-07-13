
def get_lst():
	word_dict = {}
	word_lst_fd = open("words.txt", "r")
	index = 0
	for line in word_lst_fd: 
		line = line.replace('\n','') 
		line = line.replace(' ', '') 
		word_dict[line] = index
		index += 1

	return word_dict

def decode(passphrase): 
	word_lst = get_lst()

	index = 0
	my_key = 0
	passphrase = passphrase.split("-")
	for key in passphrase:
		print key
		my_key = word_lst[key] * 32 ** index + my_key
		index += 1
		
	return my_key
		
phrase = "hallucinate-cat-victory-people-barley-giddy-kangaroo-yank"
print decode(phrase) 
