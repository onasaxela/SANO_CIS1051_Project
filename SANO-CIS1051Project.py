#CIS1051 Project
#Mechanics of Solids Time Saver
import turtle
#What type of beam is it?
print("Input '1' for a cantilevered beam")
print("Input '2' for a simply supported beam")
units = int(input("What system of units are you using? 1 = SI 2 = Imperial "))
beam = int(input("What type of beam are you using? "))


#Beam Material
#input file reading with young's modulus numbers

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
        reactionY += appliedForces[1]
    print("The reaction force in the y-direction is", reactionY, "N")

    #Calculate moment reaction
    for j in range(len(appliedForces)):
        moment += (appliedForces[j]*distances[j])
    print("The moment reaction of the beam is", moment, "N*m")
    
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
    appliedForces =[]
    distances = []
    Ay = 0
    By = 0
    print("You selected a simply supported beam")
    length = float(input("How long is the beam (in meters)? ")
    while keepGoing == True:
        print("Enter downward forces one at at time")
        Force = int(input("What force is applied on the beam? ")
        appliedForces.append(Force)
        distance = int(input("How far away is this force from the left side?")
        distances.append(distance)
        more = input("Do you have more forces to input? Y/YES or N/NO ").lower()
        if more == "y" or more == "yes":
            continue
        else:
            break
    #calculations for reaction forces
    #find moment
    for i in range(len(forces)):
        By = (appliedForces[i]*distances[i])/length
