# Programmer: Cyril Garcia
# Date: November 11, 2018
# 
# Challenge Description: We are writing a tool to help users manage their calendars. 
# Given an unordered list of times of day when someone is busy, 
# write a function that tells us whether they're available during 
# a specified period of time.


meetings = [
  {"start": 1230, "end": 1300},
  {"start":  845, "end":  900},
  {"start": 1300, "end": 1500},
  {"start": 700, "end": 800}
]

def isAvailable(hours, start, end):

	for hour in hours:
		s = hour["start"]
		e = hour["end"]

		if start > s and end < e:
			return False
		elif start > s  and start < e:
			return False
		elif end > s and end < e:
			return False
		elif start <= s and end >= e:
			return False

	return True

a = isAvailable(meetings,  830,  845) 
b = isAvailable(meetings, 1330, 1400)  
c = isAvailable(meetings,  830,  930)  
d = isAvailable(meetings,  855,  930)  
e = isAvailable(meetings, 1500, 1600)  
f = isAvailable(meetings,  845,  900)  
print(a,b,c,d,e,f)
