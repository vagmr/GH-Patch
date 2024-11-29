import os
import sys

def rename_x_files(directory):
    try:
        if not os.path.exists(directory):
            print(f"错误：目录 {directory} 不存在")
            return False
        
        items = os.listdir(directory)
        
        # 首先处理文件夹（为了避免重命名后路径变化导致的问题）
        for item in items:
            old_path = os.path.join(directory, item)
            if os.path.isdir(old_path) and item.startswith('x-'):
                new_name = item[2:]  # 删除 'x-' 前缀
                new_path = os.path.join(directory, new_name)
                
                if os.path.exists(new_path):
                    print(f"警告：目标路径已存在，跳过重命名: {new_path}")
                    continue
                
                try:
                    os.rename(old_path, new_path)
                    print(f"已重命名目录: {item} -> {new_name}")
                    old_path = new_path  # 更新路径
                except Exception as e:
                    print(f"重命名目录 {item} 时出错: {str(e)}")
                    continue
        
        # 重新获取目录列表（因为可能已经有重命名操作）
        items = os.listdir(directory)
        
        for item in items:
            current_path = os.path.join(directory, item)
            
            if not os.path.isdir(current_path) and item.startswith('x-'):
                new_name = item[2:]
                new_path = os.path.join(directory, new_name)
                
                if os.path.exists(new_path):
                    print(f"警告：目标文件已存在，跳过重命名: {new_path}")
                    continue
                
                try:
                    os.rename(current_path, new_path)
                    print(f"已重命名文件: {item} -> {new_name}")
                except Exception as e:
                    print(f"重命名文件 {item} 时出错: {str(e)}")
            
            # 递归处理子目录
            if os.path.isdir(current_path):
                rename_x_files(current_path)
        
        return True
        
    except Exception as e:
        print(f"处理目录 {directory} 时发生错误: {str(e)}")
        return False

if __name__ == "__main__":
    directory = "x-images"  # 指定目录
    
    try:
        if len(sys.argv) > 1:
            directory = sys.argv[1]
        
        print(f"开始处理目录: {directory}")
        success = rename_x_files(directory)
        
        if success:
            print("处理完成！")
        else:
            print("处理过程中出现错误！")
            
    except KeyboardInterrupt:
        print("\n程序被用户中断")
        sys.exit(1) 