import openai

import os

import pandas as pd

import time


def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

    model=model,

    messages=messages,

    temperature=0,

    )

    return response.choices[0].message["content"]


if __name__ == '__main__':
    prompt = "write three words"

    response = get_completion(prompt)

    print(response)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


