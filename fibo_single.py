import time 

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

def worker(n): 
   print("Calculating Fibonacci numbers up to ", n, fibonacci(n)) 

start_time = time.time()
for i in range(3,31):
    worker(i)
end_time = time.time()
print("Done")
print("Execution time:", end_time-start_time)
