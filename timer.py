import winsound
import time

def beep_alarm():
 for repeats in range(7):
        winsound.Beep(3000, 500)
        winsound.Beep(6000, 300)

def start_timer():
    timerDuration = int(input("Duration in seconds:"))
                    
    hours, minutes,seconds =0, 0, 0
    for i in range(timerDuration):
        print('\n' * 100)

    seconds += 1
    if seconds == 60:
       minutes += 1
       seconds = 0
    if minutes == 60:
       hours += 1
       minutes = 0
    print(f"{hours:02d}:{minutes:02d} : {seconds:02d}")
    time.sleep(1)

    beep_alarm()


if __name__ == '__main__':
     
    
    start_timer()