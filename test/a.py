import time
import os
while 1:
    def getCPUtemperature():
        res = os.popen('vcgencmd measure_temp').readline()
        return(res.replace("temp=","").replace("'C\n",""))
    def getRAMinfo():
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i==2:
                return(line.split()[1:4])
    def getCPUuse():
        return(str(os.popen("top -n1 | awk '/Cpu\s\):/ {print $2}'").readline().strip()))
    def getDiskSpace():
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i +1
            line = p.readline()
            if i==2:
                return(line.split()[1:5])
    CPU_temp = getCPUtemperature()
    CPU_usage = getCPUuse()
 
# RAM information
# Output is in kb, here I convert it in Mb for readability
    RAM_stats = getRAMinfo()
    RAM_total = round(int(RAM_stats[0]) / 1000,1)
    RAM_used = round(int(RAM_stats[1]) / 1000,1)
    RAM_free = round(int(RAM_stats[2]) / 1000,1)
 
# Disk information
    DISK_stats = getDiskSpace()
    DISK_total = DISK_stats[0]
    DISK_used = DISK_stats[1]
    DISK_perc = DISK_stats[3]
    ticks = time.time()

    file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(file.read())/1000
    file.close()
    
    time.sleep(1)
    
    fo = open("foo_3.txt","a+")
    
   # t = (time.strfitme("%Y-%m-%d %H:%M:%S", time.localtime())
    t = ('CPU teamperature = '+CPU_temp)
    fo.write(t)
    t = ("\n")
    fo.write(t)
    t = ('CPU Use = '+CPU_usage)
    fo.write(t)
    t = ("\n")
    fo.write(t)
    print('CPU tem='+CPU_temp)
    fo.close()
   # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   # print('')
   # print('CPU Temperature = '+CPU_temp)
   # print('CPU Use = '+CPU_usage)
   # print('')
   # print('RAM Total = '+str(RAM_total)+' MB')
   # print('RAM Used = '+str(RAM_used)+' MB')
   # print('RAM Free = '+str(RAM_free)+' MB')
   # print('')  
   # print('DISK Total Space = '+str(DISK_total)+'B')
   # print('DISK Used Space = '+str(DISK_used)+'B')
   # print('DISK Used Percentage = '+str(DISK_perc))

