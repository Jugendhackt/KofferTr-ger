#Imports
import RPi.GPIO as GPIO
import time

#Motoren
#Linkes Rad
P17 = 17
P27 = 27
P22 = 22
P18 = 18
#Rechtes Rad
P6 = 6
P13 = 13
P19 = 19
P26 = 26
#Ultraschallsensor
GPIO.TRIGGER = 23
GPIO.ECHO = 24
LED_NAH = 21
LED_WEIT = 22
#delay
delay = 0.002

GPIO.setmode(GPIO.BCM)
#setup linkes Rad
GPIO.setup(P17, GPIO.OUT)
GPIO.setup(P27, GPIO.OUT)
GPIO.setup(P22, GPIO.OUT)
GPIO.setup(P18, GPIO.OUT)

GPIO.setup(P13, GPIO.OUT)
GPIO.setup(P6, GPIO.OUT)
GPIO.setup(P19, GPIO.OUT)
GPIO.setup(P26, GPIO.OUT)

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.ECHO)
GPIO.setup(LED_NAH, GPIO.OUT)
GPIO.setup(LED_WEIT, GPIO.OUT)

#Gibt derzeitige Distanz zum am Nahe-Liegendsten Objekt
def distanz():
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO.TRIGGER, False)
	while GPIO.input(GPIO_ECHO) == 0:
		StartZeit = time.time()
	while GPIO.input(GPIO_ECHO) == 1:
		StopZeit = time.time()
	TimeElapsed = StopZeit - StartZeit
	distanz = (TimeElapsed * 34300) / 2
	return distanz

try:
	while True:
		
		print ("Gemessene Distanz: %.1f" % distanz())
		if distanz() >= 20:
			
			GPIO.output(LED_WEIT, 1)
			GPIO.output(LED_NAH, 0)
			
			GPIO.output(P17, 1)
			GPIO.output(P27, 0)
			GPIO.output(P22, 0)
			GPIO.output(P18, 1)
			
			GPIO.output(P6, 1)
			GPIO.output(P13, 0)
			GPIO.output(P19, 0)
			GPIO.output(P26, 1)
			
			time.sleep(delay)
			
			GPIO.output(P17, 1)
			GPIO.output(P27, 1)
			GPIO.output(P22, 0)
			GPIO.output(P18, 0)
			
			GPIO.output(P6, 0)
			GPIO.output(P13, 0)
			GPIO.output(P19, 1)
			GPIO.output(P26, 1)
			
			time.sleep(delay)
			
			GPIO.output(P17, 0)
			GPIO.output(P27, 1)
			GPIO.output(P22, 1)
			GPIO.output(P18, 0)
			
			GPIO.output(P6, 0)
			GPIO.output(P13, 1)
			GPIO.output(P19, 1)
			GPIO.output(P26, 0)
			
			time.sleep(delay)
			
			GPIO.output(P17, 0)
			GPIO.output(P27, 0)
			GPIO.output(P22, 1)
			GPIO.output(P18, 1)
			
			GPIO.output(P6, 1)
			GPIO.output(P13, 1)
			GPIO.output(P19, 0)
			GPIO.output(P26, 0)
			
			print ("Runde")
			time.sleep(delay)
		
		else:
			print ("Zu nah! - Halte an...")
			GPIO.output(LED_WEIT, 0)
			GPIO.output(LED_NAH, 1)
			time.sleep(2)

except KeyboardInterrupt:
	print ("Anwendung von Anwender/-in gestoppt")
	GPIO.cleanup()