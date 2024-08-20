import os

def delete_files(directory, txt_file, encoding='utf-8'):
    # 打开txt文件并读取文件名
    with open(txt_file, 'r', encoding=encoding) as file:
        filenames = file.read().splitlines()

    # 遍历文件名列表，删除对应的文件
    for filename in filenames:
        file_path = os.path.join(directory, filename)
        if os.path.exists(file_path):
            # 修改文件属性为可写
            os.chmod(file_path, 0o777)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        else:
            print(f"File not found: {file_path}")

# 指定目录和txt文件路径
directory = r'E:\博客markdown\图片'
txt_file = r'F:\python\request.txt'

# 调用函数删除文件
delete_files(directory, txt_file)