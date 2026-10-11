import json

with open('digits_data.json') as f:
    data = json.load(f)

lines = []
for item in data:
    lines.append(f'  "{item["label"]}:{item["hex"]}"')

output = "const RAW_DIGITS_DATA = [\n" + ",\n".join(lines) + "\n];\n"

with open('dataset_js.txt', 'w') as f:
    f.write(output)

print("Created dataset_js.txt with", len(lines), "samples.")
