# MarioPowerUp
Mario Power-Up State Machine

This project will simulate Mario's power up system using a finite state machine on a Raspberry Pi. The syste changes Mario's form based on button inputs that represent collecting power-ups or taking damage.
States include:
Small Mario (starting state)
Super Mario
Fire Mario

Inputs
Mushroom Button (Changes Mario from Small Mario to Super mario)
Fire Flower Button (Changes Mario from Super Mario to Fire Mario)
Enemy Hit Button (Causes Mario to lose a power level)

Outputs
Blue LED (Represents Small Mario)
Red LED (Represents Super Mario)
Orange LED (Represents Fire Mario)

The active LED changes depending on the state Mario is in. The program will continuously check the button inputs and updates the state and outputs.
<img width="4032" height="3024" alt="IMG_4934" src="https://github.com/user-attachments/assets/92ac54d3-d6fb-4174-96b1-d3665b17d3a9" />
