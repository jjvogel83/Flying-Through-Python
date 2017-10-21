#Challenge 17 (Splitting a String)
#circus.py
schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    (show, time) = line.split(' - ')
    print(show, time)
schedule_file.close()