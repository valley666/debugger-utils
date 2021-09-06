import gdb

class StackWalk(gdb.Command):
    def __init__(self):
        # This registers our class as "StackWalk"
        super(StackWalk, self).__init__("stackwalk", gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        # When we call "StackWalk" from gdb, this is the method
        # that will be called.
        print("Hello from StackWalk!")
        # get the register
        rbp = gdb.parse_and_eval('$rbp')
        rsp = gdb.parse_and_eval('$rsp')
        ptr = rsp
        ppwc = gdb.lookup_type('void').pointer().pointer()
        while ptr < rbp:
            try:
                print('pointer is {}'.format(ptr))
                print(gdb.execute('p (char*){}'.format(ptr.cast(ppwc).dereference())))
                print('===')
            except:
                pass
            ptr += 8
        

# This registers our class to the gdb runtime at "source" time.
StackWalk()
