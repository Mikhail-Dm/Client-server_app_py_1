import sys


def my_func():
    print(sys.argv[2])


def get_port_number():
    args = sys.argv
    port_number = args.index('-p') + 1
    return args[port_number]


if __name__ == "__main__":
    print(get_port_number())
