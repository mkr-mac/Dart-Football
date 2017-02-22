import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
i=0
while True:
	one = GPIO.input(16)
	two = GPIO.input(20)
	three = GPIO.input(21)
	four = GPIO.input(13)
	five = GPIO.input(19)
	six = GPIO.input(26)

	if one:
                if two or three:
                        pass
                elif four:
                        print("One")
                elif five:
                        print("Two")
                elif six:
                        print("Three")
                else:
                        print("Error!")
                
        elif two:
                if one or three:
                        pass
                elif four:
                        print("Four")
                elif five:
                        print("Five")
                elif six:
                        print("Six")
                else:
                        print("Error!")

        elif three:
                if one or two:
                        pass
                elif four:
                        print("Seven")
                elif five:
                        print("Eight")
                elif six:
                        print("Nine")
                else:
                        print("Error!")
                        
        #time.sleep(1)
