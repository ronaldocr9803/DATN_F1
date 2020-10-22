# select subsample of N for initial training
import os
import random
from shutil import copyfile, move
# import ipdb; ipdb.set_trace()
if not os.path.exists('a_data'):
	os.makedirs('a_data')
# determine number for the sample
NUM = 150
# create directory for the sample
base_dir = os.getcwd()
sub_dir = base_dir + '/validating_data/'
# labels = base_dir + '/data/training_data/labels/'
image_dir = base_dir + '/data/validating_data/'
image_paths = os.listdir(image_dir)
# import ipdb; ipdb.set_trace()
# randomly select subsample
num_val_sample = int(round(len(image_paths) * 0.3))
# import ipdb; ipdb.set_trace()
random_NUM = random.sample(image_paths, 300) 
# copy subsample into subsample directory
from tqdm import tqdm
for i in tqdm(random_NUM):
   move(image_dir + i, sub_dir + i )
# from tqdm import tqdm
# for i in tqdm(os.listdir(sub_dir)):
#    move(sub_dir + i, image_dir + i )