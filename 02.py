from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-5f5cfd0c89284d36bce9b27e0f3a1645",
)

model = 'qwen-max'

messages = [
    {"role": "system", "content": "你是一个能力很强的AI"},
]

while True:
    user_input = input('User: ')
    if user_input.lower() == 'exit':  # 添加退出条件
        print("Assistant: 再见！")
        break

    messages.append(
        {"role": "user", "content": user_input}
    )
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )

        result = ''
        print("Assistant: ", end='')
        for chunk in stream:
            text = chunk.choices[0].delta.content
            if text is not None:
                result += text
                print(text, end='', flush=True)
        messages.append(
            {"role": "assistant", "content": result}
        )
    except Exception as e:
        print(f"\n发生错误: {e}")