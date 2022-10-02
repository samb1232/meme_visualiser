import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mpe


def __make_images(text: str, fps: int, frameSize: tuple, bgImage: str):
    text_apart = text.split(" ")
    text_size = 70
    font = ImageFont.truetype('Caveat-VariableFont_wght.ttf', size=text_size)

    images = []

    cur_images = []

    for word_index in range(len(text_apart)):
        word = text_apart[word_index]

        image = Image.open(bgImage)
        draw_im = ImageDraw.Draw(image)
        draw_im.text(
            (image.height / 2 - len(word) / 2 * text_size / 3 - 5, image.width / 2 - text_size),
            word,
            fill='#FFFFFF',
            font=font
        )

        scale = 0.01

        while scale <= 1:
            if word_index == 0: break  # Первый кадр появляется сразу с scale = 1

            img_half = cv2.resize(np.asarray(image), (0, 0), fx=scale, fy=scale)

            new_image = Image.new('RGB', frameSize, color="#000000")
            new_image.paste(Image.fromarray(np.asarray(img_half)), (
                round(new_image.width / 2 - len(img_half) / 2), round(new_image.height / 2 - len(img_half) / 2)))

            cur_images.append(np.asarray(new_image))
            scale += 0.05

        scale = 1

        if word_index == 0: cur_images.append(np.asarray(image))
        cur_images = __easyease(cur_images, fps)
        images += cur_images
        cur_images = []

        while scale >= 0.01:
            if word_index == len(text_apart) - 1: break
            img_half = cv2.resize(np.asarray(image), (0, 0), fx=scale, fy=scale)

            new_image = Image.new('RGB', frameSize, color="#000000")
            new_image.paste(Image.fromarray(np.asarray(img_half)), (
                round(new_image.width / 2 - len(img_half) / 2), round(new_image.height / 2 - len(img_half) / 2)))

            cur_images.append(np.asarray(new_image))

            scale -= 0.05

    return images


def __easyease(arr, fps):
    fps = int(fps / 2)
    new_arr = []
    coef = 10
    for i in range(fps - len(arr) - coef):
        new_arr.append(arr[0])

    new_arr += arr

    for i in range(coef):
        new_arr.append(arr[-1])

    return new_arr


def __make_movie(text, bgImage):
    fps = 120
    frameSize = (511, 511)

    images_arr = __make_images(text, fps, frameSize, bgImage)

    out = cv2.VideoWriter('tempvid.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, frameSize)

    for im in images_arr:
        out.write(im)

    for i in range(fps):
        out.write(images_arr[-1])

    out.release()

    # Вставляем аудио
    my_clip = mpe.VideoFileClip('tempvid.avi')

    audio_background = mpe.AudioFileClip('SugarCrush2.mp3')
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile('result.mp4')


def make_clip(text: str, bgImage="starBG.jpg"):
    if len(text) == 0 and (bgImage != "starBG.jpg") and (bgImage != "sceletonBG.jpg") and (bgImage != "fireBG.jpg"):
        raise ValueError("Wrong input: str should not be empty and bg image should be: sceletonBG.jpg or fireBG.jpg "
                         "or starBG.jpg")
    __make_movie(text, bgImage)


