import os
from ibm_watsonx_ai.foundation_models.inference import ModelInference
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

WATSONX_APIKEY = os.getenv('WATSONX_APIKEY')
WATSONX_URL = os.getenv('WATSONX_URL')
MODEL_ID = os.getenv('WATSONX_MODEL_ID', 'mixtral_8x7b_instruct_v01_q')

def _init_client():
    authenticator = IAMAuthenticator(WATSONX_APIKEY)
    client = ModelInference(authenticator=authenticator)
    client.set_service_url(WATSONX_URL)
    return client

client = _init_client()

SYSTEM_PROMPT = "You are a concise study assistant. Use only the provided context to answer. Cite page numbers when possible."

def generate_notes(retrieved_chunks, max_tokens=512):
    context = '\n\n---\n\n'.join([c['text'] for c in retrieved_chunks])
    prompt = f"{SYSTEM_PROMPT}\n\nContext:\n{context}\n\nInstructions: Produce concise bullet-point study notes."

    response = client.post_model({
        'model': MODEL_ID,
        'input': prompt,
        'temperature': 0.2,
        'max_tokens': max_tokens
    })
    return response.get_result()

def generate_qa(retrieved_chunks, max_tokens=1024):
    context = '\n\n---\n\n'.join([c['text'] for c in retrieved_chunks])
    prompt = f"{SYSTEM_PROMPT}\n\nContext:\n{context}\n\nInstructions: Generate 10 Q&A pairs."

    response = client.post_model({
        'model': MODEL_ID,
        'input': prompt,
        'temperature': 0.2,
        'max_tokens': max_tokens
    })
    return response.get_result()
