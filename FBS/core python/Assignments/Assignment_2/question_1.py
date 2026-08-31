#Convert the time entered in hh,min and sec into seconds.
Hr = int(input('Enter time in hours: '))
Min= int(input('Enter time in minutes: '))
Sec =  int(input('Enter time in sec: '))


time_In_Sec = (Hr * 3600) + (Min * 60) + Sec

print(f'Time in seconds : {time_In_Sec}')
