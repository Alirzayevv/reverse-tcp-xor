def xor_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()

    key_length = len(key)
    output_data = bytearray(len(data))

    for i in range(len(data)):
        output_data[i] = data[i] ^ ord(key[i % key_length])

    with open(output_file, 'wb') as f:
        f.write(output_data)

#usage
input_file = 'reverse_tcp_9613.exe'
output_file = 'out.exe'
key = "alirzayev"

xor_file(input_file, output_file, key)
print(f"XOR operation completed. Output saved to '{output_file}'.")
