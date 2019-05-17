#!/usr/bin/python


class company:
    emp_id = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address
        print("Constructor Invoked")

    def __del__(self):
        print("Destructor Invoked")


def main():
    AAI = company("Bhushan", "Hinjewadi phase 1")
    print(AAI.__dict__)


if __name__ == '__main__':
    main()
		

