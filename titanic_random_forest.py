# coding: cp932
import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier

#�P���f�[�^�̓ǂݍ���
train_df = pd.read_csv("train.csv", header=0)

# Sex���_�~�[�ϐ��ɕϊ�(female = 0, Male = 1)
train_df["Gender"] = train_df["Sex"].map( {"female": 0, "male": 1} ).astype(int)
train_df.head(3)

# �N��̌����l�́A�N��̕��ϒl�ŕ⊮����
median_age = train_df["Age"].dropna().median()
if len(train_df.Age[ train_df.Age.isnull() ]) > 0:
    train_df.loc[ (train_df.Age.isnull()), "Age"] = median_age

# �w�K�ɕK�v��������폜����
train_df = train_df.drop(["Name", "Ticket", "Sex", "SibSp", "Parch", "Fare", "Cabin", "Embarked","PassengerId"], axis=1) 
train_df.head(3)

#�e�X�g�f�[�^�̓ǂݍ���, Sex���_�~�[�ϐ��ɕϊ�
test_df = pd.read_csv("test.csv", header=0)
test_df["Gender"] = test_df["Sex"].map( {"female": 0, "male": 1} ).astype(int)

# �N��̌����l�́A�N��̕��ϒl�ŕ⊮����
median_age = test_df["Age"].dropna().median()
if len(test_df.Age[ test_df.Age.isnull() ]) > 0:
    test_df.loc[ (test_df.Age.isnull()), "Age"] = median_age

# �e�X�g�f�[�^��PassengerId���ޔ������A�e�X�g�f�[�^�̕s�v�ȗ���폜����
ids = test_df["PassengerId"].values
test_df = test_df.drop(["Name", "Ticket", "Sex", "SibSp", "Parch", "Fare", "Cabin", "Embarked","PassengerId"], axis=1) 
test_df.head(3)

#�����_���t�H���X�g�ŗ\��
train_data = train_df.values
test_data = test_df.values
model = RandomForestClassifier(n_estimators=100)
output = model.fit(train_data[0::,1::], train_data[0::,0]).predict(test_data).astype(int)

#���ʂ�"titanic_submit.csv"�Ƃ��ď����o��
submit_file = open("titanic_submit.csv", "w")
submit_file.write("PassengerId,Survived\n")
for i, o in zip(ids, output):
  submit_file.write(str(i) + ","+ str(o) + "\n")

submit_file.close()
