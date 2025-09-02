import time

LOG_FILE = "/shared/logs/app.log"

def tail_file(path):
    with open(path, "r") as file:
        file.seek(0, 2)  # move to end of file
        while True:
            line = file.readline()
            if not line:
                time.sleep(5)
                continue
            print(f"[Logger] {line.strip()}")  

if __name__ == "__main__":
    print("Logger service started...")
    tail_file(LOG_FILE)
