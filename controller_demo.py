from pydualsense import *
import time
from tkinter import * 
from tkinter.ttk import *
import json 
import random
import colorsys
import gc

import autopy

class PixelObject: 
  def __init__(self, x, y, w, h, color):
    self.x = x # changable value 
    self.y = y # changable value 
    self.w = w # changable value 
    self.h = h # changable value 
    
    self._x = x # initial value
    self._y = y # initial value
    self._w = w # initial value
    self._h = h # initial value

    self.color = color

class ControllerPixelObject: 
  def __init__(self, width, height):
    self.width = width
    self.height = height

    self.set_active_and_inactive_color_by_hue(0.5)

    self.l2 = PixelObject(2, 1 , 3, 2, "blue")
    self.l2.boolean_pressed_name = "L2"
    self.l1 = PixelObject(2, 4 , 3, 1, "blue")
    self.l1.boolean_pressed_name = "L1"

    #mirrored
    l2_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.l2))
    self.r2 = PixelObject(l2_mirrored_x_y_w_h[0], l2_mirrored_x_y_w_h[1], l2_mirrored_x_y_w_h[2], l2_mirrored_x_y_w_h[3], "blue")
    self.r2.boolean_pressed_name = "R2"
    l1_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.l1))
    self.r1 = PixelObject(l1_mirrored_x_y_w_h[0], l1_mirrored_x_y_w_h[1], l1_mirrored_x_y_w_h[2], l1_mirrored_x_y_w_h[3], "blue")
    self.r1.boolean_pressed_name = "R1"
    
    #self.dualsense.state.DpadUp
    self.DpadUp = PixelObject(3, 8, 1, 1, "blue")
    self.DpadUp.boolean_pressed_name = "DpadUp"
    #self.dualsense.state.DpadDown
    self.DpadDown = PixelObject(3, 10, 1, 1, "blue")
    self.DpadDown.boolean_pressed_name = "DpadDown"
    #self.dualsense.state.DpadLeft
    self.DpadLeft = PixelObject(2, 9, 1, 1, "blue")
    self.DpadLeft.boolean_pressed_name = "DpadLeft"
    #self.dualsense.state.DpadRight
    self.DpadRight = PixelObject(4, 9, 1, 1, "blue")
    self.DpadRight.boolean_pressed_name = "DpadRight"

    #mirrored
    #self.dualsense.state.triangle
    DpadUp_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.DpadUp))
    self.triangle = PixelObject(DpadUp_mirrored_x_y_w_h[0], DpadUp_mirrored_x_y_w_h[1], DpadUp_mirrored_x_y_w_h[2], DpadUp_mirrored_x_y_w_h[3], "blue")
    self.triangle.boolean_pressed_name = "triangle"
    #self.dualsense.state.cross
    DpadDown_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.DpadDown))
    self.cross = PixelObject(DpadDown_mirrored_x_y_w_h[0], DpadDown_mirrored_x_y_w_h[1], DpadDown_mirrored_x_y_w_h[2], DpadDown_mirrored_x_y_w_h[3], "blue")
    self.cross.boolean_pressed_name = "cross"
    #self.dualsense.state.circle
    DpadLeft_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.DpadLeft))
    self.circle = PixelObject(DpadLeft_mirrored_x_y_w_h[0], DpadLeft_mirrored_x_y_w_h[1], DpadLeft_mirrored_x_y_w_h[2], DpadLeft_mirrored_x_y_w_h[3], "blue")
    self.circle.boolean_pressed_name = "circle"
    #self.dualsense.state.square
    DpadRight_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.DpadRight))
    self.square = PixelObject(DpadRight_mirrored_x_y_w_h[0], DpadRight_mirrored_x_y_w_h[1], DpadRight_mirrored_x_y_w_h[2], DpadRight_mirrored_x_y_w_h[3], "blue")
    self.square.boolean_pressed_name = "square"


    # self.packerC = 0
    # self.square, self.triangle, self.circle, self.cross = False, False, False, False
    # self.DpadUp, self.DpadDown, self.DpadLeft, self.DpadRight = False, False, False, False
    # self.L1, self.L2, self.L3, self.R1, self.R2, self.R3, self.R2Btn, self.L2Btn = False, False, False, False, False, False, False, False
    # self.share, self.options, self.ps, self.touch1, self.touch2, self.touchBtn, self.touchRight, self.touchLeft = False, False, False, False, False, False, False, False
    # self.touchFinger1, self.touchFinger2 = False, False
    # self.RX, self.RY, self.LX, self.LY = 128,128,128,128
    # self.trackPadTouch0, self.trackPadTouch1 = DSTouchpad(), DSTouchpad()

    #self.dualsense.state.share
    self.share = PixelObject(5, 6, 1, 1, "blue")
    self.share.boolean_pressed_name = "share"
    #self.dualsense.state.options
    share_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.share))
    self.options = PixelObject(share_mirrored_x_y_w_h[0], share_mirrored_x_y_w_h[1], share_mirrored_x_y_w_h[2], share_mirrored_x_y_w_h[3], "blue")
    self.options.boolean_pressed_name = "options"
    #left stick
    self.lstick = PixelObject(6, 11, 1, 1, "blue")
    self.lstick.boolean_pressed_name = "L3"

    #right stick
    lstick_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.lstick))
    self.rstick = PixelObject(lstick_mirrored_x_y_w_h[0], lstick_mirrored_x_y_w_h[1], lstick_mirrored_x_y_w_h[2], lstick_mirrored_x_y_w_h[3], "blue")
    self.rstick.boolean_pressed_name = "R3"

    self.touchpad = PixelObject(6, 7, 7, 3, "blue")
    self.touchpad.boolean_pressed_name = "touchBtn"

    self.psbutton = PixelObject(8, 11, 3, 1, "blue")
    self.psbutton.boolean_pressed_name = "ps"

    self.micmutebutton = PixelObject(8, 13, 3, 1, "blue")

    self.touchpadfinger1 = PixelObject(6, 7, 1, 1, "blue")


    self.lborder1 = PixelObject(1, 5, 1, 13, "black")
    self.lborder1.hsv_color = self.hsv_color_inactive

    lborder1_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.lborder1))
    self.rborder1 = PixelObject(lborder1_mirrored_x_y_w_h[0], lborder1_mirrored_x_y_w_h[1], lborder1_mirrored_x_y_w_h[2], lborder1_mirrored_x_y_w_h[3], "black")
    self.rborder1.hsv_color = self.hsv_color_inactive

    self.lbordertop1 = PixelObject(2, 5, 8, 1, "black")
    lbordertop1_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.lbordertop1))
    self.rbordertop1 = PixelObject(lbordertop1_mirrored_x_y_w_h[0], lbordertop1_mirrored_x_y_w_h[1], lbordertop1_mirrored_x_y_w_h[2], lbordertop1_mirrored_x_y_w_h[3], "black")


    self.lborderbottom1 = PixelObject(2, 17, 4, 1, self.hex_color_inactive)
    lborderbottom1_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.lborderbottom1))
    self.rborderbottom1 = PixelObject(lborderbottom1_mirrored_x_y_w_h[0], lborderbottom1_mirrored_x_y_w_h[1], lborderbottom1_mirrored_x_y_w_h[2], lborderbottom1_mirrored_x_y_w_h[3], "black")

    self.lborder2 = PixelObject(5, 17-4, 1, 5, "black")
    lborder2_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.lborder2))
    self.rborder2 = PixelObject(lborder2_mirrored_x_y_w_h[0], lborder2_mirrored_x_y_w_h[1], lborder2_mirrored_x_y_w_h[2], lborder2_mirrored_x_y_w_h[3], "black")

    self.lborder3 = PixelObject(6, 17-4, 1, 1, "black")
    lborder3_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.lborder3))
    self.rborder3 = PixelObject(lborder3_mirrored_x_y_w_h[0], lborder3_mirrored_x_y_w_h[1], lborder3_mirrored_x_y_w_h[2], lborder3_mirrored_x_y_w_h[3], "black")
    
    self.lborder4 = PixelObject(6, 17-3, 4, 1, "black")
    lborder4_mirrored_x_y_w_h = (self.get_mirrored_x_y_w_h(self.lborder4))
    self.rborder4 = PixelObject(lborder4_mirrored_x_y_w_h[0], lborder4_mirrored_x_y_w_h[1], lborder4_mirrored_x_y_w_h[2], lborder4_mirrored_x_y_w_h[3], "black")


  def get_mirrored_x_y_w_h(self, obj):
    return [self.width-(obj.x-2)-obj.w, obj.y, obj.w, obj.h]

  def set_active_and_inactive_color_by_hue(self, hue):
    hsv_color = [hue,1,0.75]
    rgb_color = colorsys.hsv_to_rgb(hsv_color[0], hsv_color[1], hsv_color[2])
    hex_color = ('#%02x%02x%02x'%(round(rgb_color[0]*255),round(rgb_color[1]*255),round(rgb_color[2]*255)))

    self.hex_color_active = hex_color
    self.hsv_color_active = hsv_color

    hsv_color = [hue,1,0.5]
    rgb_color = colorsys.hsv_to_rgb(hsv_color[0], hsv_color[1], hsv_color[2])
    hex_color = ('#%02x%02x%02x'%(round(rgb_color[0]*255),round(rgb_color[1]*255),round(rgb_color[2]*255)))

    self.hex_color_inactive = hex_color
    self.hsv_color_inactive = hsv_color

