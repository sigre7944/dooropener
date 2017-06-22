import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

try:
	while True:
		GPIO.output(7,1)
		time.sleep(0.0015)
		GPIO.output(7,0)

		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
