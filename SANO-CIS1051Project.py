#CIS1051 Project
#Mechanics of Solids Time Saver
import turtle
import tkinter  # set size of window to size of map

wn = turtle.Screen()
wn.title("Beam Options")
wn.bgpic("CIS1051_pic.gif")
wn.update()
turtle.exitonclick()
#What type of beam is it?
print("Input '1' for a cantilevered beam")
print("Input '2' for a simply supported beam")
beam = int(input("What type of beam are you using? "))
units = int(input("What system of units are you using? 1 = SI 2 = Imperial "))

#only point loading 
#Beam Material

#Finding Reaction Forces
#cantilevered beam
if beam == 1 and units == 1:
    keepGoing = True
    appliedForces = []
    distances = []
    reactionY = 0
    moment = 0
    print("You selected Cantilevered Beam")
    while keepGoing == True:
        print("Enter forces one at a time")
        Force = int(input("What downward force is applied on the beam (in Newtons)? "))
        appliedForces.append(Force)
        print(appliedForces)
        distance = int(input("How far away is this force from the fixed point (in meters)? "))
        distances.append(distance)
        print(distances)
        more = input("Do you have more forces to input? Y/YES or N/NO ").lower()
        if more == "y" or more == "yes":
            continue
        else:
            break
    #Calculate reaction in the Y-Direction
    for i in range(len(appliedForces)):
        reactionY += appliedForces[i]
    print("The reaction force in the y-direction is", reactionY, "N")

    #Calculate moment reaction
    for j in range(len(appliedForces)):
        moment += (appliedForces[j]*distances[j])
    print("The moment reaction of the beam is", moment, "N*m")
    #attempt to find shear stress across the beam
    needMore = input("Do you need to find the shear force, moment, or both? S, M, or B ").lower()
    if needMore == "s":
        length = input("How long is the beam? ")
        distances.append(length)
        distances.insert(0,0)
        allForces = appliedForces
        allForces.insert(0,reactionY)
        V_list = []
        V = reactionY
        for k in range(len(appliedForces)):
            print("Shear force in section", k+1,",","[",distances[k],",",distances[k+1],")") #this works!!!!
            # Fy = Ay - f1 - f2 - f3 - V = 0
            # V = Ay - f1 - f2- f3
            # Fy = Ay - V = 0
            # V = Ay
            # Fy = Ay - f1 - V = 0
            # V = Ay - f1
            # add summation to get rid of applied forces
            # how do i create a new variable... append the new Vs to shear to list?
            V -= appliedForces[k]
            V_list.append(V)
            print(V)
        #print(V_list)

        #find moment equations
        #EM = M +Fd +fd =0
    if needMore == "m":
        length = input("How long is the beam? ")
        distances.append(length)
        distances.insert(0,0)
        allForces = appliedForces
        allForces.insert(0,reactionY)
        M_list = []
        M = moment
        for p in range(len(appliedForces)):
            print("Moment force in section", p+1,",","[",distances[p],",",distances[p+1],")")
            M -= appliedForces[p]*distances[p]
            M_list.append(M)
            print(M)

    if needMore == "b":
        length = input("How long is the beam? ")
        distances.append(length)
        distances.insert(0,0)
        allForces = appliedForces
        allForces.insert(0,reactionY)
        V_list = []
        V = reactionY
        M_list = []
        M = moment
        for k in range(len(appliedForces)):
            print("")
            print("Section", k+1,",","[",distances[k],",",distances[k+1],")") #this works!!!!
            V -= appliedForces[k]
            V_list.append(V)
            print("Shear Force", V, "N")
            M -= appliedForces[k]*distances[k]
            M_list.append(M)
            print("Moment force",M, "N*m")
            
        
            
    
if beam == 1 and units == 2:
    keepGoing = True
    appliedForces = []
    distances = []
    reactionY = 0
    moment = 0
    print("You selected Cantilevered Beam")
    while keepGoing == True:
        print("Enter forces one at a time")
        Force = int(input("What downward force is applied on the beam (in pounds)? "))
        appliedForces.append(Force)
        print(appliedForces)
        distance = int(input("How far away is this force from the fixed point (in feet)? "))
        distances.append(distance)
        print(distances)
        more = input("Do you have more forces to input? Y/YES or N/NO ").lower()
        if more == "y" or more == "yes":
            continue
        else:
            break
    #Calculate reaction in the Y-Direction
    for i in range(len(appliedForces)):
        reactionY += appliedForces[i]
    print("The reaction force in the y-direction is", reactionY, "lbs")

    #Calculate moment reaction
    for j in range(len(appliedForces)):
        moment += (appliedForces[j]*distances[j])
    print("The moment reaction of the beam is", moment, "lbs*ft")
    
#simply supported beam
if beam ==2 and units == 1:
    keepGoing = True
    appliedForces =[]
    distances = []
    Ay = 0
    By = 0
    TotalForce = 0
    print("You selected a simply supported beam")
    length = float(input("How long is the beam (in meters)? "))
    while keepGoing == True: #why is there invalid syntax here what the fuck
        print("Enter downward forces one at at time")
        Force = int(input("What force is applied on the beam? "))
        appliedForces.append(Force)
        distance = int(input("How far away is this force from the left side?"))
        distances.append(distance)
        more = input("Do you have more forces to input? Y/YES or N/NO ").lower()
        if more == "y" or more == "yes":
            continue
        else:
            break
    #calculations for reaction forces
    #find By through moment equation
    #M = 0 = -fd1 + -fd2+ by
    for i in range(len(appliedForces)):
        By += ((appliedForces[i]*distances[i])/length)
    print("The reaction force is By is", By, "N")
    #find Ay
    #total forces
    # F = -f -f -f +Ay +By
    for j in range(len(appliedForces)):
        TotalForce += appliedForces[j]
    Ay = TotalForce - By
    print("The reaction force at Ay is", Ay, "N")
    
if beam ==2 and units == 2:
    keepGoing = True
    appliedForces =[]
    distances = []
    Ay = 0
    By = 0
    TotalForce = 0
    print("You selected a simply supported beam")
    length = float(input("How long is the beam (in meters)? "))
    while keepGoing == True: #why is there invalid syntax here what the fuck
        print("Enter downward forces one at at time")
        Force = int(input("What force is applied on the beam? "))
        appliedForces.append(Force)
        distance = int(input("How far away is this force from the left side?"))
        distances.append(distance)
        more = input("Do you have more forces to input? Y/YES or N/NO ").lower()
        if more == "y" or more == "yes":
            continue
        else:
            break
    #calculations for reaction forces
    #find By through moment equation
    #M = 0 = -fd1 + -fd2+ by
    for i in range(len(appliedForces)):
        By += ((appliedForces[i]*distances[i])/length)
    print("The reaction force is By is", By, "lbs")
    #find Ay
    #total forces
    # F = -f -f -f +Ay +By
    for j in range(len(appliedForces)):
        TotalForce += appliedForces[j]
    Ay = TotalForce - By
    print("The reaction force at Ay is", Ay, "lbs")

    
    
