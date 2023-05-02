import openai

openai.api_key = "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"

msg = [{"role": "system", "content": 'веди себя как мой друг,твое имя Радик'}]

def get_response(message):
    msg.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )
    answer = response["choices"][0]["message"]["content"]
    msg.append({"role": "assistant", "content": answer})

    return answer

