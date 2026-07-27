import os

directory = 'c:/Users/WELCOME/Desktop/CODE 99/PROJECT/1'
for root, _, files in os.walk(directory):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.css')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace href="./" with href="" and src="./" with src=""
            new_content = content.replace('href="./', 'href="').replace('src="./', 'src="')
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file}")
