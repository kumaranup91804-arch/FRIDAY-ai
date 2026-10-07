# to run friday
import multiprocessing

def startjarvis():
    from FRIDAY.main import start
    start()

# to run hotword
def listenhotword():
    from FRIDAY.engine.features import hotword
    hotword()

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=startjarvis)
    p2 = multiprocessing.Process(target=listenhotword)

    p1.start()
    p2.start()

    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("System stopped")  