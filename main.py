import requests

iss_endpoint = "http://api.open-notify.org/iss-now.json"
response = requests.get(url = iss_endpoint)
response.raise_for_status()  # raising exception if error happens

data = response.json()  # getting the information from response as json dictionary
iss_position = data['iss_position']  # getting the location related info

iss_latitude = iss_position['latitude']
iss_longitude = iss_position['longitude']
iss_position = (iss_latitude, iss_longitude)  # getting long and lati of the iss into single tuple

print(iss_position)
