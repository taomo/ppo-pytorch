import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision.transforms as T
from torch.autograd import Variable

import numpy as np

class ActorCritic (nn.Module):
    def __init__(self, num_inputs, num_outputs, hidden=64):
        super(ActorCritic, self).__init__()
        