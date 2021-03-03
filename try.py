from __future__ import print_function

import hid
import time
import os
import itertools
from tkinter import * 
from tkinter.ttk import *
import json 
import random
import colorsys
import gc

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


class CombObj:
    pass

class BoolButton:
  def __init__(self, int_val, bool_val):
      self.int_val = 0
      self.bool_val = False

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

  def end(self):
    #print(TriggerModes.__dict__)
    

    self.running = False
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

"""
so 
"""
class Dualsense:
    def __init__(self):

        self.int_max = 255

        self.bool_d_pad_up = False
        self.bool_d_pad_down = False
        self.bool_d_pad_left = False
        self.bool_d_pad_right = False

        self.bool_d_triangle = False
        self.bool_d_cross = False
        self.bool_d_square = False
        self.bool_d_circle = False

        self.bool_share = False
        self.bool_options = False

        self.bool_l3 = False
        self.bool_r3 = False

        self.bool_l1 = False
        self.bool_r1 = False

        self.bool_ps = False

        self.bool_mic = False

        self.int_analog_stick_left_axis_x = int(self.int_max/2)
        self.int_analog_stick_left_axis_y = int(self.int_max/2)
        self.int_analog_stick_right_axis_y = int(self.int_max/2)
        self.int_analog_stick_right_axis_y = int(self.int_max/2)

        self.int_trigger_l = int(self.int_max/2)
        self.int_trigger_r = int(self.int_max/2)

        self.bool_touchpad = False

        self.int_touchpad_x = int(self.int_max/2)
        self.int_touchpad_y = int(self.int_max/2)


        self.int_l1 = BoolButton(1, False)
        self.int_r1 = BoolButton(2, False)

        self.int_l12_array = [self.int_l1, self.int_r1]

        self.int_l12_combinations = self.get_comb_obj(self.int_l12_array)

        

        # now get the combinations


    def get_comb_obj(self, array):
        combos = self.get_combination_values(array)

        for val in combos:
            cmboj = CombObj()

            sum_val = 0

            for val2 in val:
                sum_val = sum_val + val2.int_val
                
            #cmboj.settart("sum_val_"+sum_val, val)

        return True

    """
    return a new array with all combinations
    """
    def get_combination_values(self,array):
        comb = []
        for i in range(len(array)):
            comb += itertools.combinations(array,i+1)

        return comb


def draw_progress_bar(min, max, value, highlight = False):
    width = max
    value_width = (value / max) * width
    ostr = ""
    # wtf c++ ... wtf -> 111/222 will return 0 , double(111)/222 will return 0.5... wtf
    for i in range(width):
        if (i == 0):
            ostr  += ("[")
        
        if(i == width - 1):
            ostr += ("]")
            break

        if (i < value_width):
            ostr += ("=")
        else:   
            ostr += (" ")
    
    ostr += " : " + str(value).rjust(len(str(max))+1, ' ') +" / "+str(max)

    ostr += " | binary : "+ '{0:08b}'.format(value) +" / " + '{0:08b}'.format(255)

    if(highlight):
        ostr = '\x1b[6;30;43m' + ostr + '\x1b[0m'

    print(ostr)

# enumerate USB devices

for d in hid.enumerate():
    keys = list(d.keys())
    keys.sort()
    for key in keys:
        print("%s : %s" % (key, d[key]))
    print()

# try opening a device, then perform write and read

