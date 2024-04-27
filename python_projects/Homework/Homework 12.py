import time
battery = 100
for i in range(battery):
    print('Playing Flappy Bird')
    print('Battery is ' + str(battery) + '%', end='\n')
    time.sleep(0.2)
    print('\n')
    battery -= 1
print('No more battery')
