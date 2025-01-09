from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
olmo = AutoModelForCausalLM.from_pretrained("allenai/OLMo-1B-0724-hf", torch_dtype=torch.float16, load_in_8bit=True)
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMo-1B-0724-hf")

file_path = r"C:\Users\allan\nvim\python\whatToEatAtUCLA\menu\{}.txt"
diningHalls = ["BruinPlate", "DeNeve", "Epicuria"]
menus = []

for hall in diningHalls:
    with open(file_path.format(hall), "r") as f:
        menus.append(f.read())



message = [
    "You are a helpful chatbot that helps users choose what to eat based on their preferences.\n"
    """User: I'm hungry. What should I eat today. These are the options: Bruin Plate, DeNeve, and Epicuria.\n 
    """
    "Bot: These are the specials from each dining hall today. Bruin Plate has {}, DeNeve has {}, and Epicuria has {}\n",
    "User: I want to eat some Italian Food. Where should I eat? \n"
    ]


inputs = tokenizer(message, return_tensors='pt', return_token_type_ids=False).to('cuda')


response = olmo.generate(**inputs, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95)
print(tokenizer.batch_decode(response, skip_special_tokens=True)[0])



