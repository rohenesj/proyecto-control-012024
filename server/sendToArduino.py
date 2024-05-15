import serial
import time
import json


ser = serial.Serial('/dev/ttyUSB0', 57600) # Change '/dev/ttyUSB0' to the correct port for your system

def send_pwm_value(value):
    # Ensure the value is within bounds
    value = min(max(value, 0), 255)
    ser.write(str(value).encode()) # Send the PWM value to Arduino
    print("Sent PWM value:", value)

def receive_analog_value():
    # Wait for the Arduino to send data
    while ser.in_waiting == 0:
        pass
    analog_value = ser.readline().decode().strip() # Read the analog value from Arduino
    return analog_value

try:
    while True:
        # Receive analog value from Arduino
        analog_value = receive_analog_value()
        print("Received analog value:", analog_value)

        # Send PWM value to Arduino
        pwm_value = int(input("Enter PWM value (0-255): "))
        send_pwm_value(pwm_value)

        time.sleep(0.1) # Wait for a short time before next iteration

except KeyboardInterrupt:
    print("\nExiting program")
    ser.close() # Close the serial connection when the program exits
