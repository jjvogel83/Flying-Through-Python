#Challenge 18 (Reading Into a Dictionary)
#circus.py
performances = {}

schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    (show, time) = line.split(' - ')
    performances[show] = time.strip()
    print(show, time)
    
schedule_file.close() 
print(performances)
