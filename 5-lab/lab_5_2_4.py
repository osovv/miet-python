import os
import concurrent.futures

def search_in_file(file_path, keyword):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        if keyword in file.read():
            return file_path
    return None

def search_in_directory(directory, keyword):
    txt_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if f.endswith('.txt')]
    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(search_in_file, file, keyword): file for file in txt_files}
        for future in concurrent.futures.as_completed(future_to_file):
            file_path = future_to_file[future]
            if future.result():
                results.append(file_path)

    return results

keyword = "key"

search_results = search_in_directory('.', keyword)
print(search_results)
