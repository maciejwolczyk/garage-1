# Use a pre-trained network to start a new experiment

In this section, we will provide a guide on how to use a pre-trained network to start a new experiment in garage. In practice, it is common for people to pretrain a network on a very large dataset and use the pre-trained network to perform the task of interest in reinforcement learning.

This tutorial will walk you through starting an experiment with a pre-trained network using two of the most common deep learning frameworks, Tensorflow and Pytorch.

## Set up the environment

First, we will start by setting up the environment for the experiment. We will train a `VPG algorithm` as an example.

We will simply setup the environment by initializing the garage environment `GarageEnv` and the `LocalRunner` instance.

```python
def vpg_pendulum(ctxt=None, seed=1):
    set_seed(seed)
    env = GarageEnv(env_name='InvertedDoublePendulum-v2')

    runner = LocalRunner(ctxt)

    ....
```

## Load the pre-trained model

After the setup, we can start to load a pre-trained model. It is assumed that a saved model is existed in the local path.

A common PyTorch convention is to save models using either a `.pt` or `.pth` file extension. Whereas Tensorflow convention is to save models inside a directory containing a protobuf binary `.pb` and a Tensorflow checkpoint `.ckpt`

Tensorflow and Pytorch provides a tutorial on how to save and load models [[pytorch]](https://pytorch.org/tutorials/beginner/saving_loading_models.html)[[Tensorflow]](https://www.tensorflow.org/tutorials/keras/save_and_load)

We will begin by loading a saved policy model.

```python
# Pytorch
import torch

PATH = './path_to/model' # model path

# specify the model
policy = GaussianMLPPolicy(env.spec,
                               hidden_sizes=[64, 64],
                               hidden_nonlinearity=torch.tanh,
                               output_nonlinearity=None)

# load the model
policy.load_state_dict(torch.load(PATH))

```

## Train

## Resources

### Pytorch pre-trained networks

https://pytorch.org/docs/stable/torchvision/models.html
