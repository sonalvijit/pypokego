import os

def load_asset(addr:str):
     txt_files_data = []

     if not os.path.isdir(addr):
         raise ValueError(f"Provided path '{addr}' is not a directory.")
     
     for filename in os.listdir(addr):
          file_path = os.path.join(addr, filename)

          if not os.path.isfile(file_path):
               continue

          try:
               with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    txt_files_data.append({
                         "filename": filename,
                         "content": content,
                         "path": file_path
                    })
          except (UnicodeDecodeError, OSError) as e:
               print(f"Error reading file {filename}: {e}")
     
     return txt_files_data

a = load_asset("assets/colorscripts/regular/")
for i in a:
     print(i["content"])
     break