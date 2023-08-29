import os, psutil, platform, cpuinfo, wmi

cpu_character = '█'

def get_system_usage():
    sysinfo =  f'\n\tCPU Usage %:{psutil.cpu_percent()}'  
    sysinfo = sysinfo + f'\n\tMemory Usage %:{psutil.virtual_memory().percent}'
    return  sysinfo

def get_platform_information():
    sysinfo = f'\n\tOperating System:{platform.system()}' 
    sysinfo = sysinfo + f'\n\tArchitecture:{platform.architecture()}'    
    sysinfo = sysinfo + f'\n\tPlatform:{platform.platform()}'        
    sysinfo = sysinfo + f'\n\tHostname:{platform.node()}' 
    sysinfo = sysinfo + f'\n\tMachine:{platform.machine()}' 
    sysinfo = sysinfo + f'\n\tProcessor:{platform.processor()}' 
    sysinfo = sysinfo + f'\n\tRelease:{platform.release()}' 
    sysinfo = sysinfo + f'\n\tVersion:{platform.version()}'     
    return sysinfo

def get_platform_specification():
    return f'\n\tSystem Specifications:{platform.uname()}' 

def get_system_information():
    sysinfo = f'\n\tCurrent User:{os.getlogin()}' 
    sysinfo = sysinfo + f'\n\tCurrent Working Directory:{os.getcwd()}'
    sysinfo = sysinfo + f'\n\tCPU Count:{os.cpu_count()}' 
    return sysinfo

def get_cpu_information():
    my_cpuinfo = cpuinfo.get_cpu_info()
    sysinfo = f'\n\tCPU Information:{my_cpuinfo["brand_raw"]}' 
    sysinfo = sysinfo + f'\n\tCPU Actual Frequency:{my_cpuinfo["hz_actual_friendly"]}' 
    sysinfo = sysinfo + f'\n\tCPU Advertised Frequency:{my_cpuinfo["hz_advertised_friendly"]}' 
    return sysinfo

def get_gpu_information():
    pc = wmi.WMI() 
    os_info = pc.Win32_OperatingSystem()[0]
    sysinfo = f'\n\tProcessor:{pc.Win32_Processor()[0].name}' 
    sysinfo = sysinfo + f'\n\tVideo Processor:{pc.Win32_VideoController()[0].name}' 
    return sysinfo

def get_windows_information():
    pc = wmi.WMI() 
    os_info = pc.Win32_OperatingSystem()[0]
    sysinfo = f'\n\tWin32 Information:{os_info}' 
    return sysinfo

def get_RAM_information():
    sysinfo = f'\n\tTotal Random Access Memory (RAM):{psutil.virtual_memory().total}  Bytes' 
    sysinfo = sysinfo + f'\n\tTotal Random Access Memory (RAM):{psutil.virtual_memory().total / 1024 / 1024 / 1024:2f} in GB' 
    return sysinfo


def get_complete_system_information():
    sysinfo = f'\n\nPlatform Information:{get_platform_information()}'
    sysinfo = sysinfo + f'\n\nSystem Information:{get_system_information()}'
    sysinfo = sysinfo + f'\n\nPlatform Information:{get_cpu_information()}' 
    sysinfo = sysinfo + f'\n\nWIN32 Information:{get_gpu_information()}'     
    sysinfo = sysinfo + f'\n\nMemory Information:{get_RAM_information()}'    
    sysinfo = sysinfo + f'\n\nSystem Usage:{get_system_usage()}'
    sysinfo = sysinfo + f'\n\nSystem Windows Info:{get_windows_information()}'    
    return sysinfo


testing = False 
if testing:
    print(f'{get_complete_system_information()}')
