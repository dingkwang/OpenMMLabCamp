from mmpretrain import ImageClassificationInferencer

infr = ImageClassificationInferencer(
    '/home/dkwang/learn_mmlab/OpenMMLabCamp/projects/hw_2_mmpretrain/resnet50_8xb32_fruit30_my.py',
    pretrained="/home/dkwang/learn_mmlab/OpenMMLabCamp/projects/hw_2_mmpretrain/best_accuracy_top1_epoch_55.pth")

img_path = "/home/dkwang/learn_mmlab/OpenMMLabCamp/projects/hw_2_mmpretrain/pineapple.jpg"
pred = infr(img_path, show_dir="outputs")
print(pred)