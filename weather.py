##This is a API script that reads the weather from openweathermap and return in real-time the value for any specific City Location in the World 
##With out going to their website you can get the info directly here with this script
import requests, json

##To access I use the given API key and the associated API URL
##Two important values that are importannt in the payload function ( q and appid)
api_key = "f6a8d0b90dd665984873ec34eceb557f"
base_url ="https://api.openweathermap.org/data/2.5/weather"
payload = {
	"q":"Mountain View",
	"appid": api_key
}

response = requests.get(base_url,params=payload)
##Here I convert into JSON
my_dict = json.loads(response.text)

print(my_dict["weather"][0]["description"])





