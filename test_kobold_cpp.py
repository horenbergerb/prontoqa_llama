import requests
import json


if __name__ == '__main__':
	prompt = 'Hey, this is just a test. I\'m just'
	temperature = 0.5
	api_url = 'http://localhost:5001/api/v1/generate'
	request_body = {'prompt': prompt, 'temperature': temperature, 'top_p': 0.9, 'top_k': 25}
	response = requests.post(api_url, json=request_body)
	print(response)
	print(type(response))
	print(response.json())
