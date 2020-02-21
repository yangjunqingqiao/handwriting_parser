from __future__ import absolute_import, division, print_function, unicode_literals

import os
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow as tf
import cProfile

def parse_image(filename):
    parts = tf.strings.split(filename, '\\')
    label = parts[-2]

    image = tf.io.read_file(filename)
    image = tf.image.decode_jpeg(image)
    image = tf.image.convert_image_dtype(image, tf.float32)
    print(image.get_shape())
    image = tf.image.resize(image, [100, 1700])
    image = tf.reshape(image, [100, 1700])
    return image, label

def show(image, label):
    plt.figure()
    plt.imshow(image)
    plt.title(label.numpy().decode('utf-8'))
    plt.axis('off')
    plt.imshow(image)

if __name__ == '__main__':
    list_ds = tf.data.Dataset.list_files(str('data/images/*'))
    file_path = next(iter(list_ds))

    image, label = parse_image(file_path)
    show(image, label)
    plt.show()