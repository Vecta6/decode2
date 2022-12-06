input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("" + chaine)
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
let chaine = "01010;11111;11111;01110;00100"
let z = chaine.length / 2
let chainep1 = chaine.slice(0, z)
let chainep2 = chaine.slice(z + 1, -1)
basic.showString( {TODO: Set} ,  {TODO: Set} )
basic.forever(function on_forever() {
    
})
