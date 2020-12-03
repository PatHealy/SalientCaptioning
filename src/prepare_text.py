# Adapted from https://machinelearningmastery.com/develop-a-caption-generation-model-in-keras/
# Original Author: Jason Brownlee
# Heavily Modified by Pat Healy

import string
import localized_narratives

truncated = False	# Modify this line to change whether captions are limited to their first sentence

def clean_caption(cap):
	pIndex = cap.find('.')
	if pIndex == -1:
		pIndex = cap.find('and')
	if pIndex == -1:
		pIndex = len(cap)
	return cap[:pIndex]

# extract descriptions for images
def load_descriptions(doc):
	mapping = dict()
	# process lines
	for line in doc:
		if line.image_id not in mapping:
			if truncated:
				mapping[line.image_id] = clean_caption(line.caption)
			else:
				mapping[line.image_id] = line.caption
	return mapping
 
def clean_descriptions(descriptions):
	# prepare translation table for removing punctuation
	table = str.maketrans('', '', string.punctuation)
	for key, desc in descriptions.items():
		# tokenize
		desc = desc.split()
		# convert to lower case
		desc = [word.lower() for word in desc]
		# remove punctuation from each token
		desc = [w.translate(table) for w in desc]
		# remove hanging 's' and 'a'
		desc = [word for word in desc if len(word)>1]
		# store as string
		descriptions[key] =  ' '.join(desc)
 
# save descriptions to file, one per line
def save_doc(descriptions, filename):
	lines = list()
	for key, desc in descriptions.items():
		lines.append(key + ' ' + desc)
	data = '\n'.join(lines)
	file = open(filename, 'w+')
	file.write(data)
	file.close()

# Loacalized Narrative data loader replaces the Brownlee loader function
local_dir = './data'
data_loader = localized_narratives.DataLoader(local_dir)
data_loader.download_annotations('flickr30k_train')
data_loader.download_annotations('flickr30k_test')

print("Loading training annotations...")
descriptions = load_descriptions(data_loader.load_annotations('flickr30k_train', 100))
print('Loaded Training: %d ' % len(descriptions))
clean_descriptions(descriptions)
save_doc(descriptions, 'train.txt')
print('Training set saved to train.txt')
print()

print("Loading test annotations...")
test_descriptions = load_descriptions(data_loader.load_annotations('flickr30k_test', 100))
print('Loaded test set: %d ' % len(test_descriptions))
clean_descriptions(test_descriptions)
save_doc(test_descriptions, 'test.txt')
print('Validation set saved to test.txt')
