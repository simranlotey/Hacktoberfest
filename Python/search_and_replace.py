class FileModifier:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def _load_content(self):
        with open(self.file_path, 'r') as f:
            return f.read()

    def _save_content(self, new_content):
        with open(self.file_path, 'w') as f:
            f.write(new_content)

    def modify(self, target, replacement):
        content = self._load_content()
        if target in content:
            updated_content = content.replace(target, replacement)
            self._save_content(updated_content)
            print(f"Occurrences of '{target}' have been replaced with '{replacement}'.")
        else:
            print(f"'{target}' not found in the file.")

def main():
    path = input("Provide the file path: ").strip()
    target_text = input("Text to find: ").strip()
    replacement_text = input("Text to replace with: ").strip()

    modifier = FileModifier(path)
    modifier.modify(target_text, replacement_text)

if __name__ == "__main__":
    main()
