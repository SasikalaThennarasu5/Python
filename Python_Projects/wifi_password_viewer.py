import subprocess

def get_saved_wifi_passwords():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode()
        profiles = [line.split(":")[1].strip() for line in result.split("\n") if "All User Profile" in line]

        for profile in profiles:
            try:
                wifi_info = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode()
                for line in wifi_info.split("\n"):
                    if "Key Content" in line:
                        password = line.split(":")[1].strip()
                        yield f"SSID: {profile} | Password: {password}"
            except subprocess.CalledProcessError:
                yield f"SSID: {profile} | Password: <Access Denied or Not Available>"
    except Exception as e:
        yield f"Error: {str(e)}"

if __name__ == "__main__":
    for wifi in get_saved_wifi_passwords():
        print(wifi)
