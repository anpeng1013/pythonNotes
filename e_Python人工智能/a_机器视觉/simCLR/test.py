# -*- coding = utf-8 -*-
# @Time : 2022/12/6 21:38
# @Author : anpeng
# @File : test.py
# @Software : PyCharm

import torch
from torch.utils.data import DataLoader
import torchvision
import torch.nn as nn
import torch.optim

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden_layer = nn.Linear(784, 30)
        self.activation_function = nn.Tanh()
        self.output_layer = nn.Linear(30, 10)

    def forward(self, x):
        out = self.hidden_layer(x)
        out = self.activation_function(out)
        out = self.output_layer(out)
        out = self.activation_function(out)
        return out

def target_transform(labels):
    batch_size = labels.shape[0]
    result = torch.zeros((batch_size, 10), dtype=torch.float32)
    for index, row in enumerate(result):
        row[labels[index]] = 1
    return result

if __name__ == '__main__':
    mnist_train = torchvision.datasets.MNIST(root='./dataset', train=True, download=True,
                                             transform=torchvision.transforms.ToTensor(),
                                             target_transform=torchvision.transforms.Lambda(
                                                 lambda label: torch.tensor(label)
                                             )
                                             )
    mnist_test = torchvision.datasets.MNIST(root='./dataset', train=False, download=True,
                                            transform=torchvision.transforms.ToTensor())
    batch_size = 10
    mnist_train_loader = torch.utils.data.DataLoader(mnist_train, batch_size=batch_size, shuffle=True)
    mnist_test_loader = torch.utils.data.DataLoader(mnist_test, batch_size=batch_size)

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    epochs = 30
    learning_rate = 0.1
    net = Net().to(device=device)
    optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)
    # loss_fn = nn.MSELoss()
    loss_fn = nn.CrossEntropyLoss()
    loss = 0.0
    for epoch in range(epochs):
        for images, labels in mnist_train_loader:
            images = images.to(device=device)
            labels = labels.to(device=device)
            output = net(images.view(images.shape[0], -1))
            # ---- MSELoss ----
            # labels = target_transform(labels).to(device=device)
            # ---- MSELoss ----
            loss = loss_fn(output, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        correct = 0
        total = 0
        with torch.no_grad():
            for images, labels in mnist_test_loader:
                images = images.to(device=device)
                labels = labels.to(device=device)
                output = net(images.view(images.shape[0], -1))
                predicted = torch.argmax(output, dim=1)
                total += labels.shape[0]
                correct += int((predicted == labels).sum())
        print('Epoch %d: %d / %d %f' % (epoch + 1, correct, total, loss))
