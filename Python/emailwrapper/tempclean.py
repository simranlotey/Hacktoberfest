                                                            import gc
import os
import shutil
import tempfile


# Clean temporary files
def clean_temp_files():
    """Remove temporary files."""
    temp_dir = tempfile.gettempdir()
    try:
        for root, dirs, files in os.walk(temp_dir):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Failed to remove {file_path}: {e}")
            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    shutil.rmtree(dir_path)
                except Exception as e:
                    print(f"Failed to remove {dir_path}: {e}")
    except Exception as e:
        print(f"Error cleaning temporary files: {e}")


# Clean RAM
def clean_ram():
    """Force garbage collection to clean up RAM."""
    gc.collect()
