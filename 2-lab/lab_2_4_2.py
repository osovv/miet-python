from pathlib import Path

def main():
        Path("./example").mkdir(exist_ok=True)
        extensions = [
            'foo', 'bar', 'baz', 'miet', 'sber', 'lab', 'python', 'masters', 'degree', 'test'
        ]
        for i in range(100):
            Path(f"./example/{i}.{extensions[i % 10]}").write_text(f"File #{i+1}")



if __name__ == '__main__':
    main()
