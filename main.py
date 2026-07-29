from datetime import datetime

def time() -> datetime:
    return datetime.now()

def greeting() -> str:
    return "Hello, welcome to my automation project!"

print(f"Current date and time: {time():%Y-%m-%d %H:%M:%S}")
print(greeting())