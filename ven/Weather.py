import requests
api_key="1fd8008fb986bac5ff1a065b2add0ca0";
city="Gudalur"
url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric";
response=requests.get(url);
json=response.json();
print(json); 