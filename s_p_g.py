#s_p_g.py 
#This script allows the user to get stock prices from companies within a specific industry.
#As an example, when you use the command "--tech tech" you will be getting pricing of stocks from that industry i.e Google, Apple etc.
import os
import time
import sys
import cmd

# [TODO] need to get an alpha vantage api so we can get stock data. 
class PriceGetterShell(cmd.cmd):

    intro = "Welcome to the Price Getter Shell. Type ? or help to list commands. \n"
    prompt = "> "
    file = None

    #---- Your commands go below here

    def exit_shell(self, arg):
        #'Stop recording, close the window, and exit: BYE'
        print("Thank you for using Price Getter Shell")
        self.close()
        exit_shell()
        return True


    #-- important commands below, so top works. -- needs more work    
    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def parse(arg):
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    PriceGetterShell().cmdloop()                


