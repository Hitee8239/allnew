def handler():
    while True:
        v1 , v2 = (yield )
        print(f"{v1} + {v2} = {v1+ v2}")

listener = handler()
listener.__next__()
listener.send(1)
listener.send("message")