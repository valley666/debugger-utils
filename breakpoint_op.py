# -*- coding: utf-8 -*

import gdb
import traceback

#Manipulating breakpoint

class BreakpointOp(gdb.Command):
    """Move BreakpointOp
    Usage: BreakpointOp arr[1] breaknum
    Example:
    (gdb)  BreakpointOp variable breaknum -- 'hardware watch variable address and enable breaknum'
    """

    def __init__(self):
        # This registers our class as "BreakpointOp"
        super(BreakpointOp, self).__init__("BreakpointOp", gdb.COMMAND_DATA)

    def invoke(self, args, from_tty):
        # When we call "BreakpointOp" from gdb, this is the method
        # that will be called.
        print("Hello from BreakpointOp!")
	print type(args)
	print args
	argv = gdb.string_to_argv(args)	
	print type(argv)
	print argv
	if len(argv) != 2:
		raise gdb.GdbError('输入参数数目不对，help BreakpointOp')

	ptype = gdb.lookup_type('long').pointer()
	toWatch = gdb.parse_and_eval(argv[0]).address;
	gdb.execute('watch *{}'.format(toWatch.cast(ptype)))
	print type(gdb.breakpoints())
	gdb.breakpoints()[int(argv[1])].enabled = True

	return 

        # get the breakpoint info
	#ptype = gdb.lookup_type('long*') //No type named long*
	ptype = gdb.lookup_type('long').pointer()
	for num in range(0,100):
		toWatch = gdb.parse_and_eval('&arr[{}]'.format(num))
		gdb.execute('watch *{}'.format(toWatch.cast(ptype)))

	bps = gdb.breakpoints()
	if bps is None: raise gdb.GdbError('No breakpoints or watchpoints.')
	for bp in bps:
		try :
			if bp.type is not None:
				print('type %u' %bp.type)	
				if bp.type == gdb.BP_HARDWARE_WATCHPOINT:
					print(bp.number,' is a hardware watchpoint')
					bp.enabled = False
					#bp.delete() #This also invalidates the Python Breakpoint object. Any further access to this object’s attributes or methods will raise an error.
			if bp.location is not None:
				print('location %s' %bp.location)	
			if bp.expression is not None:
				print('expression %s' %bp.expression)	
			if bp.condition is not None: 
				print('condition %s' %bp.condition)	
			if bp.commands is not None: 
				print('commands %s' %bp.commands)	
		except Exception as e:
			traceback.print_exc()



# This registers our class to the gdb runtime at "source" time.
BreakpointOp()





