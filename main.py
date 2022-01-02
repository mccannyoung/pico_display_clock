import utime
import picodisplay as display

def get_pen_binary_color(number):
    if number == "0":
        return display.create_pen(255, 255, 255)
    else:
        return display.create_pen(0, 255, 0)
    
def time_getbinary(time): #this is for the pseudo-binary option
    tens = f'0b{((time//10)%10):04b}'[2:]
    ones = f'0b{(time%10):04b}'[2:]
    return tens, ones

def draw_bi(hour, minute, second):
    display.set_pen(0,0,0)
    display.clear()
    display.set_pen(255, 255, 255)

    seconds_bi = f'0b{second:06b}'[2:]
    minutes_bi = f'0b{minute:06b}'[2:]
    hours_bi = f'0b{hour:06b}'[2:]
    
    ## Seconds
    display.set_pen(get_pen_binary_color(seconds_bi[5]))
    display.circle(220, 16, 10)
    display.set_pen(get_pen_binary_color(seconds_bi[4]))
    display.circle(180, 16, 10)
    display.set_pen(get_pen_binary_color(seconds_bi[3]))
    display.circle(140, 16, 10)
    display.set_pen(get_pen_binary_color(seconds_bi[2]))
    display.circle(100, 16, 10)
    display.set_pen(get_pen_binary_color(seconds_bi[1]))
    display.circle(60, 16, 10)
    display.set_pen(get_pen_binary_color(seconds_bi[0]))
    display.circle(20, 16, 10)
    ## Minutes
    display.set_pen(get_pen_binary_color(minutes_bi[5]))
    display.circle(220, 56, 10)
    display.set_pen(get_pen_binary_color(minutes_bi[4]))
    display.circle(180, 56, 10)
    display.set_pen(get_pen_binary_color(minutes_bi[3]))
    display.circle(140, 56, 10)
    display.set_pen(get_pen_binary_color(minutes_bi[2]))
    display.circle(100, 56, 10)
    display.set_pen(get_pen_binary_color(minutes_bi[1]))
    display.circle(60, 56, 10)
    display.set_pen(get_pen_binary_color(minutes_bi[0]))
    display.circle(20, 56, 10)
    ## Hours
    display.set_pen(get_pen_binary_color(hours_bi[5]))
    display.circle(220, 96, 10)
    display.set_pen(get_pen_binary_color(hours_bi[4]))
    display.circle(180, 96, 10)
    display.set_pen(get_pen_binary_color(hours_bi[3]))
    display.circle(140, 96, 10)
    display.set_pen(get_pen_binary_color(hours_bi[2]))
    display.circle(100, 96, 10)
    display.set_pen(get_pen_binary_color(hours_bi[1]))
    display.circle(60, 96, 10)
    display.set_pen(get_pen_binary_color(hours_bi[0]))
    display.circle(20, 96, 10)
    display.update()          # Update the display
    return

def display_plain(hour, minute, second):
    display.set_pen(0,0,0)
    display.clear()
    display.set_pen(255, 255, 255)
    display.text(f'{hour:02}'+":"+f'{minute:02}', 25, 35, 240, 8)
    display.update()
    return

