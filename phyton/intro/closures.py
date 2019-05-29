

# sample 1
def transmit_to_space(message):
    "This is the enclosing function"

    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

transmit_to_space("Test message")


# sample 2
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)

print_msg(9)

# sample 3
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()