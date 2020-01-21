# coding=utf-8
# created by msg on 2019/12/4 2:53 下午

import tensorflow as tf
import tensorflow_datasets as tfds

for data in tfds.list_builders():
    print(data)
    try:
        t = tfds.load(data)
    except Exception:
        continue
path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')