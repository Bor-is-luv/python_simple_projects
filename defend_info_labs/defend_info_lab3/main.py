def open_pic(pic_name):
    pixels = []
    buffer = []
    k = 0
    with open(pic_name, 'rb') as file:
        data = bytearray(file.read())
        BM = data[0:2]
        len1 = data[2:6]
        len_f = int.from_bytes(len1, 'big')
        reserv = data[6:10]
        shift = data[10:14]
        headSize = data[14:18]
        bWidth = data[18:22]
        bHeight = data[22:26]
        width = int.from_bytes(bWidth, 'big')
        height = int.from_bytes(bHeight, 'big')
        bColors = data[46:50]
        colors = int.from_bytes(bColors, 'big')

        info = data[0:54]

        for i in range(54 + 4 * colors, len(data)):
            buffer.append(data[i])
            k += 1
            if k == 4:
                buf = tuple(buffer)
                pixels.append(buffer)
                buffer = []
                k = 0
                del buf

        return pixels, info


def hide_byte_into_pixel(pixel, hide_byte):
    pixel[0] &= 0xFC
    pixel[0] |= (hide_byte >> 6) & 0x3
    pixel[1] &= 0xFC
    pixel[1] |= (hide_byte >> 4) & 0x3
    pixel[2] &= 0xFC
    pixel[2] |= (hide_byte >> 2) & 0x3
    pixel[3] &= 0xFC
    pixel[3] |= (hide_byte) & 0x3


def read_byte_from_pixel(byte_array):
    res = 0
    res |= ((byte_array[0] << 6) & 0xC0)
    res |= ((byte_array[1] << 4) & 0x30)
    res |= ((byte_array[2] << 2) & 0xC)
    res |= (byte_array[3] & 0x3)

    return res


def save(data, file_name):
    with open(file_name, 'w') as file:
        for dat in data:
            a = dat.to_bytes(1, byteorder='big').decode('CP1251')
            file.write(a)


def deshif(read_file, save_file):
    text = []
    pixels, info = open_pic(read_file)
    for pixel in pixels:
        a = read_byte_from_pixel(pixel)
        if a == 255: break
        text.append(a)

    save(text, save_file)


def save_cipher(file, info, data):
    with open(file, 'w+b') as f:
        f.write(info)
        for bit in data:
            for bi in bit:
                f.write(bi.to_bytes(1, 'big'))


def shifr(file_name, txt_name):
    with open(txt_name, 'rb') as file:
        data = bytearray(file.read())

    pixels, info = open_pic(file_name)

    k = 0
    for pixel, byte in zip(pixels, data):
        hide_byte_into_pixel(pixel, byte)
        k += 1
        print(k)

    save_cipher(file_name, info, pixels)


if __name__ == '__main__':
    deshif('5.bmp', 'decode.txt')
    shifr('1.bmp', 'code.txt')
    deshif('1.bmp', 'decode1.txt')
