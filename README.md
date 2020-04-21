# <div align='center'><i>Debugging CNNs</i></div>

<div align='center'>It’s often said that deep-learning models are “black boxes”: learning representations that are difficult to extract and present in a human-readable form. Although this is partially true for certain types of deep-learning models, it’s definitely not true for convnet's. Here I shall briefly explain some of the techniques for visualizing what the convnet's has learned. In application programming, we have debugging and error checking statements like print, assert, try-catch, etc. But when it comes to deep neural networks, debugging them becomes a bit tricky. Fortunately, CNN's takes inputs (images) which are visually interpretable by humans so by visualizing what the convnet's has learned we can debug them effectively.</div>


<p></p>
<div align='left'>This repository has two notebooks:<div>

- <a href="https://github.com/GauthamSks/Visualizing-CNNs/blob/master/Cats_Vs_Dogs%20Classifier.ipynb">Cats Vs Dogs classifier</a>
- <a href="https://github.com/GauthamSks/Visualizing-CNNs/blob/master/Visualizing%20CNN's.ipynb">Visualizing CNN</a>

## Cats Vs Dogs classifier
<p align='center'><img src=./Images/CvsD_s.jpg></p>
Here I shall demonstrate how to build a simple CNN model in Keras from scratch for classifying cats and dogs while maintaining high accuracy. The dataset used for this classification task is provided by  <a href="https://www.kaggle.com/c/dogs-vs-cats/data">Kaggle</a>. The model has an accuracy of about 93% . I have also written a simple data separator python program that will organize the files in the required format for training the model.

## Visualizing CNN

<div align='center'>Here I shall demonstrate few of the visualizing techniques to reveal what the CatsVsDogs model(image shown below) has learned and provide insights into it. The techniques that I shall be using here are:</div>
<p align='center'><img src=./Images/Model.png></p>

- ### <b>Visualizing Intermediate Activations</b>
Here we shall display the feature maps that are output by various convolution and pooling layers in a network, given a certain input. This gives a view into how input is decomposed by the different filters learned by the network. For eg say the input layer dimension is 224x224x3 and the output dimension after the first convolution operation is 224x224x64. Here, 64 is the number of filters which are used to extract input features after 1st convolution operation, so we will just plot these sixty-four 224x224 filtered outputs of the input image. A sample image from the notebook is given below.
<p align='center'><img src=./Images/VIAF1.png></p>

- ### <b>Visualizing Convnet Filters</b>
The visualization we saw above was the output of the convolution operation. A convolution operation in its most basic terms is the correlation between the filters/kernels and the input image.The filter which matches the most with the given input region will produce an output which will be higher in magnitude (compared to the output from other filters). By visualizing filters we get an idea of what pattern each layer has learned to extract from the input. This can be done with gradient ascent in input space : applying gradient descent to the value of the input image of a convnet so as to maximize the response of a specific filter, starting from a blank input image. The resulting input image will be one that the chosen filter is maximally responsive to. For this a loss function that maximizes the value of a
given filter in a given convolution layer, and then we shall use stochastic gradient descent to adjust the values of the input image so as to maximize this activation value. A sample image from the notebook is given below.
<p align='center'><img src=./Images/VCF.png></p>


- ### <b>Visualizing Heatmaps</b>
 <div align='left'>In this technique, we use GradCAM and try to understand which parts of the input image led a convnet to a particular classification decision. The general category of techniques is called “Class Activation Map” (CAM) visualization and consists in producing heatmaps of “class activation” over input images. A “class activation” heatmap is a 2D grid of scores associated with a specific output class, computed for every location in an input image, indicating how important each location is with respect to the class considered. This helps us in debugging the decision process of a convolutional neural network.A sample image from the notebook is given below.</div>
<p align='center'><img src=./Images/VH.png></p>

## References
- <a href="https://www.amazon.in/Deep-Learning-Python-Francois-Chollet/dp/1617294438">Deep Learning with Python by François Chollet</a>
- <a href="https://towardsdatascience.com/visual-interpretability-for-convolutional-neural-networks-2453856210ce">Visual Interpretability for Convolutional Neural Networks by Himanshu Rawlani</a>

