import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)
time.sleep(1)
p.ChangeDutyCycle(2.5)
time.sleep(2)
p.ChangeDutyCycle(7.5)


except KeyboardInterrupt:
	GPIO.cleanup()
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
