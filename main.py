import pyautogui
import time

# Set the duration of the click
click_duration = 0.1

# Set the time interval between clicks
interval = 0.2

# Create a dictionary of coordinates for each animal
coords = {
    'sleep': [(23, 1058), (21, 1010), (36, 904),(36, 904)],
    'shut down': [(23, 1058), (21, 1010), (26, 932),(26, 932)],
    'restart': [(23, 1058), (21, 1010), (20, 965),(20, 965)]
}
while True:
    # Print the menu
    print('Menu:')
    print('1. sleep')
    print('2. shut down')
    print('3. restart')

    # Get the user's choice
    choice = input('Enter your choice: ')

    if choice in ['1', '2', '3']:
    # Perform the autoclick based on the user's choice
        if choice == '1':
            for coord in coords['sleep']:
                x_coord, y_coord = coord
                pyautogui.click(x=x_coord, y=y_coord)
                time.sleep(interval)
            exit()
        elif choice == '2':
            for coord in coords['shut down']:
                x_coord, y_coord = coord
                pyautogui.click(x=x_coord, y=y_coord)
                time.sleep(interval)
            exit()
        elif choice == '3':
            for coord in coords['restart']:
                x_coord, y_coord = coord
                pyautogui.click(x=x_coord, y=y_coord)
                time.sleep(interval)
            exit()
else:
     print('Invalid choice. Please try again.')



