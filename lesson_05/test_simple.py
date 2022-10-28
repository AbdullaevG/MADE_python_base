from simple import my_function
from tud_test_base import set_keyboard_input, get_display_output


def test_1():
    set_keyboard_input(["Maurisio", "cat"])

    my_function()

    output = get_display_output()

    assert output == ["Your name: ", "Your animal: ",
                      "Hi Maurisio, you like cat!!!"]
