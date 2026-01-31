import os
from PIL import Image, ImageSequence

def extract_frames(source_dir, output_root):
    """
    遍历源文件夹，提取动图（GIF/APNG）的每一帧并保存到独立文件夹中。
    """
    # 确保输出根目录存在
    if not os.path.exists(output_root):
        os.makedirs(output_root)
        print(f"创建输出根目录: {output_root}")

    # 支持的后缀名（虽然有些APNG可能是.png后缀，我们也会处理）
    valid_extensions = ('.gif', '.apng', '.png')

    # 遍历文件夹
    for filename in os.listdir(source_dir):
        if not filename.lower().endswith(valid_extensions):
            continue

        file_path = os.path.join(source_dir, filename)
        
        try:
            with Image.open(file_path) as img:
                # 检查是否是动图
                # n_frames 是 Pillow 提供的属性，表示总帧数
                if not getattr(img, "is_animated", False):
                    print(f"跳过非动图文件: {filename}")
                    continue

                print(f"正在处理: {filename} (共 {img.n_frames} 帧)")

                # 为该动图创建一个独立的文件夹
                # 使用文件名（不含后缀）作为文件夹名
                folder_name = os.path.splitext(filename)[0]
                output_dir = os.path.join(output_root, folder_name)
                
                # 如果文件夹已存在，为了避免混淆，我们可以加个后缀或者直接清空，
                # 这里我们直接创建（如果不存在）
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                # 逐帧导出
                for i, frame in enumerate(ImageSequence.Iterator(img)):
                    # 每一帧保存为 i+1.png
                    # 注意：有些动图（如GIF）的帧可能有透明度处理（Dispose模式），
                    # 使用 ImageSequence.Iterator 通常能较好地处理这些。
                    # 为了确保每一帧都是完整的，我们可以将其转换为 RGBA
                    frame_path = os.path.join(output_dir, f"{i + 1}.png")
                    
                    # 转换为 RGBA 确保透明度正常保留，并且统一格式
                    # 如果是 APNG，Pillow 10+ 已经能很好地处理合成
                    frame.convert("RGBA").save(frame_path, "PNG")

                print(f"成功导出到: {output_dir}")

        except Exception as e:
            print(f"处理文件 {filename} 时出错: {e}")

if __name__ == "__main__":
    import sys
    
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2] if len(sys.argv) > 2 else "output"
    else:
        # 如果没有参数，则进入交互模式
        input_folder = input("请输入包含动图的文件夹路径: ").strip()
        output_folder = input("请输入导出图片存放的根路径 (直接回车默认为 'output'): ").strip()
        if not output_folder:
            output_folder = "output"

    if os.path.isdir(input_folder):
        extract_frames(input_folder, output_folder)
        print("\n所有任务处理完成！")
    else:
        print(f"错误：文件夹路径 '{input_folder}' 不存在。")
