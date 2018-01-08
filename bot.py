import traceback
import time
import sqlite3
import praw
import bot
import mybrain
import fingers
import keyboard
import computer
import time
import eyes


sql = sqlite3.connect('sql.db')
brain = sqlite3.connect('mybrain.db')

def my_brain():
  print("I'm going to go to "rising" and look for a random post.")
  part1 = keyboard.enter("https://www.reddit.com/rising/")
  part2 = mybrain.selectRandomOption(part1)
  
  print("I'm currently using my brain to think of an idea. I'll post to " + part2)
  idea = mybrain.think()
  print(idea + " would be a great idea!")
  fingers.type(idea)
  print("Now I need to add a fake disclaimer to the bottom, telling everyone I'm a bot!")
  fingers.type("I'm a bot and this action was performed automatically. I learn by reading users comments.")
  print("Now it's time to post my bullshit!")
  fingers.useMouseToPress("save")
  print("Now it's time to get karma :)")
  time.sleep(3600)
  checkforkarma()
  

def checkforkarma():
  print("Did I get any internet points?")
  fingers.useMouseToPress("submissions")
  eyes.lookAt("points")
  internetpoints = eyes.remember("points")
  if internetpoints > 100:
    print("Holy shit it worked!")
    my_brain()
  else:
    print("Time to try again")
    my_brain()
    
  
  
  

        
