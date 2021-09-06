# -*- coding: utf-8 -*

import gdb
import traceback

#gdb events handler

def exit_handler (event):
    if  isinstance(event,gdb.Event): 
        if type(event) == gdb.ExitedEvent:
            print type(event)
            #正常退出有exit_code字段,非正常退出没有exit_code字段 
            print ("exit code: %d" % (event.exit_code))

#gdb.events.exited.connect (exit_handler)

def stop_handler (event):
    print ('stop handler called')
    if  isinstance(event,gdb.Event): 
        if type(event) == gdb.StopEvent:
            print type(event)
            print ("event __dict__",event.__dict__)
        elif type(event) == gdb.SignalEvent:
            print type(event)
            print ("event __dict__",event.__dict__)
        elif type(event) == gdb.BreakpointEvent:
            print type(event)
            print ("event __dict__", event.__dict__)
            
            
#gdb.events.stop.connect(stop_handler)

def stop_handler1(event):
    print ('stop handler1 called')
    gdb.events.stop.disconnect(stop_handler)

#connectResult = gdb.events.stop.connect(stop_handler1)
#print('connectResult:',type(connectResult))

def new_thread_handler (event):
    if  isinstance(event,gdb.Event): 
        if type(event) == gdb.NewThreadEvent:
            print type(event)
            print ("event __dict__",event.__dict__)

gdb.events.new_thread.connect(new_thread_handler)
