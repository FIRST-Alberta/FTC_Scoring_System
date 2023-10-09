import PySimpleGUI as sg
from lib.display_manager import Display_Manager
import lib.gui_elements as frames
from lib.common.utilities import Get_Server_Name

display_manager = Display_Manager()
__DISPLAY_SELECTOR__ = sg.Combo(display_manager.displays, expand_x=True, enable_events=True, readonly=True, key='-DISPLAY-')
__ROLES__ = ["audience", "field1", "field2", "inspection", "pit", "sponsor"]
__ROLE_SELECTOR__ = sg.Combo(__ROLES__, expand_x=True, enable_events=True, readonly=True, key="-ROLE-")


layout = [[sg.Text("Display:"), __DISPLAY_SELECTOR__, sg.Button("Update")],
          [sg.Text("New Role:"), __ROLE_SELECTOR__],
          [sg.Text("Event Code:"), sg.Input(key="-EVENT-", expand_x=True)],
          [sg.Text("Server Hostname or IP Address. Defaults to this computer."), sg.Input(expand_x=True, key="server_ip")],
          [frames.__EMPTY_FRAME__],
          [frames.__AUDIENCE_FRAME__],
          [frames.__FIELD_FRAME__],
          [frames.__INSPECTION_FRAME__],
          [frames.__PIT_FRAME__],
          [frames.__SPONSOR_FRAME__],
          [sg.Button("Exit"), sg.Button("Apply"), sg.Button("Restart Display", key="Restart")]]

window = sg.Window("Display Configurator", layout)
visible_frame = "-EMPTY-FRAME-"

while True:
    event, values = window.read()

    # Buttons #
    ###########

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "Update":
        print("Updating")
        display_manager.update_Display_List()
        window["-DISPLAY-"].update(values=display_manager.displays)

    if event == "Apply":
        print("Apply Event")
        print(values)
        if values["-EVENT-"]:
            values["-DISPLAY-"].event_code = values["-EVENT-"]
        else:
            print("Enter an Event Code")
            continue
        if not values["server_ip"]:
            values["server_ip"] = Get_Server_Name()
            print("New Server IP:", values["server_ip"])
        if values["-DISPLAY-"].role != values["-ROLE-"]:
            values["-DISPLAY-"] = display_manager.Change_Display_Role(values["-DISPLAY-"], values["-ROLE-"])
            window["-DISPLAY-"].update(value=values["-DISPLAY-"],values=display_manager.displays)
            
        values["-DISPLAY-"].Apply_Config(values)
        values["-DISPLAY-"].Reload_Services()

    if event == "Restart":
        values["-DISPLAY-"].Reboot_Display()    

    # Combos #
    ##########

    if event == "-DISPLAY-":
        print("Display Selected", values["-DISPLAY-"])
        

    if event == "-ROLE-":
        print(values)
        window[visible_frame].update(visible=False)
        if "audience" in values["-ROLE-"]:
            visible_frame = "-AUDIENCE-FRAME-"
        elif "field" in values["-ROLE-"]:
            visible_frame = "-FIELD-FRAME-"
        elif "inspection" in values["-ROLE-"]:
            visible_frame = "-INSPECTION-FRAME-"
        elif "pit" in values["-ROLE-"]:
            visible_frame = "-PIT-FRAME-"
        elif "sponsor" in values["-ROLE-"]:
            visible_frame = "-SPONSOR-FRAME-"
        window[visible_frame].update(visible=True)


        
    
window.close()