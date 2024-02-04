import os   #importing library for interacting with the operating system
import platform #importing library for fetching system information
import socket  #importing library for networking operations
import subprocess #importing library for running shell commands
import psutil #importing library for system monitoring
import speedtest #importing library for measuring internet speed
import getmac #importing libarary for getting MAc address of Wifi     
def All_installed_software():
    installed_software = subprocess.check_output(['wmic', 'product', 'get', 'name']).decode('utf-8') # Using 'wmic' command to fetch a list of installed software in the system
    return installed_software 
def internet_speed():    
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Converting download speed to Mbps
    upload_speed = st.upload() / 10**6  # Converting upload speed to Mbps
    return f"Download Speed: {download_speed:.2f} Mbps, Upload Speed: {upload_speed:.2f} Mbps"
def screen_resolution():
    try:      
        from screeninfo import get_monitors   #Importing get_monitors function from screeninfo library Getting screen resolution by using the screeninfo library
        monitors = get_monitors()
        return f"Screen Resolution: {monitors[0].width}x{monitors[0].height}"
    except ImportError:
        return "Screen Resolution: Library 'screeninfo' not installed"
def cpu_model_info():
    cpu_info = f"CPU Model: {platform.processor()}\n"
    cpu_info += f"Cores: {psutil.cpu_count(logical=False)}, Threads: {psutil.cpu_count(logical=True)}"
    return cpu_info
def gpu_Model_info():
    try:
        import GPUtil
        gpu_info = GPUtil.getGPUs()
        if gpu_info:
            return f"GPU Model: {gpu_info[0].name}"
        else:
            return "No GPU found"
    except ImportError:
        return "GPU Model: Library 'GPUtil' not installed"
def ram_size():
    ram_size = psutil.virtual_memory().total / (1024**3)   # Converting RAM size to GB 
    return f"RAM Size: {ram_size:.2f} GB"
def screen_size():
    try:
        from screeninfo import get_monitors  # for Getting screen size in inches using the screeninfo library
        monitors = get_monitors()
        if monitors:
            return f"Screen Size: {monitors[0].width} inch"
        else:
            return "Screen Size: Unknown"
    except ImportError:
        return "Screen Size: Library 'screeninfo' not installed"
def Wifi_mac_address(): 
    try:
        return f"Wi-Fi MAC Address: {getmac.get_mac_address()}"   #Calling the get_mac_address() function from the getmac library to retrieve Wi-Fi MAC address
    except Exception as e:
        return f"Error: {str(e)}"
def public_ip_address():
    try:
        public_ip = socket.gethostbyname(socket.gethostname())
        return f"Public IP Address: {public_ip}"
    except socket.gaierror:
        return "Public IP Address: Not Found"
def windows_version():
    windows_version = platform.platform()
    return f"Windows Version: {windows_version}"

if __name__ == "__main__":
    results = [                       # Calling each function and storing results in a list
        All_installed_software(),
        internet_speed(),
        screen_resolution(),
        cpu_model_info(),
        gpu_Model_info(),
        ram_size(),
        screen_size(),
        Wifi_mac_address(),
        public_ip_address(),
        windows_version()
    ]

    for result in results:     # Printing results
        print(result)
