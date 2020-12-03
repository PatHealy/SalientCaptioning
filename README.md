# SalientCaptioning
Salient Image Caption Generation with Initial Utterances of Localized Narratives. This was work completed for a class project, for CS 3730 at the University of Pittsburgh.

## Pre-Reqs
- Python 3.x
- Pandas
- nltk
- keras
- wget

## Contents
- /src contains the Python scripts that generate/train/use the model
- /models contains the two saved, trained models, which can be loaded into Keras and used to generate captions
- /evaluation contains data meant to evaluate the two models. It contains BLEU scores and example generated captions.
- Report.pdf is a written report on this project.

## How to Train the Models and Generate Captions
1. Download [the Flickr30K Image Set](https://www.kaggle.com/hsankesara/flickr-image-dataset) and place the folder in the /src/data folder.
2. Choose which of the two models (Full Text or First Sentence) you wish to user by setting the boolean flag on line 8 of "prepare_text.py" in the /src folder.
3. Download and prepare the annotation data by running "prepare_text.py" in the /src folder.
4. Extract features from the Flickr30K Image set by running "prepare_images.py" in the /src folder.
5. Set parameters for model training on lines 242-247 in "train.py" in the /src folder,
6. Train the model and evaluate it by running "train.py" in the /src folder.

## Citations
- Annotation data is taken from [Localized Narratives](https://google.github.io/localized-narratives/)
- Captioning Model based heavily on [a tutorial by Jason Brownlee](https://machinelearningmastery.com/develop-a-caption-generation-model-in-keras/)
