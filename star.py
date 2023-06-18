import json

def calculate_average_vsini(data):
    # Dictionary to store the sums and counts for each "tayf"
    sums = {}
    counts = {}
    averages = []

    # Iterate over the data and calculate sums and counts for each "tayf"
    for item in data:
        tayf = item["tayf"]
        vsini = item["vsini"]

        if tayf in sums:
            sums[tayf] += vsini
            counts[tayf] += 1
        else:
            sums[tayf] = vsini
            counts[tayf] = 1

    # Calculate averages for each "tayf" and create the resulting list of dictionaries
    for tayf, sum_vsini in sums.items():
        count = counts[tayf]
        average = sum_vsini / count
        averages.append({"tayf": tayf, "avg": average})

    return averages

# Step 1: Open the file
file_path = "json_data.json"

# Step 2: Read the JSON data
with open(file_path, "r") as file:
    json_data = json.load(file)

# Step 3: Process the data
result = calculate_average_vsini(json_data)
output_file_path = "avg_result.json"

with open(output_file_path, "w") as output_file:
    json.dump(result, output_file, indent=4)

print("Dosya başarıyla oluşturuldu:", output_file_path)


