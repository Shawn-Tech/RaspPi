from flask import Flask, render_template
import datetime
import RPI.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

@app.route("/")
def hello():
  now = datetime.datetime.now()
  timeString = now.strftime("%Y - %m - %d %H:%M")
  templateData = {
   'title' : 'Return page from Raspberry Pi Server', 
   'time' : timeString
}
  
  return render_template('main.html', **templateData)



@app.route("/readPin/<pin>")
def readPin(pin):
	try:
		GPIO.setup(int(pin),GPIO.IN)
		if GPIO.setup(int(pin)) == True:
        		response = "Pin number " + pin + " is high !"
                else :
			response = "Pin number " + pin + " is low !"
		except :  
			response = "There was an error reading Pin " + pin + " . "

  templateData = {
   'title' : 'Status of hardware Pin  ' + pin, 
   'response' : response
}

return render_template('pin.html', **templateData)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)