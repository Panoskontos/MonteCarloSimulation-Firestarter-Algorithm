import threading

def thread_function(name,start,end):
    print(f"Thread {name}: {i} - {start} - {end}")

if __name__ == "__main__":
    threads = list()
    step = 101//5
    print(step)
    for i in range(THREADS):
        start = step*i
        end = step*(i+1)
        # If it is the last
        if(i==THREADS-1):
            end=NUMS
        t = threading.Thread(target=thread_function, args=(i,start,end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

print("done")