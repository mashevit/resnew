from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
#OpenAI.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


def get_ans(prompt):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        #{"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        #{"role": "user", "content": prompt}
       # {"role": "user", "content": "write 3 words"}
        {"role": "user", "content": prompt}
      ],
      temperature=0,
     # max_tokens=50
    )
    print(f'prompt = {prompt}')
    str_tmp = completion.choices[0].message.content
    print(f"tmp = {str_tmp}")
    return str_tmp





def get_ans_4(prompt):
    completion = client.chat.completions.create(
      model="gpt-4",
      messages=[
        #{"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        #{"role": "user", "content": prompt}
       # {"role": "user", "content": "write 3 words"}
        {"role": "user", "content": prompt}
      ],
      temperature=0,
     # max_tokens=50
    )

    str_tmp = completion.choices[0].message.content
    print(f"tmpGPT4 = {str_tmp}")
    return str_tmp



"""
I have dataset with the following features:
   1. animal name:      Unique for each instance
   2. hair		Boolean
   3. feathers		Boolean
   4. eggs		Boolean
   5. milk		Boolean
   6. airborne		Boolean
   7. aquatic		Boolean
   8. predator		Boolean
   9. toothed		Boolean
  10. backbone		Boolean
  11. breathes		Boolean
  12. venomous		Boolean
  13. fins		Boolean
  14. legs		Numeric (set of values: {0,2,4,5,6,8})
  15. tail		Boolean
  16. domestic		Boolean
  17. catsize		Boolean
  18. type		Numeric (integer values in range [1,7])
suggest me one additional feature from external knowledge that can improve machine learning classification. output only feature name for further processing
  """
#ChatCompletionMessage(content='Habitat (Categorical variable indicating the natural environment or type of habitat where the animal resides)', role='assistant', function_call=None, tool_calls=None)





#print(completion.choices[0].message)