input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    
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
let o = 0
let a = 0
basic.forever(function on_forever() {
    
})
