def come_home(callback):
    print("im home")
    return callback


def go_sleep():
    print("im gonna go sleep")

def go_run():
    print("im going on a run")

come_home(go_sleep)
come_home(go_run)