import argparse
import sys
import os
from PIL import Image



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Mandatory parametr')
    parser.add_argument('--width', type=int)
    parser.add_argument('--height', type=int)
    parser.add_argument('--scale', type=float)
    parser.add_argument('--output', help='The path where a file will be saved')
    return parser.parse_args()


def new_size(width, height, scale):
    if scale is not None:
        return int(img.width * scale), int(img.height * scale)
    if width is None:
        return (old_scale * height), height
    if height is None:
        value = old_scale()
        return width, int(width / value)
    elif width and height is not None:
        value = old_scale()
        if (width / height) != value:
            print('Scale is not same as initial value')
        return width, height
       
            
def old_scale():
    old_scale = (old_width)/(old_height)
    return int(old_scale)


def resize_img(img, width=None, height=None, scale=None):
    size = new_size(width, height, scale)
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
    if not os.path.exists(params.input):
        print('There is none image for modify')
        exit()
    if params.scale is not None and (params.width or params.height is not None):
        print('You should specify only scale or width and height')
        exit()
    img = Image.open(params.input)
    old_width, old_height = img.size
    updated_image = resize_img(img, width=params.width, height=params.height, scale=params.scale)
    path_to_result = output_for_updated_img(params.output, params.input, updated_image)
    updated_image.save(path_to_result)
    