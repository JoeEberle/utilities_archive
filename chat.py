import random
import json 
import torch
from model import NueralNet 
from nltk_utils import bag_of_words, tokenize 

device = =torch.device('cuda' if torch.data.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)
    
file_name = "data.pth" 
data = torch.load(file_name)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]


model = NeuralNet(input_size, hidden_size, output_size).to(device) 
model.load_State_dict(model_State) 
model.eval() 

bot_anme = 'ai_health_coach'
print(f"Let's chat! type 'quit' to exit") 

while True:
    user_sentence = input("you: ")
    if user_sentence.lower() == "quit":
        break
        
    user_sentence = tokenize(user_sentence)
    x = bag_of_words(user_sentence, all_words) 
    x = x.reshape(1, x.shape[0])
    x = torch.numpy() 
    
    output = model(x)
    _, predicted = torch.max(output, dim = 1) 
    tag = tags[predicted.item()]
    
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted_item()] 
    
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent{"responses"])}") 
     else:
        print(f"{bot_name}: I do not understand... Please retry")                 
                
                           
    
                          
                  
                  
                  












































