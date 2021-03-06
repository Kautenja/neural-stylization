"""An implementation of a basic gradient descent algorithm."""
from typing import Callable
from tqdm import tqdm
import numpy as np


class GradientDescent(object):
    """A basic gradient descent optimizer."""

    def __init__(self, learning_rate: float=1e-4) -> None:
        """
        Initialize a new Stochastic Gradient Descent optimizer.

        Args:
            learning_rate: how fast to adjust the parameters (dW)

        Returns:
            None

        """
        self.learning_rate = learning_rate
        # set the history of loss evaluations to empty list
        self.loss_history = []

    def __repr__(self) -> str:
        """Return an executable string representation of this object."""
        return '{}(learning_rate={})'.format(*[
            self.__class__.__name__,
            self.learning_rate
        ])

    def __call__(self,
                 X: np.ndarray,
                 shape: tuple,
                 loss_grads: Callable,
                 iterations: int=1000,
                 callback: Callable=None):
        """
        Reduce the loss generated by X by moving it based on its gradient.

        Args:
            X: the input value to adjust to minimize loss
            shape: the shape to coerce X to
            loss_grads: a callable method that returns loss and gradients
                        given some input
            iterations: the number of iterations of optimization to perform
            callback: an optional callback method to receive image updates

        Returns:
            an optimized X about the loss and gradients given

        """
        # reset the history of loss evaluations to empty list
        self.loss_history = []
        for i in tqdm(range(iterations)):
            # pass the input through the loss function and generate gradients
            loss_i, grads_i = loss_grads([X])
            # move the input based on the gradients and learning rate
            X -= self.learning_rate * grads_i
            # update the loss history with this loss value
            self.loss_history.append(loss_i)
            # pass the values to the callback if any
            if callable(callback):
                callback(X, i)

        return X


# explicitly define the outward facing API of this module
__all__ = [GradientDescent.__name__]
