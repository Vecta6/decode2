def on_button_pressed_a():
    radio.send_string("")
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

chaine=[]
chaine.push(0b01010)

sendmess=""
for i in chaine:
    sendmess=sendmess+str(int(i))+";"
sendmess=sendmess[0:-1]

recemess=sendmess.split(";")
newrecemess=""
for j in recemess:
    binarie=str(bin(int(j)))[2::]
    for n in range(5-len(binarie)):
        binarie="0"+binarie
    newrecemess=newrecemess+binarie+";"
    
newrecemess=newrecemess[0:-1]

o = 0
a = 0



def on_forever():
    pass
basic.forever(on_forever)
