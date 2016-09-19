---
layout: post
title: Play with Neural Nets
---

Neural Nets are simple to implement but difficult to understand and explain. It's hard to figure out how and why they work the way they do. the TensorFlow playground is a great place to develop some intuition. Play is always a great way to learn, and Learning about Machine Learning is no different. Teasing is a great way to probe the learning of another neural net, even if it's artificial.

First, like any good play or experiment try the same thing at least three times before giving up. Regenerate a new random dataset with your parameters and rerun the training. That's the only way to be sure the "intuition" you're building (the impression on your squishy neural net) is real. Everyone can get lucky or unlucky once, but 3 times is pretty rare. But don't change your train/test set before comparing all the other hyperparameters. So the process is:

1. Generate a dataset by choosing a dataset type, your training/testset ratio, noise.
2. Make it a gamet to try to find the best mix of the other parameters

- dataset_type
- dataset_training_ratio: the portion of the dataset to use during training (the rest is the test set)
- dataset_noise

Touching any of the parameters in step 1 in the Playground interface will regenerate the dataset, so don't do that until your really sure you understand how the other parameters were able to deal with that particular data set.

## Baseline Success (Fast and Reasonably Accurate)

### Parameters that regenerate a data set

- dataset_type: spiral
- dataset_training_ratio: .5 - 0.9
- dataset_noise: 50

### Parameters that just randomize the initial state

batch_size: 30
features: [x1, x2, x1**2, x2**2]
layers: [5]
learning_rate: 0.1
activation: sigmoid
regularization: L2
regularization_rate: 0.01
problem_type: classification



steadily falls to 0.08 - 0.19 testset loss loss after 2k epochs
odd contours in white space that partially match intuition
