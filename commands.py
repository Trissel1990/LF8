def commands():
    inputcommand=input('Command eingeben:')
    if inputcommand=="log":
        log()
    if inputcommand=="usage":
        print("cpu verbrauch liegt bei",CpuUsage,"Prozent")
        print("ram verbrauch liegt bei",MemoryUsageGB,"gb")
        print(CpuInfo)
        print("CPU Frequenz liegt bei:",CpuFreq,"MhZ")
    #commands für Ausführung von Logs per hand bzw auslesen des System Verbrauch 
    timer3=threading.Timer(0.1,commands()).start()