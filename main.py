chaine="01010;11111;11111;01110;00100"

def on_received_string(receivedString):
    o=0
    a=0
    basic.clear_screen()
    for i in receivedString.split(";"):
        for j in i:
            if j=="1":
                led.plot(a, o)
            a+=1
        a=0
        o+=1
radio.on_received_string(on_received_string)

def on_button_pressed_a():
    global chaine
    radio.send_string(chaine)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
