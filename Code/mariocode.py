#AI was used to develop and to help build the code.
from gpiozero import Button, LED
from signal import pause
#inputs
mushroom_button = Button(17)
fireflower_button = Button(27)
enemyhit_button = Button(22)
#outputs
small_led = LED(18)
super_led = LED(23)
fire_led = LED(24)
#All states. AI helped define them. I also had the AI explain what to us the purpose.
SMALL = "Small Mario"
SUPER = "Super Mario"
FIRE = "Fire Mario"

state = SMALL
 # AI helped explain how outputs should change based on the current state.
def update_outputs():
    if state == SMALL:
        small_led.on()
        super_led.off()
        fire_led.off()

    elif state == SUPER:
        small_led.off()
        super_led.on()
        fire_led.off()

    elif state == FIRE:
        small_led.off()
        super_led.off()
        fire_led.on()

def mushroom_pressed():
    global state

    if state == SMALL:
        state = SUPER

    update_outputs()

def fireflower_pressed():
    global state

    if state == SMALL or state == SUPER:
        state = FIRE
# The AI suggested that we add another input for the Small Mario to turn it into Fire Mario. It told us to use an or statement.
    update_outputs()

def enemyhit_pressed():
    global state

    if state == FIRE:
        state = SUPER
    elif state == SUPER:
        state = SMALL

    update_outputs()

mushroom_button.when_pressed = mushroom_pressed
fireflower_button.when_pressed = fireflower_pressed
enemyhit_button.when_pressed = enemyhit_pressed

update_outputs()

pause()
