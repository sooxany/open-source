from time import sleep
from datetime import datetime

def log(message, when=None):
 if when is None:
    when = datetime.now()
 print(f'{when}: {message}')

log('Hi there!')
sleep(0.1)
log('Hello again!')