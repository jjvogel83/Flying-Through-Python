#Challenge 16 (Reading schedule.txt)
#circus.py
schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    print(line)
    
schedule_file.close()
