import os
import numpy as np
import cv2


def mykmeans(ncol, img_filename):
    images_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'images'))
    img_path = os.path.join(images_folder, img_filename)

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_shape = img.shape
    img = img.reshape((-1, 3))
    img = np.float32(img)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
    wcss, labels, centers = cv2.kmeans(img, ncol, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    basic_colors = [[255, 165, 0], [255, 255, 255], [255, 255, 0], [0, 255, 0], [0, 0, 0]]  # Orange, White, Yellow, Green, Black
    basic_colors = {i + 1: basic_colors[:i + 1] for i in range(5)}
    basic_colors = np.array(basic_colors[ncol], dtype=np.uint8)
    clustered_img = basic_colors[labels.flatten()]
    clustered_img = clustered_img.reshape(img_shape)

    output_filename = f'clustered_image_{ncol}.jpg'
    output_path = os.path.join(images_folder, output_filename)
    cv2.imwrite(output_path, cv2.cvtColor(clustered_img, cv2.COLOR_RGB2BGR))

    return output_filename
