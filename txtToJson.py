import json

file_path = "yildiz.txt"

def txt_to_json(file_path):
    # Step 1: Open the file
    with open(file_path, "r") as file:
        # Step 2: Read the contents
        file_contents = file.readlines()
    return file_contents

# Step 3: Process the data
lines = txt_to_json(file_path)
formatted_data = []

for line in lines:
    values = line.split()
    if len(values) == 2:
        formatted_data.append({"tayf": float(values[0]), "vsini": float(values[1])})

# Step 4: JSON formatını dosyaya yazma
output_file_path = "json_data.json"

with open(output_file_path, "w") as output_file:
    json.dump(formatted_data, output_file, indent=4)

print("Dosya başarıyla oluşturuldu:", output_file_path)
