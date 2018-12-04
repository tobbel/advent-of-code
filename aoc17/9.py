'''
Groups - sequences that begin with { and end with }
Group contains zero or more things, separated by commas: another group or garbage

Garbage begins with < and ends with >.
Any character after ! should be ignored.

Here are some self-contained pieces of garbage:

<>, empty garbage.
<random characters>, garbage containing random characters.
<<<<>, because the extra < are ignored.
<{!>}>, because the first > is canceled.
<!!>, because the second ! is canceled, allowing the > to terminate the garbage.
<!!!>>, because the second ! and the first > are canceled.
<{o"i!a,<{i<a>, which ends at the first >.
Here are some examples of whole streams and the number of groups they contain:

{}, 1 group.
{{{}}}, 3 groups.
{{},{}}, also 3 groups.
{{{},{},{{}}}}, 6 groups.
{<{},{},{{}}>}, 1 group (which itself contains garbage).
{<a>,<a>,<a>,<a>}, 1 group.
{{<a>},{<a>},{<a>},{<a>}}, 5 groups.
{{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are canceled).
Your goal is to find the total score for all groups in your input. Each group is assigned a score which is one more than the score of the group that immediately contains it. (The outermost group gets a score of 1.)

{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
What is the total score for all groups in your input?




Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.

<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
How many non-canceled characters are within the garbage in your puzzle input?



'''

score = 0
with open('c:\\dev\\avc17\\9-in.txt') as f:
	input = f.read()
#print(input)

#input = '{{{}}}'
total_groups = 0
i = 0
group_depth = 0
group_lengths = []
total_score = 0
in_garbage = False
chars_in_garbage = 0
while i < len(input):
	inp = input[i]
	#print(inp)
	if in_garbage:
		if inp == '>':
			in_garbage = False
		elif inp == '!':
			i += 2
			continue
		else:
			chars_in_garbage += 1
			i += 1
			continue
	
	if inp == '{':
		# start group
		total_groups += 1
		group_depth += 1
		group_lengths.append([group_depth, int(i)])
	elif inp == '!':
		i += 1
	elif inp == '<':
		# start garbage
		in_garbage = True
	elif inp == '}':
		#group_length = i - group_lengths.pop()
		group_info = group_lengths.pop()
		start = group_info[1]
		total_score += group_info[0]
		end = int(i + 1)
#		print('Ended group: ', input[start:end])
#		print('Group depth: ', group_depth)
		group_depth -= 1
	i += 1

print('End, total groups: ', total_groups, ' total score: ', total_score)
print('Chars in garbage: ', chars_in_garbage)