# py-port-scanner
Building a port scanner with python3 

Notes

threading.Lock allows a lock to allow thread workers to hold the line in order to do a certain actions such as manipulating variables without race conditions(another worker overwriting the variable manipulation performed by a worker that needed to perform a task on the variable at the same time but got there first.)

get a service being used by a port by using the socket.getservbyport(port, 'tcp'). The first arg is the port number of type int, and the second the protocol that is being used (tcp, udp) of type string.

To set up queue:

    import:
        from queue import Queue

    instatiate queue:
        q = Queue()

    add to queue:
        q.put(arg)

    retrieve from queue:
        q.get() -> returns item in queue

    task with queue item complete:
        q.task_done()
    
    block processes until queue has emptied:
        q.join()

