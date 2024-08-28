goal_height = 250
current_height = 0
meters_daily = 2.5
day = 0


while current_height != goal_height:
    current_height += meters_daily
    day += 1
    print(f'current height on day {day} is {current_height}')
print(f'it took {day} days to build the tower')