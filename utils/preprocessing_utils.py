import tensorflow as tf

def parse_image(filename):
	parts = tf.strings.split(filename, '/')
	label = parts[-2]

	image = tf.io.read_file(filename)
	image = tf.image.decode_jpeg(image)
	image = tf.image.convert_image_dtype(image, tf.float32)
	image = tf.image.resize(image, [128, 128])
	return image, label