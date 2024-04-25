"""
import arrr
from pyscript import document


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)

"""
# imports
import time  # for measuring time duration of API calls
from openai import OpenAI
import os
from pyscript import document
await micropip.install("ssl")

def translate_english(event):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    input_text = document.querySelector("#english")
    english = input_text.value

    # record the time before the request is sent
    start_time = time.time()

    # send a ChatCompletion request to count to 100
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': english}
        ],
        temperature=0,
        stream=True  # again, we set stream=True
    )
    # create variables to collect the stream of chunks
    collected_chunks = []
    collected_messages = []

    output_div = document.querySelector("#output")

    # iterate through the stream of events
    for chunk in response:
        chunk_time = time.time() - start_time  # calculate the time delay of the chunk
        collected_chunks.append(chunk)  # save the event response
        chunk_message = chunk.choices[0].delta.content  # extract the message
        if(chunk_message != None):
            collected_messages.append(chunk_message)  # save the message
            
            #output_div.innerText += chunk_message
            #print(chunk_message, end="")

    collected_messages = [m for m in collected_messages if m is not None]
    full_reply_content = ''.join([m for m in collected_messages])

    output_div.innerText = full_reply_content

    #print(f"Full conversation received: {full_reply_content}")

    