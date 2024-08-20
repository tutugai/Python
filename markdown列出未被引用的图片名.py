import os
import re

def find_images_in_markdown(directory):
    markdown_files = get_markdown_files(directory)
    image_names = set()

    for file in markdown_files:
        with open(file, 'r', encoding='latin1') as f:
            content = f.read()
            images = re.findall(r'!\[.*?\]\((.*?)\)', content)
            for image in images:
                image_name = os.path.basename(image)
                image_names.add(image_name)

    return image_names

def find_missing_images(image_directory, markdown_directory):
    image_names = get_all_image_names(image_directory)
    markdown_images = find_images_in_markdown(markdown_directory)
    missing_images = sorted(image_names - markdown_images)

    return missing_images

def get_markdown_files(directory):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def get_all_image_names(directory):
    image_names = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif','webp')):
                image_names.add(file)
    return image_names

# 指定图片目录和Markdown目录的路径
image_directory = 'E:\博客markdown\图片'
markdown_directory = 'E:\博客markdown'

# 检查不存在于Markdown文档中的图片名称
missing_images = find_missing_images(image_directory, markdown_directory)

# 将结果排序并输出到request.txt文件
output_file = 'request.txt'
missing_images.sort()
with open(output_file, 'w', encoding='utf-8') as f:
    for image_name in missing_images:
        f.write(image_name + '\n')

print("Missing images have been written to", output_file)