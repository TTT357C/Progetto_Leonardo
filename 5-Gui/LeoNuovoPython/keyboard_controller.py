"""
Function to analyze in which direction moving and for how long 

format of the messages: MMMDDDDK

MMM : characters for movement
DDDD : timer 0 - 9999 for movement
K : key character for message

    ###   DC DIRECTION    ###

FWD  ->  Leonardo moving forward (keyboard 'w')
BCK  ->  Leonardo moving backwards (keyboard 's')
LFT  ->  Leonardo turning  left (keyboard 'a')
RGH  ->  Leonardo turning right (keyboard 'd')

    ###   STEPPER DIRECTION   ###


S1U  ->  moving front axis up (keyboard 'r')
S1D ->  moving front axis down (keyboard 'f')
S2U  ->  moving middle axis up (keyboard 't')
S2D  ->  moving middle axis down (keyboard 'g')
S3U  ->  moving back axis up (keyboard 'y')
S3D  ->  moving back axis down (keyboard 'h')
S4U  ->  moving balance axis up (keyboard 'u')
S4D  ->  moving balance axis down (keyboard 'j')
"""

import keyboard
import time

def write_to_file(movement, duration, key):
    message = f"{movement}{duration:04d}{key}"
    with open('key.txt', 'w') as file:
        file.write(message)

def main():
    print("Press keys to control Leonardo. Press 'q' to quit.")
    start_time = 0
    current_movement = ""
    
    while True:
        if keyboard.is_pressed('w'):
            current_movement = "FWD"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('s'):
            current_movement = "BCK"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('a'):
            current_movement = "LFT"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('d'):
            current_movement = "RGH"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('r'):
            current_movement = "S1U"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('f'):
            current_movement = "S1D"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('t'):
            current_movement = "S2U"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('g'):
            current_movement = "S2D"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('y'):
            current_movement = "S3U"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('h'):
            current_movement = "S3D"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('u'):
            current_movement = "S4U"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('j'):
            current_movement = "S4D"
            start_time = time.time() if start_time == 0 else start_time
        elif keyboard.is_pressed('q'):
            print("Quitting...")
            break
        else:
            if current_movement and start_time > 0:
                duration = int((time.time() - start_time) * 1000)  # Convert to milliseconds
                if duration > 9999:
                    duration = 9999
                write_to_file(current_movement, duration, "0")
                current_movement = ""
                start_time = 0
        
        time.sleep(0.01)  # Small delay to prevent high CPU usage

if __name__ == "__main__":
    main()
