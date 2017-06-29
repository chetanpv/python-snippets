from eventlet import event
from eventlet import greenthread

class LoopingCall(object):
    def __init__(self):
        self._running = False

    def start(self, interval, initial_delay=None):
        self._running = True
        done = event.Event()
        def _inner():
            try:
                while self._running:
                    print "In loop"
                    greenthread.sleep(interval)
                    print "loop done"
            except Exception as e:
                print('in looping call')
                return
        self.done = done
        greenthread.spawn(_inner)
        return self.done

    def stop(self):
        self._running = False

    def wait(self):
        return self.done.wait()

timer = LoopingCall()

timer.start(interval=5).wait()
