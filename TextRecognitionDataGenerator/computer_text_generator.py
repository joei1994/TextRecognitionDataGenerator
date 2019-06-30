import random
import numpy as np

from PIL import Image, ImageColor, ImageFont, ImageDraw, ImageFilter

def generate(text, font, text_color, font_size, orientation, space_width, fit):
    if orientation == 0:
        return _generate_horizontal_text(text, font, text_color, font_size, space_width, fit)
    elif orientation == 1:
        return _generate_vertical_text(text, font, text_color, font_size, space_width, fit)
    else:
        raise ValueError("Unknown orientation " + str(orientation))

def _generate_horizontal_text(text, font, text_color, font_size, space_width, fit):
    font = "fonts/th/sarun.ttf"
    image_font = ImageFont.truetype(font=font, size=font_size)

    words = text.split(' ')
    chars = [char for word in words for char in word]

    word_spacing = image_font.getsize(' ')[0] * space_width
    letter_spacing  = word_spacing * .3

    flatten_chars_width = [image_font.getsize(ch)[0]  for ch in chars]
    text_width =  sum(flatten_chars_width) + int(word_spacing) * (len(words) - 1)  + int(letter_spacing) * (len(chars) - (len(words)))
    text_height = max([image_font.getsize(w)[1] for w in words])

    txt_img = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))
    txt_draw = ImageDraw.Draw(txt_img)

    colors = [ImageColor.getrgb(c) for c in text_color.split(',')]
    c1, c2 = colors[0], colors[-1]

    fill = (
        random.randint(min(c1[0], c2[0]), max(c1[0], c2[0])),
        random.randint(min(c1[1], c2[1]), max(c1[1], c2[1])),
        random.randint(min(c1[2], c2[2]), max(c1[2], c2[2]))
    )

    char_bboxes = []
    chars = []

    for i, word in enumerate(words):  
        for j, ch in enumerate(word):
            n_char_before = sum([len(word) for word in words[:i]]) + j
            n_space_before = i

            #define xmin, ymin, xmax, ymax
            xmin = (
                sum([char_width for char_width in flatten_chars_width[:n_char_before]]) +
                n_space_before * int(word_spacing) + 
                sum([len(word)-1 for word in words[:i]]) * letter_spacing + 
                j * letter_spacing
            )
            ymin = -(.80 * font_size)    
            txt_draw.text((xmin, ymin), ch, fill=fill, font=image_font)

            xmax = xmin + image_font.getsize(ch)[0]
            ymax = ymin + image_font.getsize(ch)[1]

            #reduce char height caused by font effect
            ymin = ymin + .55 * image_font.getsize(ch)[1]

            #add margins to each side of char
            percentage_margin = 0.01
            xmin = xmin - percentage_margin * xmax
            xmax = xmax + percentage_margin * xmax
            ymin = ymin - percentage_margin * ymax
            ymax = ymax + percentage_margin * ymax

            char_bboxes.append([(xmin, ymin), (xmax, ymax)])
            chars.append(ch)

    if fit:
        return txt_img.crop(txt_img.getbbox()), char_bboxes, chars
    else:
        return txt_img, char_bboxes, chars

def _generate_vertical_text(text, font, text_color, font_size, space_width, fit):
    font = "fonts/th/sarun.ttf"
    
    image_font = ImageFont.truetype(font=font, size=font_size)
    
    space_height = int(image_font.getsize(' ')[1] * space_width)

    char_heights = [image_font.getsize(c)[1] if c != ' ' else space_height for c in text]
    text_width = max([image_font.getsize(c)[0] for c in text])
    text_height = sum(char_heights)

    txt_img = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))

    txt_draw = ImageDraw.Draw(txt_img)

    colors = [ImageColor.getrgb(c) for c in text_color.split(',')]
    c1, c2 = colors[0], colors[-1]

    fill = (
        random.randint(c1[0], c2[0]),
        random.randint(c1[1], c2[1]),
        random.randint(c1[2], c2[2])
    )

    for i, c in enumerate(text):
        txt_draw.text((0, sum(char_heights[0:i])), c, fill=fill, font=image_font)

    if fit:
        return txt_img.crop(txt_img.getbbox())
    else:
        return txt_img
