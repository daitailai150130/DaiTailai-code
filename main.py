def on_button_pressed_a():
    basic.show_number(randint(1, 6))
input.on_button_pressed(Button.A, on_button_pressed_a)
