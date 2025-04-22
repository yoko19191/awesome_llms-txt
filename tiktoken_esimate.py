import os
import tiktoken
import pandas as pd
import datetime

def count_tokens(text, encoding):
    """mesure the token useage with tiktoken"""
    return len(encoding.encode(text))

def main():
    # initalize tokenier 
    encoding = tiktoken.get_encoding("o200k_base")
    
    results = []
    
    # for loop dirs under content dir
    for root, dirs, files in os.walk('content'):
        for file in files:
            # process .txt and .md file only
            if file.endswith(('.txt', '.md')):
                file_path = os.path.join(root, file)
                
                try:
                    # read file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # mersure token usage
                    token_count = count_tokens(content, encoding)
                    
                    # get modifeied date 
                    mod_time = os.path.getmtime(file_path)
                    mod_time_str = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
                    
                    # 
                    relative_path = root.replace('content', '', 1).lstrip(os.sep)
                    if not relative_path:
                        relative_path = '/'
                    
                    # 添加结果
                    results.append({
                        'path': relative_path,
                        'file': file,
                        'modified_date': mod_time_str,
                        'token_usage': token_count
                    })
                except Exception as e:
                    print(f"Estimate {file_path} tokens failed: {str(e)}")

    # save result as csv 
    df = pd.DataFrame(results)
    df.to_csv('token_usage.csv', index=False, encoding='utf-8-sig')
    print(f"token_usage.csv has been saved.")

if __name__ == "__main__":
    main()
