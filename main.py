distanse = 0

def on_forever():
    global distanse
    distanse = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    if distanse <= 5:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # . . . .
                        # . . . .
                        # . . . .
        """)
    elif distanse <= 10:
        basic.show_leds("""
            # # . . .
                        # # . . .
                        # # . . .
                        # # . . .
                        # # . . .
        """)
    elif distanse <= 15:
        basic.show_leds("""
            # # # . .
                        # # # . .
                        # # # . .
                        # # # . .
                        # # # . .
        """)
    elif distanse <= 20:
        basic.show_leds("""
            # # # # .
                        # # # # .
                        # # # # .
                        # # # # .
                        # # # # .
        """)
    elif distanse <= 25:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
basic.forever(on_forever)
