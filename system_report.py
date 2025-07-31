import platform
import psutil
import socket
import datetime

def system_info():
    info = {}

        # OS and machine details
    info['System'] = platform.system()
    info['Node Name'] = platform.node()
    info['Release'] = platform.release()
    info['Version'] = platform.version()
    info['Machine'] = platform.machine()
    info['Processor'] = platform.processor()

    # CPU and Memory
    info['CPU Cores'] = psutil.cpu_count(logical=True)
    info['RAM (Total)'] = f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
    info['RAM (Used)'] = f"{round(psutil.virtual_memory().used / (1024 ** 3), 2)} GB"

    # Disk
    disk = psutil.disk_usage('/')
    info['Disk (Total)'] = f"{round(disk.total / (1024 ** 3), 2)} GB"
    info['Disk (Used)'] = f"{round(disk.used / (1024 ** 3), 2)} GB"

    # Network
    hostname = socket.gethostname()
    info['IP Address'] = socket.gethostbyname(hostname)

    # Uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    info['System Uptime Since'] = boot_time.strftime('%Y-%m-%d %H:%M:%S')

    return info

def save_report(info):
    with open("system_report.txt", "w") as f:
        for key, value in info.items():
            f.write(f"{key}: {value}\n")
    print("✅ System report saved as 'system_report.txt'")

    # Run it
if __name__ == "__main__":
    system_info = system_info()
    save_report(system_info)