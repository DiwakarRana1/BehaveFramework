import openai

# Set your OpenAI API Key
openai.api_key = ""


def get_credentials_from_ai(prompt):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can use other models too
        messages=[{"role": "user", "content": prompt}]
    )

    content = response['choices'][0]['message']['content'].strip()
    print("AI Response:\n", content)

    # Simple extraction logic
    credentials = {}
    for line in content.split('\n'):
        if 'username' in line.lower():
            credentials['username'] = line.split(":")[1].strip()
        elif 'password' in line.lower():
            credentials['password'] = line.split(":")[1].strip()

    return credentials


# 👉 Scenario 1: Generate fake username and fake password
prompt_1 = "Generate a fake username and fake password. Reply in the format:\nUsername: <value>\nPassword: <value>"
creds1 = get_credentials_from_ai(prompt_1)
print("\n[Scenario 1] Fake Username & Password:", creds1)

# 👉 Scenario 2: Valid username and fake password
prompt_2 = "Generate a valid username (test_user) and a fake password. Reply in the format:\nUsername: test_user\nPassword: <value>"
creds2 = get_credentials_from_ai(prompt_2)
print("\n[Scenario 2] Valid Username & Fake Password:", creds2)