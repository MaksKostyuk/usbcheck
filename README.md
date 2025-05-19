# usbcheck

# USB Device Checker

A Python script that detects USB devices connected to a Windows machine and displays detailed information about each device using WMI (Windows Management Instrumentation).

## Features

- Lists all connected USB devices
- Displays device description, DeviceID, PNPDeviceID, manufacturer, and status
- Checks if the device supports Power Management
- Waits for user input before exiting to allow you to review the output

## Requirements

- Windows OS
- Python 3.x
- `wmi` Python module

## Installation

1. Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Install the `wmi` module using pip:

   ```bash
   pip install wmi
