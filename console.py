#!/usr/bin/python3
"""
The console (cmd) for the project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """It will perfom basic commands on the files"""
    prompt = "(hbnb) "

    """Methods"""
    def do_quit(self, line):
        """Quit commad to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exits the command line if empty line + ENTER execute"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
