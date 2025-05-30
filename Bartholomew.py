def forwards():# drives forward
 motor_8.spin(REVERSE)
 motor_20.spin(FORWARD)

def rev():# drives backwards
 motor_8.set_velocity(20, PERCENT)
 motor_20.set_velocity(20, PERCENT)
 motor_8.spin(FORWARD)
 motor_20.spin(REVERSE)

def left(): # turns lefts slightly
 motor_8.set_velocity(20, PERCENT)
 motor_20.set_velocity(20, PERCENT)
 motor_8.spin(FORWARD)
 motor_20.spin(FORWARD)
 wait(0.35,SECONDS)
 motor_8.stop()
 motor_20.stop() 
def le (l):
 motor_8.set_velocity(100, PERCENT)
 motor_20.set_velocity(100, PERCENT)
 motor_8.spin(FORWARD)
 motor_20.spin(FORWARD)
 wait(l,SECONDS)
 motor_8.stop()
 motor_20.stop()
def right():# turns right slightly
 motor_8.set_velocity(20, PERCENT)
 motor_20.set_velocity(20, PERCENT)
 motor_8.spin(REVERSE)
 motor_20.spin(REVERSE)
 wait(0.35,SECONDS)
 motor_8.stop()
 motor_20.stop() 
def ri (r):
 motor_8.set_velocity(100, PERCENT)
 motor_20.set_velocity(100, PERCENT)
 motor_8.spin(REVERSE)
 motor_20.spin(REVERSE)
 wait(r,SECONDS)
 motor_8.stop()
 motor_20.stop() 
def stope():# stops completly 
 motor_8.stop()
 motor_20.stop()

def hold (): # holds the balls so they wont fall #is not working
 flip.set_velocity(15, PERCENT)
 flip.spin(FORWARD)
 wait(1,SECONDS)
 flip.stop()
 flip.spin_for(FORWARD, 1, DEGREES)

def back(p):# backwords slower
 motor_8.set_velocity(10, PERCENT)
 motor_20.set_velocity(10, PERCENT)


 motor_8.spin(FORWARD)
 motor_20.spin(REVERSE)
 wait(p,SECONDS)
 motor_8.stop()
 motor_20.stop()

def throw():# arm throws ball in bin
 flip.set_velocity(100, PERCENT)
 flip.spin(FORWARD)
 wait(2,SECONDS)
 flip.set_velocity(40, PERCENT)
 flip.spin(REVERSE)
 wait(2,SECONDS)
 flip.stop()
#starts
head=front.object_distance(MM)
side=rights.object_distance(MM)#names the sensor
back(2)
wait(2,SECONDS)
#  hold()
wait(3,SECONDS)
while head> 225:# sees how far it goes
    head=front.object_distance(MM)
    side=rights.object_distance(MM)
    brain.screen.print("VEXcode")
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("front", head)
    brain.screen.set_cursor(2,1)
    brain.screen.print("slid", side)
    if side< 555:# checks its position to make sure it goes stright
        brain.screen.set_cursor(5,1)
        brain.screen.print("left")
        left()
    elif side> 575:
         brain.screen.set_cursor(5,1)
         brain.screen.print("right")
         right()
    else:
        brain.screen.set_cursor(5,1)
        brain.screen.print("forward")
        forwards()
    wait(.1,SECONDS)

stope()
while True:#make sure the gears arent over spining
 if limit_switch_h.pressing():
  flip.stop()
  break
 else:
  flip.set_velocity(75, PERCENT)
  flip.spin(FORWARD)
while True:#make sure it dosent slam on its self
 if limit_switch_a.pressing():
  flip.stop()
  break
 else:
  flip.set_velocity(25, PERCENT)
  flip.spin(REVERSE)

back(33)# goes back to bin (hopefully)
le(1)
ri(2)
le(1)
forwards()
wait(0.5,SECONDS)
back(2)
head=front.object_distance(MM)#repeats program to more time
side=rights.object_distance(MM)
back(2)
wait(2,SECONDS)
#  hold()
wait(3,SECONDS)
while head> 225:
    head=front.object_distance(MM)
    side=rights.object_distance(MM)
    brain.screen.print("VEXcode")
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("front", head)
    brain.screen.set_cursor(2,1)
    brain.screen.print("slid", side)
    if side< 555:
        brain.screen.set_cursor(5,1)
        brain.screen.print("left")
        left()
    elif side> 575:
         brain.screen.set_cursor(5,1)
         brain.screen.print("right")
         right()
    else:
        brain.screen.set_cursor(5,1)
        brain.screen.print("forward")
        forwards()
    wait(.1,SECONDS)

stope()
while True:
 if limit_switch_h.pressing():
  flip.stop()
  break
 else:
  flip.set_velocity(75, PERCENT)
  flip.spin(FORWARD)
while True:
 if limit_switch_a.pressing():
  flip.stop()
  break
 else:
  flip.set_velocity(25, PERCENT)
  flip.spin(REVERSE)

