'''
Test Program For Fan Class

- Must have two objects
    - First object:
        - Must be on
        - Must be on maximum speed
        - Must have a radius of 10
        - Color must be yellow
    - Second object:
        - Must be off
        - Must be on medium speed
        - Must have a radius of 5
        - Color must be blue
'''

from Fan import Fan

SLOW = 1
MEDIUM = 2
FAST = 3

first_fan = Fan(True, FAST, 10, 'yellow')
second_fan = Fan(False, MEDIUM)

def display_divider():
    print('-' * 25)

def fan_general_info(fan:Fan):
    print(f'Power state: {fan.get_power()}, speed: {fan.get_speed()}, radius: {fan.get_radius()}, color: {fan.get_color()}')

display_divider()
print('First fan details:')
fan_general_info(first_fan)
print('\n\n\n')

display_divider()
print('Second fan details:')
fan_general_info(second_fan)
print('\n\n\n')


