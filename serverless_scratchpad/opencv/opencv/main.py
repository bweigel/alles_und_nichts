import cv2
import numpy as np
import pkg_resources


def load_imng():
    file = pkg_resources.resource_filename(__name__, 'messi.png')
    img = cv2.imread(file, 0)
    return f"image size={img.size}\nimage shape={img.shape}"


def lambda_handler(event, context):
    return {'statusCode': 200,
            'body': load_imng()}
