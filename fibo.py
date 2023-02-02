import threading 
import time
# Algorithm
def fibonacci(n): 
   if n<0: 
      print("Incorrect input") 
   # First Fibonacci number is 0 
   elif n==1: 
      return 0
   # Second Fibonacci number is 1 
   elif n==2: 
      return 1
   else: 
      return fibonacci(n-1)+fibonacci(n-2) 

# Optimization using threads
THREADS = 5
# thread worker 
def worker(n,j): 
   print(f"Thread {j} Calculating Fibonacci numbers up to ", n, fibonacci(n)) 


start_time = time.time()
i = 3
while(i+THREADS-1<37+THREADS-1):
    for j in range(1,THREADS):
        globals()['thread' + str(j)] =  threading.Thread(target=worker, args=(i+j-1,j )) 
        globals()['thread' + str(j)].start()
        globals()['thread' + str(j)].join()
    i+=THREADS-1

print("Done!")
end_time = time.time()
print("Execution time:", end_time-start_time)