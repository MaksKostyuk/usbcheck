import wmi

c = wmi.WMI()

def get_power_management(device_id):
    try:
        pm_settings = c.query(
            f"SELECT * FROM Win32_PowerManagementEvent WHERE InstanceName LIKE '%{device_id.replace('\\\\', '\\\\\\\\')}%'"
        )
        return len(pm_settings) > 0
    except Exception:
        return False

def get_usb_devices():
    devices = []
    usb_devices = c.Win32_USBControllerDevice()
    for usb_device in usb_devices:
        device = usb_device.Dependent
        device_info = {
            "DeviceID": device.DeviceID,
            "PNPDeviceID": device.PNPDeviceID,
            "Description": device.Description,
            "Manufacturer": getattr(device, "Manufacturer", "Unknown"),
            "Status": getattr(device, "Status", "Unknown"),
            "PowerManagementSupported": get_power_management(device.DeviceID)
        }
        devices.append(device_info)
    return devices

def main():
    print("Created by https://t.me/nonstop4ek")
    print("=" * 40)
    
    devices = get_usb_devices()
    for idx, device in enumerate(devices, 1):
        print(f"Device #{idx}:")
        print(f"  Description: {device['Description']}")
        print(f"  DeviceID: {device['DeviceID']}")
        print(f"  PNPDeviceID: {device['PNPDeviceID']}")
        print(f"  Manufacturer: {device['Manufacturer']}")
        print(f"  Status: {device['Status']}")
        print(f"  Power Management Supported: {device['PowerManagementSupported']}")
        print("-" * 40)

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
