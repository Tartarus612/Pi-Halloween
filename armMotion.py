import time
import mpu

def getXY(vector):
    return (int(vector.x), int(vector.y))

gravityInput = mpu.mpu()

startTime = time.perf_counter()

#get current gravity
gravityX, gravityY = gravityInput.GetXY(.1)
time.sleep(.1)
gravityX, gravityY = gravityInput.GetXY(.1)
endTime = time.perf_counter()

done = False

while not done:
    startTime = time.perf_counter()
    time.sleep(.05)
    endTime = time.perf_counter()
    #get current gravity
    gravityX, gravityY = gravityInput.GetXY((endTime - startTime))
    #print("gravityX=" + str(gravityX) + " gravityY=" + str(gravityY) + " endTime - startTime=" + str((endTime - startTime)))
     