def draw_display(hour, minute, second):
    display.set_pen( 0, 0, 0)  # Set pen to a converted HSV value
    display.clear()           # Fill the screen with the colour
    tenseconds_binary, seconds_binary = time_getbinary(second)
    tenminutes_binary, minutes_binary = time_getbinary(minute)
    tenhours_binary, hours_binary = time_getbinary(hour)

    size = 10
    
    seconds =  220
    tenseconds = 180
    minutes = 140
    tenminutes = 100
    hours = 60
    tenhours = 20
    
    one_row = 106
    two_row = 76
    four_row = 46
    eight_row = 16
    
    # seconds dots
    display.set_pen(get_pen_binary_color(seconds_binary[3]))
    display.circle(seconds, one_row, size)
    display.set_pen(get_pen_binary_color(seconds_binary[2]))
    display.circle(seconds, two_row, size)
    display.set_pen(get_pen_binary_color(seconds_binary[1]))
    display.circle(seconds, four_row, size)
    display.set_pen(get_pen_binary_color(seconds_binary[0]))
    display.circle(seconds, eight_row, size)

    # 10 seconds dots
    display.set_pen(get_pen_binary_color(tenseconds_binary[3]))
    display.circle(tenseconds, one_row, size)
    display.set_pen(get_pen_binary_color(tenseconds_binary[2]))
    display.circle(tenseconds, two_row, size)
    display.set_pen(get_pen_binary_color(tenseconds_binary[1]))
    display.circle(tenseconds, four_row, size)
    #disabled
    display.set_pen(75, 75, 75)
    display.circle(tenseconds, eight_row, size)

    # minutes dots
    display.set_pen(get_pen_binary_color(minutes_binary[3]))
    display.circle(minutes, one_row, size)
    display.set_pen(get_pen_binary_color(minutes_binary[2]))
    display.circle(minutes, two_row, size)
    display.set_pen(get_pen_binary_color(minutes_binary[1]))
    display.circle(minutes, four_row, size)
    display.set_pen(get_pen_binary_color(minutes_binary[0]))
    display.circle(minutes, eight_row, size)

    # 10 minutes dots
    display.set_pen(get_pen_binary_color(tenminutes_binary[3]))
    display.circle(tenminutes, one_row, size)
    display.set_pen(get_pen_binary_color(tenminutes_binary[2]))
    display.circle(tenminutes, two_row, size)
    display.set_pen(get_pen_binary_color(tenminutes_binary[1]))
    display.circle(tenminutes, four_row, size)
    #disabled
    display.set_pen(75, 75, 75)
    display.circle(tenminutes, eight_row, size)

    # hours dots
    display.set_pen(get_pen_binary_color(hours_binary[3]))
    display.circle(hours, one_row, size)
    display.set_pen(get_pen_binary_color(hours_binary[2]))
    display.circle(hours, two_row, size)
    display.set_pen(get_pen_binary_color(hours_binary[1]))
    display.circle(hours, four_row, size)
    display.set_pen(get_pen_binary_color(hours_binary[0]))
    display.circle(hours, eight_row, size)
    
    # 10 hours dots
    display.set_pen(get_pen_binary_color(tenhours_binary[3]))
    display.circle(tenhours, one_row, size)
    display.set_pen(get_pen_binary_color(tenhours_binary[2]))
    display.circle(tenhours, two_row, size)
    #disabled
    display.set_pen(75, 75, 75)
    display.circle(tenhours, four_row, size)
    display.circle(tenhours, eight_row, size)

    display.update()
    return
    
# Set up and initialise Pico Display
buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)
display.set_backlight(0.3)
 
display.set_pen( 0, 0, 0)  # Set pen to a converted HSV value
display.clear()           # Fill the screen with the colour

rtc = machine.RTC()
rtc.datetime((1970, 1, 1, 0, 0, 0, 0, 0))

year, month, day, unsure, hour, minute, second, millisecondmaybe = rtc.datetime()
cSec = second
display.set_led(0, 0, 125)
display_mode = 0
while True:
    utime.sleep_ms(250) #this is to limit the button sensitivity
    year, month, day, unsure, hour, minute, second, millisecondmaybe = rtc.datetime()
    if second != cSec:
        cSec = second
        if display_mode == 0:
            draw_display(hour, minute, second)
        if display_mode == 1:
            draw_bi(hour,minute,second)
        if display_mode == 2:
            display_plain(hour,minute,second)
            
    if display.is_pressed(display.BUTTON_A):
        if(hour != 23):
            rtc.datetime((year,month,day,unsure,hour+1,minute,second,millisecondmaybe))
        else:
            rtc.datetime((year,month,day,unsure,0,minute,second,millisecondmaybe))
    if display.is_pressed(display.BUTTON_B):
        if (minute != 59):
            rtc.datetime((year,month,day,unsure,hour,minute+1,second,millisecondmaybe))
        else:
            rtc.datetime((year,month,day,unsure,hour+1,0,second,millisecondmaybe))
    if display.is_pressed(display.BUTTON_X):
        if display_mode < 2:
            display_mode = display_mode+1
        else:
            display_mode = 0
    if display.is_pressed(display.BUTTON_Y):
        rtc.datetime((1970, 1, 1, 0, 0, 0, 0, 0)) #reset the time back to midnight
