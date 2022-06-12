import pyautogui as pg

while(True):
    a = pg.confirm('Are you mad??', buttons=["Yes", "No"])
    if(a == "Yes"):
        a2 = pg.alert('That\'s the correct answer 😂')
        break
        