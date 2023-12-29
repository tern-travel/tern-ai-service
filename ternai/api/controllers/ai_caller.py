from openai import OpenAI
import json
from api.models import ExternalCall, APICall


def make_ai_call(prompt:str, endpoint_used:ExternalCall):
  
  client = OpenAI()

  response = client.chat.completions.create(
    model=endpoint_used.endpoint.prompt.model.api_value, #We get the endpoint to use from the API
    response_format={ "type": "json_object" }, #NOTE THE JSON OBJECT TYPE
    messages=[
      {"role": "system", "content": endpoint_used.endpoint.prompt.instructions},
      {"role": "user", "content": prompt}
    ]
  )

  response_dict = json.loads(response.choices[0].message.content)
  log_api_call(endpoint_used.endpoint.prompt.instructions,response_dict)
  return response_dict


def log_api_call(prompt:str, results:dict):
  
  response_json = json.dumps(results)

  new_api_call = APICall(
    prompt_text=prompt,
    in_progress=False,
    complete=True,
    response=response_json
  )
  
  new_api_call.save()
