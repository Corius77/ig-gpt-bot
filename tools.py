import random
import time

def wait():
    return time.sleep(random.uniform(0.8, 1.5))

def png_name():
    random_float = str(random.uniform(1, 99))
    last_numbers = random_float[3:6]
    name = f"screen{last_numbers}.png"
    return name

