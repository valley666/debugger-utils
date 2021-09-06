import gdb

class thwatch(gdb.Command):
    def __init__(self):
        # This registers our class as "thwatch"
        super(thbreak, self).__init__("thwatch", gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        # When we call "thbreak" from gdb, this is the method
        # that will be called.
        gdb.execute('watch {}'.format(arg))
        

# This registers our class to the gdb runtime at "source" time.
thwatch)
