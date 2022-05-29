def usage():
    global CpuInfo,CpuUsage, MemoryUsageGB,CpuUsageLOG,CpuFreq,CpuUsageError
    smtpObj.login(sender,send_pass) 
    CpuUsage=psutil.cpu_percent(interval=1)
    CpuInfo=cpuinfo.get_cpu_info()['brand_raw']
    CpuFreq=psutil.cpu_freq().current
    MemoryUsage=int(psutil.virtual_memory().total - psutil.virtual_memory().available)
    MemoryUsageGB=MemoryUsage/1024/1024
    MemoryUsageGB=round(MemoryUsageGB)
    CpuUsageLOG=str(CpuUsage)
    MemoryUsageGB=str(MemoryUsageGB)
    CpuFreq=str(CpuFreq)
    CpuUsageError=CpuUsage
    CpuUsageError=int(CpuUsageError)
    if CpuUsageError>=80:
        message=(" Achtung Kritische Ueberlastung")
        smtpObj.sendmail(sender,recievers,message)
        print("Done")
        #Begrenzung für cpu verbrauch bei 80%
    timer1=threading.Timer(0.5, usage).start()