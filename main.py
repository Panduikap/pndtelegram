import os, time

delay = 60
for i in range(99**99):
	os.system('python scrap.py')
	for i in range(delay):
		print(f'{delay - i+ 1} Detik Lagi', end='\r')
		time.sleep(1)