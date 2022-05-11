from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(21)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

while True:
    print(button.is_pressed)
    while True:
        if button.is_pressed:
            print("Hello")
        else:
            print("Goodbye")
            
            while True:
                button.wait_for_press()
                
                # green on
                lights.green.on()
                sleep (1)
                
                # green off
                lights.green.off()
                sleep(1)
                
                # amber on
                lights.amber.on()
                sleep(1)
                
                # amber off
                lights.amber.off()
                sleep(1)
                
                # red, buzzer on
                lights.red.on()
                buzzer.on()
                sleep (3)
                
                # all light & buzzer off
                lights.red.off()
                lights.off()
                buzzer.off()
                delay(3)



