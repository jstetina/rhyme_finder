import sys

path_to_dictionary = "dictionary.txt"
TEST_WORD = ""
dictionary = open(path_to_dictionary)


try:
	TEST_WORD = sys.argv[1]
except:
	if TEST_WORD == "":
		print("you did not put in a word")
		print("correct syntax> python rhyme_finder.py [word] [first X words]")
		quit()

def get_word_count_par(WORD_LIST):
	first_x_words = 0
	try:
		first_x_words = int(sys.argv[2])
	except:
		first_x_words = len(WORD_LIST)
	return first_x_words

def get_word_endings(INPUT_WORD):
	word_endings_list = list()
	for word in range(1,len(INPUT_WORD)):
		string_append = ""
		for letter_index in range(word,len(INPUT_WORD)):
			string_append += INPUT_WORD[letter_index]
		word_endings_list.append(string_append)
	return word_endings_list

def find_words(WORD_ENDINGS_LIST):
	output_list = list()
	for word_ending in WORD_ENDINGS_LIST:
		for word in dictionary:
			word = word.rstrip()
			if word.endswith(word_ending):
				output_list.append(word)
	return output_list

word_endings = get_word_endings(TEST_WORD)
word_list = find_words(word_endings)
print("found",len(word_list),"words")
counter = 1

for word_index in range(get_word_count_par(word_list)):
	print(str(counter) + ". " + word_list[word_index])
	counter += 1

