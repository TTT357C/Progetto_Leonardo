# Import SerialWriter from serial_write_module
from serial_write_module import SerialWriter as sw
from Talker import Talker

def read_api_key():
    try:
        with open('api.ttt', 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        print("Error: api.ttt file not found")
        return None
    except Exception as e:
        print(f"Error reading api.ttt: {e}")
        return None

api_key = read_api_key()


el1 = Talker("MhCxqsUNqPcgb5bNYy5r", api_key, False)

def initialize():
    def select_module():
        # Display module selection menu
        print("Select a module:")
        print("1. MQTT")
        print("2. GUI")
        print("3. KEY")
        module_choice = input("Enter your choice (1,2,3): ")

        # Use match-case to handle module selection
        match module_choice:
            case "1":
                el1.talk("MQTT module selected")
                # Import MQTT module
                from mqtt_read_module import Module as Mod
                return Mod
            case "2":
                el1.talk("GUI module selected")
                # Import GUI module
                from gui_read_module import Module as Mod
                return Mod
            case "3":
                el1.talk("Keyboard module selected")
                # Import KEY module
                from keyboard_read_module import Module as Mod
                return Mod
            case _:
                # Handle invalid selection
                print("Error: Invalid module selection")
                return None

    return select_module()

if __name__ == "__main__":
    # Initialize the selected module
    module = initialize()
    # Create an instance of SerialWriter
    #serial_bridge = sw()
    el1.talk("Module successfully initialized")
    el1.talk("Starting serial communication")
    if module:
        # Create an instance of the selected module
        module_instance = module()
        print(module_instance.name)
        while True:
            # Read data from the module
            ret = module_instance.read()
            if(ret != None):
                print(ret)
                try:
                    # Send the received data through the serial bridge
                    serial_bridge.send_string(ret)
                except:
                    print("Error: Failed to send string to serial bridge")
                
        
    else:
        print("Failed to initialize module")
