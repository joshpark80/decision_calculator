import forecastio

def get_weather(api_key, lat, lng):
	forecast = forecastio.load_forecast(api_key, lat, lng).currently()
	return print ("It is currently %  degrees." % (forecast.temperature) )

api_key="f824c9b9adb4c0d098859fc7a2b09ff6"
lat=input ("what is your latitude?")
lng=input ("what is your longitude?")

#forecast = forecastio.load_forecast(api_key, lat, lng).currently()
#print(forecast.summary, forecast.temperature, forecast.precipProbability)

print(get_weather(api_key, lat, lng))
