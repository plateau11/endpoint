from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def homePage():
    return 'Welcome to Medic 101'

@app.route('/listing')
def doctorListing():
    return 'Dr. NK Sharma,MD,Neurology'
    
@app.route('/detailPage')
def doctorDetails():
    return 'Dr. NK Sharma has done his MD in Neurology in AIIMS Delhi. '

#supplied query string, eg: /availability?day=Sunday
@app.route('/availability')
def doctorAvailability():
    day = request.args.get('day')
    if day:
     if day =='Sunday':
      return f'Doctor Unavailable on: {day}'
     else:
      return f'Doctor is Available on: {day}'
    else:
      return 'Day is required.'
    
@app.route('/appointment')
def doctorAppointment():
    return 'you have successfully registered an appointment'
    
@app.route('/booking')
def doctorBooking():
    return 'Booking completed'
