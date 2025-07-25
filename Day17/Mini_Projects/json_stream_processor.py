import json

def json_stream_processor(filepath, stop_key=None, stop_value=None):
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                yield obj
                if stop_key and obj.get(stop_key) == stop_value:
                    print(f" Stop condition met at: {obj}")
                    return  # Stop generator
            except json.JSONDecodeError:
                print(f" Skipping invalid JSON line: {line}")

if __name__ == "__main__":
    for item in json_stream_processor("data.json", stop_key="name", stop_value="Charlie"):
        print(" Parsed:", item)

