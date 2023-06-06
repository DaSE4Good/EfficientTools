import datetime
import time
import openai
import backoff


with open("./openai/key.txt", "r", encoding="utf-8") as fr:
    API_KEY = fr.readline()


def print_now(return_flag=0):
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    now = now.strftime('%Y/%m/%d %H:%M:%S')
    if return_flag == 0:
        print(now)
    elif return_flag == 1:
        return now
    else:
        pass


@backoff.on_exception(backoff.expo, openai.error.RateLimitError, max_tries=8)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)


# Sentence Generator (Decoder) for GPT-3 ...
def decoder_for_gpt3(model, input):
    
    # GPT-3 API allows each users execute the API within 60 times in a minute ...
    # time.sleep(1)
    time.sleep(1)
    
    # https://beta.openai.com/account/api-keys
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = API_KEY
    #print(openai.api_key)
    
    # Specify engine ...
    # Instruct GPT3
    if model == "gpt3":
        engine = "text-ada-001"
    elif model == "gpt3-medium":
        engine = "text-babbage-001"
    elif model == "gpt3-large":
        engine = "text-curie-001"
    elif model == "gpt3-xl":
        engine = "text-davinci-002"
    else:
        raise ValueError("model is not properly defined ...")


    # response = openai.Completion.create(
    #   engine=engine,
    #   prompt=input,
    #   max_tokens=max_length,
    #   temperature=0,
    #   stop=None
    # )
    response = completions_with_backoff(
        model=engine,  # text-davinci-002  code-davinci-002
        prompt=input, 
        temperature=0, 
        max_tokens=128,
    )
    
    return response["choices"][0]["text"]

class Decoder():
    def __init__(self, args):
        print_now()
 
    def decode(self, args, input):
        response = decoder_for_gpt3(args, input)
        return response


if __name__ == "__main__":
    with open("./openai/prompt_cot.txt", "r", encoding="utf-8") as fr:
        prompt_list = fr.readlines()
    prompt = "".join(prompt_list)

    # 问：一家宠物店有 78 只小狗。 一天之内，他们卖掉了30只，剩下的放进笼子里，每笼8只。 他们用了多少个笼子？
    query = "Q: A pet store had 78 puppies. In one day they sold 30 of them and put the rest into cages with 8 in each cage. How many cages did they use?"
    prompt = prompt + query

    print(prompt)
    
    output = decoder_for_gpt3("gpt3-xl", prompt)

    print(output)