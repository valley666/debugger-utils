import gdb_utils


def hello(argv, from_tty):
    """
    Say hello.
    """
	
    print('hello %s' % argv[0])
    #print('hello %s', %args)
    #print('hello %s','xxxx')
gdb_utils.define(hello)
