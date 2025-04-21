import torch.nn as nn
import torch
from torchvision.models import resnet34, resnet50

class ResNet34(nn.Module):

    def __init__(self, pretrained=False):
        super(ResNet34, self).__init__()

        self.model = resnet34(pretrained=pretrained)
        # changing the last layer to match 8 classes
        self.model.fc = nn.Linear(512, 8)

    def forward(self, x):
        return self.model(x)


class ResNet50(nn.Module):

    def __init__(self, pretrained=False):
        super(ResNet50, self).__init__()

        self.model = resnet50(pretrained=pretrained)
        # changing the last layer to match 8 classes
        self.model.fc = nn.Linear(2048, 8)

    def forward(self, x):
        return self.model(x)
