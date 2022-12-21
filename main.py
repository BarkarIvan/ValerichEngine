from config import *
import instance
import logging
import device



class Engine:

    def __init__(self):

        self.debugMode = True

        # glfw window parms
        self.width = 800
        self.height = 600

        if self.debugMode:
            print("Making a Valerich Engine")

        self.build_glfw_window()
        self.make_instance()
        self.make_device()


    def build_glfw_window(self):
        # init glfw
        glfw.init()

        # no default client, we will hook vulkan up to windows later
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CLIENT_API, GLFW_CONSTANTS.GLFW_NO_API)
        # resize break swaphain, turn off
        glfw.window_hint(GLFW_CONSTANTS.GLFW_RESIZABLE, GLFW_CONSTANTS.GLFW_FALSE)

        # get window
        self.window = glfw.create_window(self.width, self.height, "Valerich Engine", None, None)
        if self.window is not None:
            if self.debugMode:
                print("window created\n")
        else:
            if self.debugMode:
                print("glfw window creation filed\n")

    def make_instance(self):
        self.instance = instance.make_instance(self.debugMode, "Valerich engine")

        if self.debugMode:
            self.debugMessenger = logging.make_debug_messenger(self.instance)


    def make_device(self):
        self.physicalDevice = device.choose_physical_device(self.instance, self.debugMode)

    def close(self):
        if self.debugMode:
            print("Bye\n")

        if self.debugMode:
            destuctionFunction = vkGetInstanceProcAddr(self.instance, 'vkDestroyDebugReportCallbackEXT')
            destuctionFunction(self.instance, self.debugMessenger, None)

        vkDestroyInstance(self.instance, None)

        # termintate glfw
        glfw.terminate()


if __name__ == "__main__":
    graphicEngine = Engine()
    graphicEngine.close()
