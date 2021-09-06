# -*- coding: utf-8 -*

import gdb
import gdb_utils
import gdb_utils
import re
from functools import partial
import traceback


#before

class thwatch(gdb.Command):
    def __init__(self):
        # This registers our class as "thwatch"
        super(thwatch, self).__init__("thwatch", gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        # When we call "thwatch" from gdb, this is the method
        # that will be called.
        gdb.execute('watch {}'.format(arg))
        

# This registers our class to the gdb runtime at "source" time.
thwatch()

#after
def twatch(argv, from_tty):
    if len(argv) != 1:
        raise gdb.GdbError('输入参数数目不对，help twatch以获得用法')
    result = gdb.execute('watch {}'.format(argv[0]),False,True)
    print 'gdb.execute return type:',type(result),'result value:',result
    searchResult = re.search(r'\d+',result)
    bpNum = searchResult.group()
    print("bp number:{}".format(bpNum))
    bp = gdb_utils.get_breakpoint(number=int(bpNum))
    print type(bp)
    bound_f = partial(cusdelbreakpoint, bp)

    gdb_utils.tstop(bound_f,bp)

gdb_utils.define(twatch)
                   
def cusdelbreakpoint(breakpoint):
    print("cusdelbreakpoint delete breakpoint callback breakpoint")

    #remove breakpoint stop callback
    #gdb_utils.stop(breakpoint.call,breakpoint,True)
    #bp = gdb_utils.get_breakpoint(number=num)
    print("acture delete breakpoint")
    breakpoint.delete()

def deletebreakpoint(breakpointEvent):
    print("automatic delete breakpoint callback breakpoint")
    bps = breakpointEvent.breakpoints
    print ("breakpointEvent:",type(bps))
    traceback.print_stack()
    print bps
    for bp in bps:
        #remove breakpoint stop callback
        gdb_utils.stop(deletebreakpoint,bp,True)
        #bp = gdb_utils.get_breakpoint(number=num)
        print("acture delete breakpoint")
        bp.delete()
        print bps



