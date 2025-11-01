while True:
    try:
        sec = int(input("Enter the seconds: "))
        if sec < 1:
            print("Seconds should be greater than 0. Try again.")
            continue
        break
    except Exception:
        print("Invalid seconds entered! Try again.")
import time
print("Timer started....")
for i in range(sec,-1,-1):
    min,secs = divmod(i,60)
    print(f"Time left: {min:02}:{secs:02}",end='\r')
    time.sleep(1)
else:
    print("\nTime's up!!!")