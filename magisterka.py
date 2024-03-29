# -*- coding: utf-8 -*-
"""magisterka.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iMKO4Ts6_1uzhS2DzmLRBY2YhqPaeHVN
"""

!curl -s https://course.fast.ai/setup/colab | bash

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)


from fastai import *
from fastai.vision import *

#path to root path
cd gdrive/'My Drive'/'Colab Notebooks' 
#batch size
bs = 7
#partition split 
pct = 0.3
#cycles number
cycles = 10
#loading spectograms
data = ImageDataBunch.from_folder('spectograms/', valid_pct=pct, bs=bs)
#normalizing spectograms
data.normalize(imagenet_stats)

#learner = cnn_learner(data, models.squeezenet1_0, metrics=accuracy)
#learner = cnn_learner(data, models.squeezenet1_1, metrics=accuracy)
#learner = cnn_learner(data, models.densenet121, metrics=accuracy)
#learner = cnn_learner(data, models.alexnet, metrics=accuracy)

#creating cnn_learner that depends on resnet101
learner = cnn_learner(data, models.resnet101, metrics=accuracy)

#starting learning
learner.fit_one_cycle(cycles)

#statistics about learning process
preds,y,losses = learner.get_preds(with_loss=True)
#interpretation of results
interpretation = ClassificationInterpretation(learner, preds, y, losses)

#top losses
interpretation.plot_top_losses(9, figsize=(10,10))

#confusion table
interpretation.plot_confusion_matrix(figsize=(10,10), dpi=80)

#losses diagram
learner.recorder.plot_losses()
#learning rate diagram
learner.recorder.plot_lr()