try:

    
    print("Opening the device")
    
    app = App()

    h = hid.device()
    h.open(0x054c, 0x0CE6)  # TREZOR VendorID/ProductID

    # interface_number : 3
    # manufacturer_string : Sony Interactive Entertainment
    # path : b'IOService:/AppleACPIPlatformExpert/PCI0@0/AppleACPIPCI/XHC1@14/XHC1@14000000/HS09@14400000/Wireless Controller@14400000/IOUSBHostInterface@3/IOUSBHostHIDDevice@14400000,3'
    # product_id : 3302
    # product_string : Wireless Controller
    # release_number : 256
    # serial_number : 
    # usage : 5
    # usage_page : 1
    # vendor_id : 1356

    print("Manufacturer: %s" % h.get_manufacturer_string())
    print("Product: %s" % h.get_product_string())
    #print("Serial No: %s" % h.get_serial_number_string())

    dualsense = Dualsense()
    print("Closing the device")

    # enable non-blocking mode
    h.set_nonblocking(1)

    # write some data to the device
    #print("Write the data")
    #h.write([0, 63, 35, 35] + [0] * 61)

    # wait
    time.sleep(0.05)

    # read back the answer
    print("Read the data")

    while True:
        d = h.read(64)
        if d:
            print(d)
        else:
            break

    try:
        c = 0 
        while c < 5000:
            c= c+1
            print(c)
            time.sleep(0.1)
            d_len = 128
            d = h.read(d_len)
            d_slice_len = int(d_len / 2)
            d_slice_min = int(d_slice_len * 1)
            d_slice_max = int(d_slice_min + d_slice_len)
            d_sliced = d[(d_slice_min):(d_slice_max)]

            d_slice_min = 0
            d_slice_max = 70
            d_sliced = d[(d_slice_min):(d_slice_max)]



            os.system('cls' if os.name == 'nt' else 'clear')
            print("output data of ["+str(d_slice_min)+":"+str(d_slice_max)+"]")

            rightthumbbuttons = d[8]
            
            state = (rightthumbbuttons & (1 << 7)) != 0


            print("biwise operated ")
            print(state)


            highlight_text = False
            for i, val in enumerate(d_sliced):
                if(i == 0):
                    continue
                if(i == 8):
                    highlight_text = True
                else:
                    highlight_text = False

                print("["+str(i).rjust(3, ' ')+"]", end="")

                draw_progress_bar(0, 255, val, highlight_text)

            #left analog stick
            # 1: x-axis
            dualsense.int_analog_stick_left_axis_x = d[1]
            # 2: y-axis
            dualsense.int_analog_stick_left_axis_x = d[2]
            # right analog stick
            # 3: x-axis
            dualsense.int_analog_stick_left_axis_x = d[3]
            # 4: y-axis
            dualsense.int_analog_stick_left_axis_x = d[4]

            dualsense.int_touchpad_y = d[36]

            # triggers on the back
            dualsense.int_trigger_l = d[5]
            dualsense.int_trigger_l = d[6]

            # cross square triangle circle d[8]
            # bit true position of

            #   8: 0b 0000100: nothing pressed
            #  24: 0b 0001100: square
            #  40: 0b 0010100: cross 
            #  72: 0b 0100100: circle
            # 136: 0b 1000100: triangle

            #now we can use bitoperations bit shift
            left_buttons_state = d[8]

            dualsense.bool_d_square = (left_buttons_state & (1 << 3)) != 0
            dualsense.bool_d_cross = (left_buttons_state & (1 << 4)) != 0
            dualsense.bool_d_circle = (left_buttons_state & (1 << 5)) != 0
            dualsense.bool_d_triangle = (left_buttons_state & (1 << 6)) != 0

            dualsense.bool_touchpad = True if d[10] == 2 else False

            if(d[9] == 1):
                dualsense.bool_l1 = True
            
            if(d[9] == 2):
                dualsense.bool_r1 = True
            
            if(d[9] == 3):
                dualsense.bool_l1 = True
                dualsense.bool_r1 = True
            
            if(dualsense.int_analog_stick_left_axis_x == 255):
                break
            

    except KeyboardInterrupt:
        pass

    print("Closing the device")
    h.close()

except IOError as ex:
    print(ex)
    print("You probably don't have the hard-coded device.")
    print("Update the h.open() line in this script with the one")
    print("from the enumeration list output above and try again.")

print("Done")




