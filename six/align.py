alien_0={"color":"green","point":5}
print(alien_0["color"])
print(alien_0["point"])

new_points = alien_0["point"]
print("You just earned:"+ str(new_points))

alien_0["x_postion"] = 0
alien_0["y_postion"] = 25
print(alien_0)

alien_0["color"] = "red"
print(alien_0)

alien_0 = {"x_position":0,"y_position":25,"speed":"medium"}

print("Ori_position:"+str(alien_0["x_position"]))

if alien_0["speed"]  == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New_position:"+str(alien_0["x_position"]))


del alien_0["speed"]
print(alien_0)