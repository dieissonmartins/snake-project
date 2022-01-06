# Python3 program to

import datetime


class Main:
    # attribute
    today = datetime.datetime.now()
    input = ''

    def run(self):
        print("running script---------")
        print("-----------------------")
        print(self.today.strftime("%Y-%m-%d"))

        self.input = input("inform date period:\n")

        ret = self.input

        return ret


# object instantiation
execute = Main()

# method through objects
response = execute.run()

print(response)

print("end process script")
