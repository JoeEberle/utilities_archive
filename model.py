import torch
import torch.nn as nn 

Class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        self.l1 = nn.Linear(input_size, hidden_Size)
        self.l2 = nn.Linear(hidden_Size, hidden_Size)
        self.l3 = nn.Linear(hidden_Size, num_classes)  
        self.relu = nn.Relu()
        
    def forward(self, x ):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out 
    
    