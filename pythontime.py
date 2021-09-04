# how we fetch time of any process in python
# using time module 

import time

start=time.time()    #this is starting time 
 
a=1000
while a>0:
    print(a)
    a=a-1

time.sleep(5)     
# this is used to take break in code after 5seconds break it will automatically runs
print(f' Time taken by while loop is   {time.time()-start}')


# now u will see that process take almost 3+5 =8
# this process takes 3.8363451957702637s to process

print("thanks for watching my video please do subscribe my channel and like the video")