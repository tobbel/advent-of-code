'''
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
'''

with open('c:\\dev\\avc17\\4.txt') as f:
	lines = f.read().splitlines()

valid_count = 0
for line in lines:
	words = line.split(' ')
	if len(words) == len(set(words)):
		valid_count += 1
print('Part 1: ' + str(valid_count))

#187 too low (counted invalids)
#325 

# Part 2
'''
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
'''
valid_count = 0
import itertools
# lines = [
# 'nyot babgr babgr kqtu kqtu kzshonp ylyk psqk',
# 'iix ewj rojvbkk phrij iix zuajnk tadv givslju ewj bda',
# 'isjur jppvano vctnpjp ngwzdq pxqfrk mnxxes zqwgnd giqh',
# 'ojufqke gpd olzirc jfao cjfh rcivvw pqqpudp',
# 'ilgomox extiffg ylbd nqxhk lsi isl nrho yom',
# 'feauv scstmie qgbod enpltx jrhlxet qps lejrtxh',
# 'wlrxtdo tlwdxor ezg ztp uze xtmw neuga aojrixu zpt',
# 'wchrl pzibt nvcae wceb',
# 'rdwytj kxuyet bqnzlv nyntjan dyrpsn zhi kbxlj ivo',
# 'dab mwiz bapjpz jbzppa',
# ]
for line in lines: #line: asdfawje fewaölfkjwe felwöjkfwö lökjfawe 
	line_valid = True
	words = line.split(' ')
	#print(words)
	for word in words:
		if line_valid == False:
			break
		# check if any other word in list can be permutated
		perms = list(map(''.join, itertools.permutations(word)))
		perms.remove(word)
		#print(perms)
		for compare_word in words:
			if line_valid == False:
				break
			if compare_word in perms:
				print('Line: ' + line + ' not valid, ')
				print('\t\t\t' + compare_word + ' is anagram of ' + word)
				line_valid = False

	if line_valid:
		print('Line: ' + line + ' valid')
		print(line)
		valid_count += 1
print('Part 2 : ' + str(valid_count))
# 281: too high
# 325: too high (duh)
# 199 correct