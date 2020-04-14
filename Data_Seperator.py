import os
import shutil


original_Train_dataset_dir = '/home/lordgrim/Desktop/WorkSpace/Projects/CNN/Cat_VS_Dog Classifier/Data/Train'
Train_dir = os.path.join(original_Train_dataset_dir, 'Train')
os.mkdir(Train_dir)
Validation_dir = os.path.join(original_Train_dataset_dir, 'Validation')
os.mkdir(Validation_dir)

Train_Cats_Dir = os.path.join(Train_dir, 'Cats') 
os.mkdir(Train_Cats_Dir)

Train_Dogs_dir = os.path.join(Train_dir, 'Dogs')
os.mkdir(Train_Dogs_dir)

Val_Cats_Dir = os.path.join(Validation_dir, 'Cats') 
os.mkdir(Val_Cats_Dir)

Val_Dogs_dir = os.path.join(Validation_dir, 'Dogs')
os.mkdir(Val_Dogs_dir)

Cnames = ['cat.{}.jpg'.format(i) for i in range(3125,12500)]
for cat in Cnames:
    src = os.path.join(original_Train_dataset_dir, cat)
    dst = os.path.join(Train_Cats_Dir, cat)
    shutil.move(src,dst)

Dnames = ['dog.{}.jpg'.format(i) for i in range(3125,12500)]
for dog in Dnames:
    src = os.path.join(original_Train_dataset_dir, dog)
    dst = os.path.join(Train_Dogs_dir, dog)
    shutil.move(src,dst)

CVnames = ['cat.{}.jpg'.format(i) for i in range(3125)]
for cat in CVnames:
    src = os.path.join(original_Train_dataset_dir, cat)
    dst = os.path.join(Val_Cats_Dir, cat)
    shutil.move(src,dst)

DVnames = ['dog.{}.jpg'.format(i) for i in range(3125)]
for dog in DVnames:
    src = os.path.join(original_Train_dataset_dir, dog)
    dst = os.path.join(Val_Dogs_dir, dog)
    shutil.move(src,dst)