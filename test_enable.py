"""Test script for enable/disable monitor functionality."""
from monitor_api import (
    get_monitors, get_all_display_devices, get_connected_device_names,
    get_all_device_names, enable_monitor, disable_monitor, get_best_display_mode,
    MonitorInfo
)

def test_enable_display(device_name: str):
    """Test enabling a specific display."""
    print(f"\n{'='*60}")
    print(f"Testing enable for: {device_name}")
    print(f"{'='*60}")

    # Check if device exists
    all_devices = get_all_device_names()
    if device_name not in all_devices:
        print(f"ERROR: {device_name} not found in available devices")
        return

    connected = get_connected_device_names()
    if device_name in connected:
        print(f"{device_name} is already connected/active")
        return

    print(f"{device_name} is DETACHED, attempting to enable...")

    # Check for available modes
    best_mode = get_best_display_mode(device_name, 1920, 1080, 60)
    if best_mode:
        print(f"Found display mode: {best_mode.dmPelsWidth}x{best_mode.dmPelsHeight} @ {best_mode.dmDisplayFrequency}Hz")
    else:
        print("No matching display mode found, will try fallback")

    # Create a test MonitorInfo
    test_monitor = MonitorInfo(
        device_name=device_name,
        device_string="Test",
        width=1920,
        height=1080,
        position_x=2560,  # To the right of primary
        position_y=0,
        refresh_rate=60,
        orientation=0,
        bits_per_pixel=32,
        is_primary=False,
        is_active=False,
        enabled=True
    )

    success = enable_monitor(device_name, test_monitor, use_noreset=False)
    print(f"Result: {'SUCCESS' if success else 'FAILED'}")


if __name__ == "__main__":
    print("Current display state:")
    print("-" * 40)
    for dev in get_all_display_devices():
        status = "ATTACHED" if dev["attached"] else "DETACHED"
        modes = "has_modes" if dev["has_modes"] else "no_modes"
        print(f"  {dev['name']}: [{status}] [{modes}]")

    print("\nActive monitors:")
    for m in get_monitors():
        print(f"  {m}")

    # Find a detached display with modes to test
    print("\n" + "="*60)
    print("Looking for a detached display to test enable...")
    for dev in get_all_display_devices():
        if not dev["attached"] and dev["has_modes"]:
            print(f"Found: {dev['name']} ({dev['string']})")
            response = input(f"Try to enable {dev['name']}? (y/n): ")
            if response.lower() == 'y':
                test_enable_display(dev['name'])
            break
    else:
        print("No detached displays with valid modes found.")
