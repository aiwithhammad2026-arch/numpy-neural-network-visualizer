import urllib.request, gzip, csv, base64

url = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/main/sklearn/datasets/data/digits.csv.gz'
data = gzip.decompress(urllib.request.urlopen(url).read()).decode('utf-8')
reader = csv.reader(data.strip().split('\n'))
rows = list(reader)

buf = bytearray()
for r in rows:
    buf.append(int(r[64])) # label: 0-9
    for v in r[:64]:
        buf.append(int(v)) # pixel: 0-16

b64 = base64.b64encode(buf).decode('ascii')
print('Samples:', len(rows), 'Total bytes:', len(buf), 'Base64 length:', len(b64))

with open('digits_dataset_b64.js', 'w') as f:
    f.write('const DIGITS_B64 = "' + b64 + '";\n')
print('Wrote digits_dataset_b64.js successfully')
