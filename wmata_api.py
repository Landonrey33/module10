import json
import requests
from flask import Flask

# API endpoint URL's and access keys
INCIDENTS_URL = "https://jhu-intropython-mod10.replit.app/"

################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
  # create an empty list called 'incidents'
  incidents = []
  
  # use 'requests' to do a GET request to the WMATA Incidents API
  # retrieve the JSON from the response
  response = requests.get(INCIDENTS_URL)
  all_incidents = response.json()

  # iterate through the JSON response and retrieve all incidents matching 'unit_type'
  # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
  #   -StationCode, StationName, UnitType, UnitName
  # add each incident dictionary object to the 'incidents' list
  for incident in all_incidents['ElevatorIncidents']:
    if incident['UnitType'] == str(unit_type).upper():
       new_dict = dict(StationCode = incident['StationCode'], StationName = incident['StationName'], UnitType = incident['UnitType'], UnitName = incident['UnitName'])
       incidents.append(new_dict)

  # return the list of incident dictionaries using json.dumps()
  return json.dumps(incidents)

if __name__ == '__main__':
    app.run(debug=True)
