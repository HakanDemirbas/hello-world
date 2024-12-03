import time
import sys

class Greeting:
    def __init__(self):
        self.message = "Hello"
        self.delay_time = 0.1

    def print_char(self, char):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(self.delay_time)

    def print_greeting(self):
        for char in self.message:
            self.print_char(char)
        print()

    def repeat_message(self, count):
        for _ in range(count):
            self.print_greeting()

def main():
    greeting_instance = Greeting()
    greeting_instance.repeat_message(1) 

if __name__ == "__main__":
    main()
