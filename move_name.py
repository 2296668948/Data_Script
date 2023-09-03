import os
import shutil

def move_matching_images(image_directory, txt_directory, target_directory):
    # 获取txt文件名列表
    txt_files = os.listdir(txt_directory)
    txt_filenames = [os.path.splitext(txt_file)[0] for txt_file in txt_files]

    # 遍历图片文件夹中的文件
    for image_file in os.listdir(image_directory):
        image_path = os.path.join(image_directory, image_file)
        if os.path.isfile(image_path):
            # 检查图片文件名是否与txt文件名匹配
            image_filename = os.path.splitext(image_file)[0]
            if image_filename in txt_filenames:
                # 移动匹配的图片到目标文件夹
                target_path = os.path.join(target_directory, image_file)
                shutil.move(image_path, target_path)
                print(f"Moved image {image_file} to {target_directory}")

if __name__ == '__main__':
    image_directory = 'E:/yjy/Crowhunman/images/'  # 替换为图片文件夹的路径
    txt_directory = 'E:/yjy/Crowhunman/crow_data/labels/val/'  # 替换为txt文件夹的路径
    target_directory = 'E:/yjy/Crowhunman/crow_data/images/val/'  # 替换为目标文件夹的路径

    # 移动匹配的图片到目标文件夹
    move_matching_images(image_directory, txt_directory, target_directory)