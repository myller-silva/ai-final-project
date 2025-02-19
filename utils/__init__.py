import numpy as np
import torch
import matplotlib.pyplot as plt


def plot_decision_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
    grid = np.c_[xx.ravel(), yy.ravel()]
    grid_tensor = torch.tensor(grid, dtype=torch.float32)
    with torch.no_grad():
        Z = model(grid_tensor).numpy()
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8, cmap="bwr")
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors="k", cmap="bwr")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Fronteira de Decisão")
    plt.show()

def accuracy(y_true, y_pred):
    y_pred_class = (y_pred > 0.5).float()
    return (y_pred_class == y_true).float().mean()