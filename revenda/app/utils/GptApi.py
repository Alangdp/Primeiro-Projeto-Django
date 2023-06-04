import httpx
import json

async def chat_gpt_async(message):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': 'Bearer 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',
        'Content-Type': 'application/json'
    }

    data = {
        'messages': [
            {'role': 'system', 'content': 'Você é um assistente de bate-papo. Para uma de carros que parcela carros em 120 vezes, se o cliente pedir informe sobre o carro as seguitne caresticas, rodas,banco, marca, modelo, ano, motor, velocidade maxima e demais informacoes'},
            {'role': 'user', 'content': message}
        ],
        'model': 'gpt-3.5-turbo'
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)

    response_json = response.json()
    if 'choices' in response_json:
        retornoApi = response_json['choices'][0]['message']['content']
        return retornoApi
    else:
        return None
