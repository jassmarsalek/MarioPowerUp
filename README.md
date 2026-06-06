# MarioPowerUp
Mario Power-Up State Machine

This project will simulate Mario's power up system using a finite state machine on a Raspberry Pi. The system changes Mario's form based on button inputs that represent collecting power-ups or taking damage.
### States
Small Mario (starting state)
Super Mario
Fire Mario

### Inputs
Mushroom Button (Changes Mario from Small Mario to Super Mario)
Fire Flower Button (Changes Mario from Super/Small Mario to Fire Mario)
Enemy Hit Button (Causes Mario to lose a power level)

### Outputs
Blue LED (Represents Small Mario)
Red LED (Represents Super Mario)
Orange LED (Represents Fire Mario)

The active LED changes depending on the state Mario is in. The program will continuously check the button inputs and updates the state and outputs.
### State Diagram
<img width="3024" height="4032" alt="IMG_4934" src="https://github.com/user-attachments/assets/acb06735-662e-4a3a-9e35-8acd2ed395b9" />
### Inputs

Mushroom Button (GPIO 17) → Changes Small Mario to Super Mario
Fire Flower Button (GPIO 27) → Changes Small Mario or Super Mario to Fire Mario
Enemy Hit Button (GPIO 22) → Changes Fire Mario to Super Mario or Super Mario to Small Mario

### Outputs

Small Mario LED (GPIO 18) → Turns on when Mario is in the Small Mario state
Super Mario LED (GPIO 23) → Turns on when Mario is in the Super Mario state
Fire Mario LED (GPIO 24) → Turns on when Mario is in the Fire Mario state
