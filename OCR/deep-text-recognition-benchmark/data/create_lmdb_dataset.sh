#!/usr/bin/env bash
python create_lmdb_dataset.py --inputPath ./generator/TextRecognitionDataGenerator --gtFile generator/TextRecognitionDataGenerator/gt_basic.txt --outputPath ./data_lmdb_release/training/basic/;

python create_lmdb_dataset.py --inputPath ./generator/TextRecognitionDataGenerator --gtFile generator/TextRecognitionDataGenerator/gt_skew.txt --outputPath ./data_lmdb_release/training/skew/;

python create_lmdb_dataset.py --inputPath ./generator/TextRecognitionDataGenerator --gtFile generator/TextRecognitionDataGenerator/gt_dist.txt --outputPath ./data_lmdb_release/training/dist/;

python create_lmdb_dataset.py --inputPath ./generator/TextRecognitionDataGenerator --gtFile generator/TextRecognitionDataGenerator/gt_blur.txt --outputPath ./data_lmdb_release/training/blur/;

python create_lmdb_dataset.py --inputPath ./generator/TextRecognitionDataGenerator --gtFile generator/TextRecognitionDataGenerator/gt_back.txt --outputPath ./data_lmdb_release/training/back/;

python create_lmdb_dataset.py --inputPath ./generator/TextRecognitionDataGenerator --gtFile generator/TextRecognitionDataGenerator/gt_basic_validate.txt --outputPath ./data_lmdb_release/validation/basic/;

python create_lmdb_dataset.py --inputPath ./generator/TextRecognitionDataGenerator --gtFile generator/TextRecognitionDataGenerator/gt_skew_validate.txt --outputPath ./data_lmdb_release/validation/skew/;

python create_lmdb_dataset.py --inputPath ./generator/TextRecognitionDataGenerator --gtFile generator/TextRecognitionDataGenerator/gt_dist_validate.txt --outputPath ./data_lmdb_release/validation/dist/;

python create_lmdb_dataset.py --inputPath ./generator/TextRecognitionDataGenerator --gtFile generator/TextRecognitionDataGenerator/gt_blur_validate.txt --outputPath ./data_lmdb_release/validation/blur/;

python create_lmdb_dataset.py --inputPath ./generator/TextRecognitionDataGenerator --gtFile generator/TextRecognitionDataGenerator/gt_back_validate.txt --outputPath ./data_lmdb_release/validation/back/;


# python create_lmdb_dataset.py --inputPath data/generator/TextRecognitionDataGenerator --gtFile data/generator/TextRecognitionDataGenerator/gt_skew.txt --outputPath data/data_lmdb_release/training/skew/;

# python create_lmdb_dataset.py --inputPath data/generator/TextRecognitionDataGenerator --gtFile data/generator/TextRecognitionDataGenerator/gt_dist.txt --outputPath ocr_kor/data/data_lmdb_release/validation/dist/;

# python create_lmdb_dataset.py --inputPath data/generator/TextRecognitionDataGenerator --gtFile data/generator/TextRecognitionDataGenerator/gt_blur.txt --outputPath ocr_kor/data/data_lmdb_release/validation/blur/;

# python create_lmdb_dataset.py --inputPath data/generator/TextRecognitionDataGenerator --gtFile data/generator/TextRecognitionDataGenerator/gt_back.txt --outputPath ocr_kor/data/data_lmdb_release/validation/back/;

# CUDA_VISIBLE_DEVICES=0 python train.py --train_data data/data_lmdb_release/training --valid_data data/data_lmdb_release/validation --select_data basic-skew --batch_ratio 0.5-0.5 --Transformation TPS --FeatureExtraction VGG --SequenceModeling None --Prediction Attn --data_filtering_off --batch_max_length 50 --workers 4