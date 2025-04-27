import dearpygui.dearpygui as dpg
import keyboard , pyautogui,time

def click():
    """функция для клика и выключения кликера"""
    pyautogui.FAILSAFE = False
    while True:
        pyautogui.click()
        time.sleep(0)
        if keyboard.is_pressed('ctrl+/'):
            break

def hot_key():
    """хоткей для включения"""
    keyboard.add_hotkey('ctrl+]',lambda:click())


                    
def main():

    dpg.create_context()

    with dpg.window(tag="Primary Window",autosize=True):

        
        dpg.add_text("AutoClicker",pos=[110,35])
        dpg.add_text("Press 'START' then press:\nCtrl + ] --> Start Cliker\nCtrl + / --> Stop Cliker ",pos=[70,50])
        button = dpg.add_button(label="START",callback=hot_key,pos=[90,100],width=100,height=35)


    dpg.create_viewport(title='Cliker', width=300, height=200)
    dpg.setup_dearpygui()
    dpg.show_viewport() 
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.add_button()
    dpg.destroy_context()
    

if __name__ == '__main__':
    main()