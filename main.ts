let chaine = "01010;11111;11111;01110;00100"
radio.onReceivedString(function on_received_string(receivedString: string) {
    let o = 0
    let a = 0
    basic.clearScreen()
    for (let i of _py.py_string_split(receivedString, ";")) {
        for (let j of i) {
            if (j == "1") {
                led.plot(a, o)
            }
            
            a += 1
        }
        a = 0
        o += 1
    }
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    radio.sendString(chaine)
})
basic.forever(function on_forever() {
    
})
