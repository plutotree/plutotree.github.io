import os
import re
import yaml
from datetime import datetime

def process_md_files():
    # 遍历当前目录所有文件[1,3](@ref)
    for filename in os.listdir('.'):
        # 匹配YYYY-MM-DD-xxxx.md格式的文件[5](@ref)
        if re.match(r'^\d{4}-\d{2}-\d{2}-.+\.md$', filename):
            print(f"处理文件: {filename}")
            
            # 提取文件名各部分
            date_str, slug_part = filename[:10], filename[11:-3]
            ymd = filename[:10].split('-')
            
            # 读取文件内容
            with open(filename, 'r+', encoding='utf-8') as f:
                content = f.read()
                
                # 分割front matter和正文[6,7](@ref)
                front_matter_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
                
                if front_matter_match:
                    yaml_content, body = front_matter_match.groups()
                    
                    # 解析YAML
                    data = yaml.safe_load(yaml_content)
                    
                    # 添加slug字段[5](@ref)
                    if 'slug' not in data:
                        data['slug'] = slug_part
                        
                    # 添加aliases字段[5](@ref)
                    alias_path = f"/{date_str}/{slug_part}.html"
                    aliases = data.get('aliases', [])
                    if not any(alias_path in s for s in aliases):
                        aliases.insert(0, alias_path)
                        data['aliases'] = aliases
                    
                    # 生成新的YAML内容[7](@ref)
                    new_yaml = yaml.dump(
                        data,
                        allow_unicode=True,
                        sort_keys=False,
                        default_flow_style=None
                    )
                    
                    # 重组文件内容
                    new_content = f"---\n{new_yaml}---\n{body}"
                    
                    # 回写文件[5](@ref)
                    f.seek(0)
                    f.write(new_content)
                    f.truncate()

if __name__ == '__main__':
    process_md_files()
