'''

'''
import os 
import time

# Get problem: n.txt
dir_path = os.path.dirname(os.path.realpath(__file__))
problem_number = os.path.basename(__file__).split('.')[0][0]
file_path = dir_path + '/' + problem_number + '-in.txt'
with open(file_path) as f:
	lines = f.read().splitlines()

# lines = [
# '[1518-11-01 00:00] Guard #10 begins shift',
# '[1518-11-01 00:05] falls asleep',
# '[1518-11-01 00:25] wakes up',
# '[1518-11-01 00:30] falls asleep',
# '[1518-11-01 00:55] wakes up',
# '[1518-11-01 23:58] Guard #99 begins shift',
# '[1518-11-02 00:40] falls asleep',
# '[1518-11-02 00:50] wakes up',
# '[1518-11-03 00:05] Guard #10 begins shift',
# '[1518-11-03 00:24] falls asleep',
# '[1518-11-03 00:29] wakes up',
# '[1518-11-04 00:02] Guard #99 begins shift',
# '[1518-11-04 00:36] falls asleep',
# '[1518-11-04 00:46] wakes up',
# '[1518-11-05 00:03] Guard #99 begins shift',
# '[1518-11-05 00:45] falls asleep',
# '[1518-11-05 00:55] wakes up'
# ]
#start = time.process_time()

def sortingFunction(e):
	return e.date + e.time

class Event:
	def __init__(self, date, time, event):
		self.date = date
		self.time = time
		self.event = event

class Guard:
	def __init__(self, number):
		self.number = number
		self.sleeping_minutes = []
		for i in range(0, 59):
			self.sleeping_minutes.append(0)
	
	def start_sleeping(self, time):
		self.sleep_start = time.split(':')[1]
		#print('Guard #', self.number, 'started sleeping at', time)
		
	def stop_sleeping(self, time):
		self.sleep_stop = time.split(':')[1]
		#print('Guard #', self.number, 'stopped sleeping at', time)
		for i in range(int(self.sleep_start), int(self.sleep_stop)):
			self.sleeping_minutes[i] += 1

events = []
for line in lines:
	# For each line, split and create
	line = line.split('] ')
	date = line[0][1:].split(' ')[0]
	time = line[0][1:].split(' ')[1]
	event = line[1]
	e = Event(date, time, event)
	events.append(e)

# Order by timestamp
events.sort(reverse=False, key=sortingFunction)

#for event in events:
#	print(event.date + ' ' + event.time + ' ' + event.event)

guards = []
current_guard = Guard(-1)
# Find guard that has most minutes asleep
for event in events:
	if event.event.startswith('Guard'):
		text = event.event.split(' ')
		guard_number = int(text[1][1:])
		guard = [x for x in guards if x.number == guard_number]
		if len(guard) == 0:
			guard = Guard(guard_number)
			guards.append(guard)
		else:
			guard = guard[0]
	elif event.event.startswith('falls'):
		guard.start_sleeping(event.time)
	else:
		guard.stop_sleeping(event.time)

most_minutes = 0
most_minutes_number = -1
for g in guards:
	total_sleep_minutes = 0
	for minute in g.sleeping_minutes:
		total_sleep_minutes += minute
		
	if total_sleep_minutes > most_minutes:
		most_minutes = total_sleep_minutes
		most_minutes_number = g.number

print('Guard ID:', str(most_minutes_number))

# Find the minute that guard sleeps the most
for g in guards:
	max_minute = 0
	max_minute_index = -1
	if g.number == most_minutes_number:
		for i in range(0, len(g.sleeping_minutes)):
			minute_sleeping = g.sleeping_minutes[i]
			if minute_sleeping > max_minute:
				max_minute = minute_sleeping
				max_minute_index = i
		print('Minute selected:', str(max_minute_index))
		
# 4-2: - Of all guards, which guard is most frequently asleep on the same minute?
max_minute = 0
max_minute_index = -1
max_minute_guard = -1
for g in guards:
	for i in range(0, len(g.sleeping_minutes)):
			minute_sleeping = g.sleeping_minutes[i]
			if minute_sleeping > max_minute:
				max_minute = minute_sleeping
				max_minute_index = i
				max_minute_guard = g.number
print('Max minute:', str(max_minute))
print('Minute selected:', str(max_minute_index))
print('Guard ID:', str(max_minute_guard))

#end = time.process_time()
#print(str(end-start))