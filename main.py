def on_button_pressed_a():
    radio.send_string("" + (chaine))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    global a, o
    basic.clear_screen()
    for i in receivedString.split(";"):
        for j in i:
            if j == "1":
                led.plot(a, o)
            a += 1
        a = 0
        o += 1
radio.on_received_string(on_received_string)

o = 0
a = 0
chaine = "01010;11111;11111;01110;00100"
z=chaine.length/2
chainep1=chaine[0:z]
chainep2=chaine[z+1:-1]
final=""
final.includes(chainep1)
final.includes(chainep2)
basic.show_string(final)

def on_forever():
    pass
basic.forever(on_forever)
