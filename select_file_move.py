import os
import random
import shutil


def get_random_files(directory, file_extension, num_files):
    # 获取指定目录下特定扩展名的文件列表
    files = [file for file in os.listdir(directory) if file.endswith(file_extension)]

    # 从文件列表中随机选择指定数量的文件
    random_files = random.sample(files, num_files)

    return random_files


if __name__ == '__main__':
    source_directory = 'E:/yjy/Crowhunman/labels/labels/'  # 替换为要搜索的目录路径
    target_directory = 'E:/yjy/Crowhunman/crow_data/labels/val/'  # 替换为要将文件移动到的目标目录路径
    file_extension = '.txt'  # 替换为要选择的文件扩展名
    num_files = 600  # 替换为要选择的文件数量

    # 获取随机文件列表
    random_files = get_random_files(source_directory, file_extension, num_files)

    # 移动选中的文件到目标目录
    for file in random_files:
        source_path = os.path.join(source_directory, file)
        target_path = os.path.join(target_directory, file)
        shutil.move(source_path, target_path)
        print(f"File {file} moved to {target_directory}")