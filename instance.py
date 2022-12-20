from config import *


def supported(extensions, layers, debug):
    supportedExtensions = [extensions.extensionName for extensions in vkEnumerateInstanceExtensionProperties(None)]
    supportedLayers = [layer.layerName for layer in vkEnumerateInstanceLayerProperties()]

    if debug:
        print("Device can suport following extensions:")
        for supportedExtension in supportedExtensions:
            print(f"\t\"{supportedExtension}\"")
        print("Device can support the following layers:")
        for supportedLayer in supportedLayers:
            print(f"\t\"{supportedLayer}\"")

    for extension in extensions:
        if extension in supportedExtensions:
            if debug:
                print(f"Extension \"{extension}\" is supported")
            else:
                if debug:
                    print(f"Extension \"{extension}\" is not supported")
                return False

    for layer in layers:
        if layer in supportedLayers:
            if debug:
                print(f"Layer \"{layer}\" is supported")
            else:
                if debug:
                    print(f"Layer \"{layer}\" is not supported")
                return False
    return True


def make_instance(debug, applicationName):
    version = vkEnumerateInstanceVersion()
    if debug:
        print(f"System can support vulkan var: {version >> 29}\
        , Major: {VK_VERSION_MAJOR(version)}\
        , Minor: {VK_VERSION_MINOR(version)}\
        , Patch: {VK_VERSION_PATCH(version)}"
              )
    version = VK_MAKE_VERSION(1, 0, 0)

    appInfo = VkApplicationInfo(
        pApplicationName=applicationName,
        applicationVersion=version,
        pEngineName="Doing it",
        engineVersion=version,
        apiVersion=version
    )

    # evrth with vulkan is opt-in. we need query which extension gltf need in order to interface with vulkan
    extensions = glfw.get_required_instance_extensions()

    if debug:
        extensions.append(VK_EXT_DEBUG_REPORT_EXTENSION_NAME)

    if debug:
        print(f"extensions:")
        for extensionName in extensions:
            print(f"\t\"{extensionName}\"")

    layers = []
    if debug:
        layers.append("VK_LAYER_KHRONOS_validation")

    supported(extensions, layers, debug)

    createInfo = VkInstanceCreateInfo(
        pApplicationInfo=appInfo,
        enabledLayerCount=len(layers), ppEnabledLayerNames=layers,
        enabledExtensionCount=len(extensions), ppEnabledExtensionNames=extensions
    )

    try:
        return vkCreateInstance(createInfo, None)
    except:
        if (debug):
            print("Fail crate VK instance")
        return None
