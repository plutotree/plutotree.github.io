import os
import re
import pyperclip

def Upload(img):
    # 使用picgo上传，需要安装插件autocopy
    pyperclip.copy("")
    ret = os.system('picgo upload ./{}'.format(img))
    if ret != 0:
        print('图片[{}]上传失败'.format(img))
        return img
    new_img = pyperclip.paste().rstrip('\n')
    if not new_img:
        print('图片[{}]似乎上传失败'.format(img))
        return img
    print('图片[{}]上传成功 ->[{}]'.format(img, new_img))
    return new_img

def Process(root, file):
    content = ''
    print('process file:{}/{}'.format(root, file))
    inf = open('{}/{}'.format(root, file), 'r')
    for line in inf.readlines():
        result = re.finditer('!\[([^]]*)\]\(([^)]*)\)', line)
        update = False
        new_line = ''
        last_pos = 0
        for r in result:
            img = r.group(2)
            if not (img.startswith('http://') or img.startswith('https://')):
                update = True
                new_line += line[last_pos : r.start(2)]
                last_pos = r.end(2)
                new_line += Upload(img)
        new_line += line[last_pos:]
        if update:
            content += new_line
        else:
            content += line
    inf.close()

    outf = open('{}/{}'.format(root, file), 'w')
    outf.write(content)
    outf.close()

if __name__ == '__main__':
    for root, dirs, files in os.walk('./_posts/'):
        for file in files:
            if file.endswith(".md") or file.endswith(".markdown"):
                Process(root, file)
