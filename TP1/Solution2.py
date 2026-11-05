total = 9875
hour = total//3600
re_h = total%3600
minute = re_h//60
re_m = re_h%60
second = re_m


print("Hour :",hour)
print("Minute :",minute)
print("Second :",re_m)

#print(f"{hour} H-{minute} m-{second} s")