class App:
  def __init__(self):
    self.controller_pixel_object = ControllerPixelObject(17, 17)

    self.running = True
    self.render_id = 0
    # creating tkinter window 
    self.tk_root = Tk() 
    self.tk_root.title("Python GUI") 
    self.tk_root_w = 500
    self.tk_root_h = 500
    self.tk_root.geometry(str(self.tk_root_w)+"x"+str(self.tk_root_h))

    self.tk_root.protocol("WM_DELETE_WINDOW", self.end)
    # create dualsense
    self.dualsense = pydualsense()
    # find device and initialize
    self.dualsense.init()

    self.trigger_modes = [
    "Off",
    "Rigid",
    "Pulse",
    "Rigid_A",
    "Rigid_B",
    "Rigid_AB",
    "Pulse_A",
    "Pulse_B",
    "Pulse_AB",
    "Calibration"]
    self.trigger_mode = "Off"
    self.trigger_mode_index = 0
    self.trigger_mode_change_delta = 0
    self.trigger_mode_last_change_ts = 0


    # Progress bar widget 
    # self.progress_l = Progressbar(self.tk_root, orient = VERTICAL, length = 100, mode = 'determinate') 
    # self.progress_r = Progressbar(self.tk_root, orient = VERTICAL, length = 100, mode = 'determinate') 
    # self.progress_l.pack(pady = 10)
    # self.progress_r.pack(pady = 10)

    self.label_text = StringVar()
    self.label_text.set("test")
    self.label = Label(self.tk_root, textvariable=self.label_text).place(x=5, y=0)
    #self.label.pack()

    self.label2_text = StringVar()
    self.label2_text.set("test")
    self.label2 = Label(self.tk_root, textvariable=self.label2_text).place(x=5, y=0)
    #self.label2.pack()

    

    # self.button = Button(self.tk_root, text ="close", command = self.end)
    # self.button.pack(pady = 10)

    if(self.controller_pixel_object.width > self.controller_pixel_object.height):
      self.controller_pixel_object_factor = self.tk_root_w / (self.controller_pixel_object.width+2)
    else:
      self.controller_pixel_object_factor = self.tk_root_h /( self.controller_pixel_object.height+2)


    self.tk_canvas = Canvas(self.tk_root, width=self.tk_root_w, height=self.tk_root_h)
    self.tk_canvas.pack()

    self.reset_touchpad_autopy_mouse()

    self.start()

  def end(self):
    #print(TriggerModes.__dict__)
    

    self.running = False
    self.dualsense.close()
    self.tk_root.destroy()
    self.tk_root.quit()


  def render_canvas(self):

    for obj in gc.get_objects():
        if isinstance(obj, PixelObject):
          factor = self.controller_pixel_object_factor
          x0 = obj.x * factor
          y0 = obj.y * factor
          x1 = x0 + obj.w * factor
          y1 = y0 + obj.h * factor
          color = obj.color
          if hasattr(obj, 'boolean_pressed_name'):
            if(getattr(self.dualsense.state, obj.boolean_pressed_name)):
              color = self.controller_pixel_object.hex_color_active
            else: 
              color = self.controller_pixel_object.hex_color_inactive

          self.tk_canvas.create_rectangle(x0, y0, x1, y1, fill=color)

  def reset_touchpad_autopy_mouse(self):
      self.touch0_up = True
      self.touch0_down_autopy_mouse_location = None
      self.touch0_down_dualsense_state_trackpadtouch0_x = None
      self.touch0_down_dualsense_state_trackpadtouch0_y = None
      self.touch0_down_dualsense_state_trackpadtouch0_x_delta = None
      self.touch0_down_dualsense_state_trackpadtouch0_y_delta = None

  def start(self):
      try:
        while self.running:

            self.tk_canvas.delete("all")
            #render canvas
            self.render_canvas()

            self.render_id = self.render_id + 1
    
            #print(dualsense.state.RY)
            if(self.dualsense.state.R1):

                print("move right stick up and down to change force on right rumble")
                self.dualsense.setRightMotor((255-(127+self.dualsense.state.RY)))

                print("move left stick up and down to change force on left rumble")
                self.dualsense.setLeftMotor((255-(127+self.dualsense.state.LY)))
            else: 
                print("move right stick up and down to change force on right rumble")
                self.dualsense.setRightMotor(0)

                print("move left stick up and down to change force on left rumble")
                self.dualsense.setLeftMotor(0)

            if(self.dualsense.state.cross):
              self.trigger_mode_change_delta = time.time() - self.trigger_mode_last_change_ts
              if(self.trigger_mode_change_delta > 0.1):
                self.trigger_mode_last_change_ts = time.time()
                self.trigger_mode_index = (self.trigger_mode_index + 1) % len(self.trigger_modes)
                self.trigger_mode = self.trigger_modes[self.trigger_mode_index]
                


            # self.progress_l['value'] =  (100/255)*(255-(127+self.dualsense.state.LY)) 
            # self.progress_r['value'] =  (100/255)*(255-(127+self.dualsense.state.RY)) 

            self.dualsense.triggerR.setMode(TriggerModes[self.trigger_mode])
            self.dualsense.triggerR.setForce(int(((128+self.dualsense.state.LY)/255)*6), 127+self.dualsense.state.RY)

            self.dualsense.triggerL.setMode(TriggerModes[self.trigger_mode])
            self.dualsense.triggerL.setForce(int(((128+self.dualsense.state.LY)/255)*6), 127+self.dualsense.state.RY)


            self.label_text.set("press x to change, trigger mode:"+str(self.trigger_mode))
            self.tk_root.title("press x to change, trigger mode:"+str(self.trigger_mode)) 

            if(self.dualsense.state.triangle):
                if((self.render_id)%10== 0):
                    #self.dualsense.light.setColorI(random.randint(0,255),random.randint(0,255), random.randint(0,255))
                    random_hsv = [(1/100)*random.randint(0,100),1,1]
                    self.controller_pixel_object.set_active_and_inactive_color_by_hue(random_hsv[0])
                    random_color = colorsys.hsv_to_rgb(random_hsv[0], random_hsv[1], random_hsv[2])
                    #self.dualsense.light.setColorI(int(random_color[0]*255), int(random_color[1]*255), int(random_color[2]*255))
                    self.dualsense.light.setColorI(int(random_color[0]*255), int(random_color[1]*255), int(random_color[2]*255))
                    for obj in gc.get_objects():
                      if isinstance(obj, PixelObject):
                        obj.color = self.controller_pixel_object.hex_color_inactive
              
              #print(Brightness.__dict__)#{'_generate_next_value_': <function Flag._generate_next_value_ at 0x00000225991D83A0>, '__module__': 'pydualsense.enums', '__doc__': 'An enumeration.', '_member_names_': ['high', 'medium', 'low'], '_member_map_': {'high': <Brightness.high: 0>, 'medium': <Brightness.medium: 1>, 'low': <Brightness.low: 2>}, '_member_type_': <class 'int'>, '_value2member_map_': {0: <Brightness.high: 0>, 1: <Brightness.medium: 1>, 2: <Brightness.low: 2>}, 'high': <Brightness.high: 0>, 'medium': <Brightness.medium: 1>, 'low': <Brightness.low: 2>, '__new__': <function Enum.__new__ at 0x00000225991D5CA0>}
            else:
              if(self.odd_frame_ids(20)):
                #autopy.mouse.move(200,200)
                self.dualsense.light.setBrightness(Brightness.low)
              else:
                self.dualsense.light.setBrightness(Brightness.high)

            if(self.dualsense.state.L1):
              self.controller_pixel_object.l1.color = self.controller_pixel_object.hex_color_active
            else:
              self.controller_pixel_object.l1.color = self.controller_pixel_object.hex_color_inactive


            self.controller_pixel_object.rstick.x = self.controller_pixel_object.rstick._x + (1/127)*self.dualsense.state.RX
            self.controller_pixel_object.rstick.y = self.controller_pixel_object.rstick._y + (1/127)*self.dualsense.state.RY

            self.controller_pixel_object.lstick.x = self.controller_pixel_object.lstick._x + (1/127)*self.dualsense.state.LX
            self.controller_pixel_object.lstick.y = self.controller_pixel_object.lstick._y + (1/127)*self.dualsense.state.LY            
            
            self.controller_pixel_object.lborder1.hsv_color[2] = ((self.controller_pixel_object.lborder1.hsv_color[2] + (((self.dualsense.leftMotor+1)/(255+1))*0.1) )) % 0.5 + 0.5
            rgb_color = colorsys.hsv_to_rgb(self.controller_pixel_object.lborder1.hsv_color[0], self.controller_pixel_object.lborder1.hsv_color[1], self.controller_pixel_object.lborder1.hsv_color[2])
            hex_color = ('#%02x%02x%02x'%(round(rgb_color[0]*255),round(rgb_color[1]*255),round(rgb_color[2]*255)))
            self.controller_pixel_object.lborder1.color = hex_color

            self.controller_pixel_object.rborder1.hsv_color[2] = ((self.controller_pixel_object.rborder1.hsv_color[2] + (((self.dualsense.rightMotor+1)/(255+1))*0.1) )) % 0.5 + 0.5
            rgb_color = colorsys.hsv_to_rgb(self.controller_pixel_object.rborder1.hsv_color[0], self.controller_pixel_object.rborder1.hsv_color[1], self.controller_pixel_object.rborder1.hsv_color[2])
            hex_color = ('#%02x%02x%02x'%(round(rgb_color[0]*255),round(rgb_color[1]*255),round(rgb_color[2]*255)))
            self.controller_pixel_object.rborder1.color = hex_color

            if(self.dualsense.state.touchBtn):
              autopy.mouse.click()

            self.controller_pixel_object.touchpadfinger1.color = self.controller_pixel_object.hex_color_inactive

            if(self.dualsense.state.trackPadTouch0.isActive == True):
              self.controller_pixel_object.touchpadfinger1.color = self.controller_pixel_object.hex_color_active
              if(self.touch0_down_autopy_mouse_location == None):
                self.touch0_down_autopy_mouse_location = autopy.mouse.location() 
                self.touch0_down_dualsense_state_trackpadtouch0_x = self.dualsense.state.trackPadTouch0.X
                self.touch0_down_dualsense_state_trackpadtouch0_y = self.dualsense.state.trackPadTouch0.Y
              else:
                self.touch0_up = False
                #trackpad has FullHD 1920 x 1080 :0
                self.label2_text.set(str(self.dualsense.state.trackPadTouch0.X)+":"+str(self.dualsense.state.trackPadTouch0.Y))
                
                self.touch0_down_dualsense_state_trackpadtouch0_x_delta = self.touch0_down_dualsense_state_trackpadtouch0_x - self.dualsense.state.trackPadTouch0.X
                self.touch0_down_dualsense_state_trackpadtouch0_y_delta = self.touch0_down_dualsense_state_trackpadtouch0_y - self.dualsense.state.trackPadTouch0.Y
                mouse_move_sensitivity = 0.5
                autopy.mouse.move(self.touch0_down_autopy_mouse_location[0]-(self.touch0_down_dualsense_state_trackpadtouch0_x_delta*mouse_move_sensitivity),self.touch0_down_autopy_mouse_location[1]-(self.touch0_down_dualsense_state_trackpadtouch0_y_delta*mouse_move_sensitivity))

                finger_x = ((self.controller_pixel_object.touchpad.w-1) / 1920) * self.dualsense.state.trackPadTouch0.X
                finger_y = ((self.controller_pixel_object.touchpad.h-1) / 1080) * self.dualsense.state.trackPadTouch0.Y
                
                self.controller_pixel_object.touchpadfinger1.x = self.controller_pixel_object.touchpadfinger1._x + finger_x
                self.controller_pixel_object.touchpadfinger1.y = self.controller_pixel_object.touchpadfinger1._y + finger_y
            else:
              if(self.touch0_down_autopy_mouse_location != None):
                self.reset_touchpad_autopy_mouse()
              
            self.tk_root.update_idletasks()
            self.tk_root.update()
            time.sleep(0.001)

            #self.dualsense.light.setPulseOption(PulseOptions.FadeBlue)

            #print(LedOptions.__dict__)
            #print(PulseOptions.__dict__)
            #self.label_text.set((self.state.trackPadTouch0.X))

      except KeyboardInterrupt:
        pass

  def odd_frame_ids(self, frame_ids):
      return int(self.render_id/frame_ids)%2 == 0









app = App()