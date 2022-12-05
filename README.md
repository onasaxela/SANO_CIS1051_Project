# SANO_CIS1051_Project
# What problems have I encountered?
# The first thing problem I was with the turtle window. I was not able to keep the turtle window open while code was operating. I had to close the window so that the code would conitnue. I would've been able to keep it up had I used a different library like pillow but I wanted to keep as true to python as much as possible so that others could easily use the code.

# The hardest part about this project was figuring out the equations to use. In the ideal project, I would've liked to make a code that would work for all scenarios. I thougth this was doable but as I was coding, I found that there were a lot of different scenarios that could happen and I would'be had to code an equation for each individual problem which is impossible. What makes it difficult is that there are equations that go up to the 4th power. Instead, I just used the simplest scenario which are point loads. With these types of problems, the equations only go up to the 1st power.

# With the equations being section based, I had to use a specific number. To do this, I appended the added point loads to a list and from there I just indexed which number I needed. Initially, I had a problem with the index going out of range. I solved this by creating a new list and appending the calculated reaction forces or a 0 (depending on the beam type). 

# another limitation to this code is that it does not give you the moment equation. It only gives you moment at a certain point. This is okay as it can help you solve problems. It jsut does not solve the problem for you.  

# my initialy thought process for this project was to have a list of equation (of which I would've had the code calculate), that way if a problem asked you about a moment inbetween the section end points, you were able to find it. 
