import requests

url = "https://real-time-amazon-data.p.rapidapi.com/search"

querystring = {"query":"football","page":"1","country":"IN","category_id":"aps"}

headers = {
	"X-RapidAPI-Key": "c650adbc45msh6d3675464b84e3ep19041ejsned1588b8e45b",
	"X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())