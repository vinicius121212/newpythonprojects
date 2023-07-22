from elevenlabs import set_api_key, generate, play
import openai
import json

openaikey = "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"
secretkey = openaikey

openai.api_key = secretkey

# File path to store messages
messages_file = "conversation_messages.json"

# Function to load previous messages from the file (if available)
def load_messages():
    try:
        with open(messages_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Load previous messages from the file or start with the initial messages
messages = load_messages()

# Function to continue the conversation and save messages
def continue_conversation(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=prompt
    )
    reply = response.choices[0].message['content'] # type: ignore

    # Append the user and assistant messages to the conversation
    prompt.append({"role": "assistant", "content": reply})

    # Save the updated messages to the file
    with open(messages_file, "w") as f:
        json.dump(prompt, f)

    return reply

# Main loop for back-and-forth conversation
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Exiting the conversation.")
        break

    # Append the user message to the conversation messages
    messages.append({"role": "user", "content": user_input})

    # Get the assistant's reply
    reply = continue_conversation(messages)
    print("VOLT:", reply)  # Print "VOLT:" before the assistant's reply
    audio = generate(
    text= str(reply),
    voice="Arnold",
    model='eleven_multilingual_v1'
    )
    
    play(audio) # type: ignore
    