from config import *


def log_device_properties(device):
    properties = vkGetPhysicalDeviceProperties(device)

    print(f"Device name: {properties.deviceName}")
    print ("Device type: ", end="")
    if properties.deviceType == VK_PHYSICAL_DEVICE_TYPE_CPU:
        print("CPU")
    elif properties.deviceType == VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU:
        print("Discrete GPU")
    elif properties.deviceType == VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU:
        print("Integrated GPU")
    elif properties.deviceType == VK_PHYSICAL_DEVICE_TYPE_VIRTUAL_GPU:
        print("Virtual GPU")
    else:
        print("Other")


def check_device_extension_support(device, requestedExtension, debug):
    supportExtensions = [extension.extensionName for extension in vkEnumerateDeviceExtensionProperties(device, None)]

    if debug:
        print("Device can support extensions:")

    for extension in supportExtensions:
        print(f"\t\"{extension}\"")

    for extension in requestedExtension:
        if extension not in supportExtensions:
            return False
    return True


def is_suitable(device, debug):
    #suitable if can present to the screen, support swapchain
    requestedExtension = [VK_KHR_SWAPCHAIN_EXTENSION_NAME]

    if debug:
        print("We are requested device extension:")
        for extension in requestedExtension:
            print(f"\t\"{extension}\"")

    if check_device_extension_support(device, requestedExtension, debug):
        if debug:
            print("Device can support requested extensions")
            return True
    if debug:
        print("Device dont support requested extensions")
    return False



def choose_physical_device(instance, debug):

    if debug:
        print("choose physical device")

    availableDevices = vkEnumeratePhysicalDevices(instance)

    if debug:
        print(f"There are {len(availableDevices)} physical devices on this system")
    
    #check if a suitable divice can be found

    for device in availableDevices:
        if debug:
            log_device_properties(device)
        if is_suitable(device, debug):
            return device
    return None