def handler():
    while True:
        value = (yield )
        print("Received %s " % value)

listener = handler()
listener.__next__()
listener.send(1)
listener.send("message")