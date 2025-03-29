import os
import json
import socket
import getpass
import winreg

# Collect data on the user of the computer
username = getpass.getuser()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

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
