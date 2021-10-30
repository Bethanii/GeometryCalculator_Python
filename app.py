from flask import Flask, request, render_template, redirect, url_for
import cylinder, cone, sphere#<--why?

#flask plumbing
app = Flask(__name__)

#flask route for the index page
#uses html template for user selection
@app.route("/", methods = ["GET", "POST"])
def mainForm():
   if request.method == "POST":
      sphere = request.form.get("sphere")
      cylinder = request.form.get("cylinder")
      cone = request.form.get("cone")
      print("Selection was: ", sphere, cylinder) #prints to command line for trouble shooting
      if sphere == "on":
         print("User selected sphere") #prints to command line for trouble shooting
         return redirect(url_for('sphereForm'))
      elif cylinder == "on":
         print("User selected cylinder") #prints to command line for trouble shooting
         return redirect(url_for('cylinderForm'))
      elif cone == "on":
         print("User selected cone") #prints to command line for trouble shooting
         return redirect(url_for('coneForm'))
   return render_template("index.html")

#flask route for the cylinder calculations page
@app.route("/cylinder", methods = ["GET", "POST"])
def cylinderForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # getting input with name = lname in HTML form 
       height = request.form.get("hgt") 
       vol = cylinder.volume(int(radius), int(height))
       return "User entered: Radius "+ str(radius) + " and Height: " + str(height) + ". <p>The Volume is: " + str(vol)
   return render_template("cylinder.html")

#flask route for the cone calulation page
@app.route("/cone", methods = ["GET", "POST"])
def coneForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # getting input with name = lname in HTML form 
       height = request.form.get("hgt") 

       #Setting variables to cone functions 
       vol = cone.volume(int(radius), int(height))
       slant = cone.slant(int(radius), int(height))
       surfaceArea = cone.surfaceArea(int(radius), int(height))
       latSurfaceArea = cone.latSurfaceArea(int(radius), int(height))

       #general output displaying user input
       output = "User entered: Radius "+ str(radius) + " and Height: " + str(height)
       #setting output to variables (for code structure)
       volResult = ". <p>The Volume is: " +str(vol)
       slantResult = ". <p>The Slant is: " + str(slant)
       surfAreaResult = ". <p>The Surface Area is: " + str(surfaceArea)
       latSurfAreaResult = ". <p>The Lateral Surface Area is: " + str(latSurfaceArea)

       #returning variables as output
       return output + volResult + slantResult + surfAreaResult + latSurfAreaResult
   return render_template("cone.html")

   #flask route for the sphere calculation page
@app.route("/sphere", methods = ["GET", "POST"])
def sphereForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")

       #Setting variables to cone functions 
       vol = sphere.volume(int(radius))
       surfaceArea = sphere.surfaceArea(int(radius))

       #general output displaying user input
       output = "User entered: Radius "+ str(radius) 
       #setting output to variables (for code structure)
       volResult = ". <p>The Volume is: " +str(vol)
       surfAreaResult = ". <p>The Surface Area is: " + str(surfaceArea)

       #returning variables as output
       return output + volResult +  surfAreaResult
   return render_template("sphere.html")

#more code here for the rest of the calculators: sphere, cube, etc.
  
if __name__=='__main__':   #more flask plumbing so the environment starts correctly
   app.run(host='0.0.0.0')