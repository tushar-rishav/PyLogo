from turtle import *
import cmd
import sys

file_name = None


class PyLogo(cmd.Cmd):
    intro = 'Welcome to Logo. Type help or ? to list commands.\n'
    prompt = 'PyLogo#'
    flag = 0

    def do_forward(self, arg):
        'Move the turtle forward by the specified distance: forward 10'
        forward(*parse(arg))
        if self.flag:
            self.do_record("forward " + arg + "\n")

    def do_right(self, arg):
        'Move the turtle right by the specified distance: right 10'
        right(*parse(arg))
        if self.flag:
            self.do_record("right " + arg + "\n")

    def do_left(self, arg):
        'Move the turtle left by the specified distance: left 10'
        left(*parse(arg))
        if self.flag:
            self.do_record("left " + arg + "\n")

    def do_goto(self, arg):
        'Move the turtle to an absolute position with\
         changing orientation: goto 100 200'
        goto(*parse(arg))
        if self.flag:
            self.do_record("goto " + arg + "\n")

    def do_home(self, arg):
        'Return turtle to home position: home'
        home()
        if self.flag:
            self.do_record("home")

    def do_circle(self, arg):
        '''
            Draw circle: circle (radius, extent=None, steps=None)
            circle 50,180,2
            circle 50
            circle 50,180
        '''
        circle(*parse(arg))
        if self.flag:
            self.do_record("circle " + arg + "\n")

    def do_position(self, arg):
        'Print the current turtle position:position'
        print("current position is %d %d\n" % position())
        if self.flag:
            self.do_record("position " + arg + "\n")

    def heading(self, arg):
        'Print the current turle heading in degrees: heading'
        print("Current heading is %d\n" % (heading(),))
        if self.flag:
            self.do_record("heading " + arg + "\n")

    def do_color(self, arg):
        'Set the color: color BLUE'
        color(arg.lower())
        if self.flag:
            self.do_record("color " + arg + "\n")

    def do_undo(self, arg):
        'undo(repeatedly) the last turtle action(s):undo'
        undo()
        if self.flag:
            self.do_record("undo\n")

    def do_reset(self, arg):
        'Clear the screen and return turtle to center: reset'
        reset()
        if self.flag:
            self.do_record("reset\n")

    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit: bye'
        print('Logo says Goodbye!')
        try:
            self.flag = 0
            self.close()
            bye()
            sys.exit(0)
        except Exception as e:
            print e

    def do_stop_record(self, arg):
        'Close the current recording'
        file_name.close()
        self.flag = 0

    def do_record(self, arg=None):
        "Save future commands to filename: record playback.cmd"
        if not self.flag:
            global file_name
            self.flag = 1
            file_name = open(arg, 'a')  # open the file to write data
        file_name.write(arg)

    def do_playback(self, arg):
        "Playback commands from a file: playback playback.cmd"
        self.close()
        cmds = open(arg).read().splitlines()
        self.cmdqueue.extend(cmds)

    def close(self):
        global file_name
        if file_name:
            file_name.close()
            file_name = None


def parse(arg):
    "Convert a series of zero or more numbers to an argument tuple"
    return tuple(map(int, arg.split()))


def main():
    PyLogo().cmdloop()
if __name__ == '__main__':
    main()
