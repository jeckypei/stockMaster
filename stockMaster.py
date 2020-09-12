#!/usr/bin/python3

from  worker.worker import Worker

def main():
    worker = Worker("./config/")
    worker.startWork()
    
    
if __name__ == "__main__":
    main()   