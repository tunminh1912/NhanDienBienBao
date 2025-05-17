import os
import shutil
import random

# Định nghĩa đường dẫn
dataset_path = "Dataset"  # Thư mục gốc chứa dữ liệu
image_dir = os.path.join(dataset_path, "images")
label_dir = os.path.join(dataset_path, "labels")

# Tạo thư mục train, val, test
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(dataset_path, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(dataset_path, split, "labels"), exist_ok=True)

# Lấy danh sách file ảnh
images = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]

# Xáo trộn ngẫu nhiên danh sách ảnh
random.shuffle(images)

# Xác định số lượng dữ liệu
num_total = len(images)
num_train = int(num_total * 0.8)
num_val = int(num_total * 0.1)
num_test = num_total - num_train - num_val

# Chia dữ liệu
train_images = images[:num_train]
val_images = images[num_train:num_train + num_val]
test_images = images[num_train + num_val:]

# Hàm di chuyển file
def move_files(file_list, split):
    for file in file_list:
        img_src = os.path.join(image_dir, file)
        label_src = os.path.join(label_dir, file.replace(".jpg", ".txt"))

        img_dst = os.path.join(dataset_path, split, "images", file)
        label_dst = os.path.join(dataset_path, split, "labels", file.replace(".jpg", ".txt"))

        shutil.move(img_src, img_dst)
        shutil.move(label_src, label_dst)

# Di chuyển file vào thư mục tương ứng
move_files(train_images, "train")
move_files(val_images, "val")
move_files(test_images, "test")

print("✅ Chia tập dữ liệu hoàn tất!")
