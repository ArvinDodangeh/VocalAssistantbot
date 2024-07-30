from openai import OpenAI
from config.config import setting

# Authorization of Openapi  :

client = OpenAI(api_key=setting.openai_key)
