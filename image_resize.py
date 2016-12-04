import argparse
import sys
import os
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_path', help='Mandatory parametr')
    parser.add_argument('--width', type=int)
    parser.add_argument('--height', type=int)
    parser.add_argument('--scale', type=float)
    parser.add_argument('--output', help='The path where a file will be saved')
    return parser.parse_args()


def get_new_size(width, height, scale):
    initial_scale = get_old_scale()
    if scale is not None:
        return int(img.width * scale), int(img.height * scale)
    if width is None:
        return (initial_scale * height), height
    if height is None:
        return width, int(width / initial_scale)
    elif width and height is not None:
        if (width / height) != initial_scale:
            print('Scale is not same as initial value')
        return width, height
       
            
def get_old_scale():
    old_scale = (old_width)/(old_height)
    return int(old_scale)


def resize_img(img, width=None, height=None, scale=None):
    size = get_new_size(width, height, scale)
    return img.resize(size)


def output_for_updated_img(output_path, path_to_image, img):
    if output_path is not None:
        return output_path
    else:
        filename, file_ext = os.path.splitext(os.path.basename(path_to_image))
        return '{}__{}x{}{}'.format(filename,
                                    img.width,
                                    img.height,
                                    file_ext)


if __name__ == '__main__':
    params = get_args()
    if not os.path.exists(params.source_path):
        print('There is none image for modify')
        exit()
    if params.scale is not None and (params.width or params.height is not None):
        print('You should specify only scale or width and height')
        exit()
    img = Image.open(params.source_path)
    old_width, old_height = img.size
    updated_image = resize_img(img, width=params.width, height=params.height, scale=params.scale)
    path_to_result = output_for_updated_img(params.output, params.source_path, updated_image)
    updated_image.save(path_to_result)
    