import requests
import urllib.request
from urllib.error import HTTPError
import json


last_request_time = float('-inf')

def predict(prompt, temperature=0, stop=None, max_tokens=1024, echo=False, min_query_interval=None):

	def filter_answer(ans):
		if ans.startswith('A:'):
			ans = ans[len('A:'):]
		return ans

	request_body = {'prompt': prompt, 'temperature': temperature, 'top_p': 0.9, 'top_k': 25, 'max_length': min(512, max_tokens), 'rep_pen': 1.0}
	if stop is not None:
		request_body['stop_sequence'] = [stop]
	api_url = 'http://localhost:5001/api/v1/generate'

	response = requests.post(api_url, json=request_body)
	response_text = response.json()['results'][0]['text']
	if stop is not None:
		response_text.removesuffix(stop)
	
	return response_text, None