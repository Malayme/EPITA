import sys
from bitstring import BitArray
from PIL import Image

LSB_PAYLOAD_LENGTH_BITS = 32

def read_data(input_file):
    try:
        with open(input_file, "rb") as f:
            data = f.read()
    except IOError:
        print("Could not open file {}".format(input_file))
        sys.exit(1)
    return data

def write_data(output_file, data):
    try:
        with open(output_file, "wb") as f:
            f.write(data)
    except IOError:
        print("Could not open file {}".format(output_file))
        sys.exit(1)
    print("Data written to {}".format(output_file))

def obfuscate_via_lsb(data_file, input_file, output_file):
    data = read_data(data_file)
    data = BitArray(uint=len(data) * 8, length=LSB_PAYLOAD_LENGTH_BITS).bin + BitArray(bytes=data).bin
    i = 0
    try:
        with Image.open(input_file) as img:
            width, height = img.size
            if len(data) > width * height * 3:
                print("Data is too large for the image. Data contains {} bytes, max is {}".format(int(len(data) / 8), int(width * height * 3 / 8)))
                sys.exit(1)
            for x in range(width):
                for y in range(height):
                    pixel = list(img.getpixel((x, y)))
                    for n in range(3):
                        if i < len(data):
                            pixel[n] = (pixel[n] & ~1) | int(data[i])
                            i += 1
                    img.putpixel((x, y), tuple(pixel))
                    if i >= len(data):
                        break
                if i >= len(data):
                    break
            img.save(output_file, "png")
    except IOError:
        print("Could not open {}. Check that the file exists and it is a valid image file.".format(input_file))
        sys.exit(1)
    print("Data written to {}".format(output_file))

def deobfuscate_via_lsb(input_file, output_file):
    try:
        with Image.open(input_file) as img:
            payload_length = int("".join([str(x) for x in decode_img_nbits(img, LSB_PAYLOAD_LENGTH_BITS)]), 2)
            data = decode_img_nbits(img, payload_length + LSB_PAYLOAD_LENGTH_BITS)[LSB_PAYLOAD_LENGTH_BITS:]
            data = BitArray(bin="".join([str(x) for x in data])).bytes
    except IOError:
        print("Could not open {}. Check that the file exists and it is a valid image file.".format(input_file))
        sys.exit(1)
    write_data(output_file, data)

def decode_img_nbits(img, nbits):
    data = []
    i = 0
    width, height = img.size
    for x in range(width):
        for y in range(height):
            pixel = list(img.getpixel((x, y)))
            for n in range(3):
                if i < nbits:
                    data.append(pixel[n] & 1)
                    i += 1
            if i >= nbits:
                break
        if i >= nbits:
            break
    return data
