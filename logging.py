from config import *


def debugCallback(*args):
    # print(f"Debug message has {len(args)} components")
    # for arg in args:

    #validation layers
    print(f"Debug:{args[5]} + ' ' + {args[6]}")
    return 0


def make_debug_messenger(instance):

    createInfo = VkDebugReportCallbackCreateInfoEXT(
        flags=VK_DEBUG_REPORT_ERROR_BIT_EXT | VK_DEBUG_REPORT_WARNING_BIT_EXT,
        pfnCallback=debugCallback
    )

    # fetch creation function
    creationFunction = vkGetInstanceProcAddr(instance, 'vkCreateDebugReportCallbackEXT')

    return creationFunction(instance, createInfo, None)



