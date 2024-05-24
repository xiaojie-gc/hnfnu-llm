import json
from read_old_format import get_qa
import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description='Description of your script.')

# 输入数据文件
parser.add_argument('input', default='train.json', type=str, help='Description of arg1')
# 输出数据文件
parser.add_argument('output', default='data.json', type=str, help='Description of arg2')

# Parse the arguments
args = parser.parse_args()

#可以通过文心一言跟它说 把下面问题和回答分别整理成列表形式（重点）
# 定义问答对

questions, answers = get_qa(args.input)

try:
        # 尝试读取JSON文件中的数据
    with open(args.output, 'r',encoding='utf-8') as file:
            or_data = json.load(file)     #原始的列表 json数据
except FileNotFoundError:
        # 如果文件不存在，创建一个空列表（假设我们期望一个列表作为JSON的根）
        or_data=[]

json_data = or_data

# 构建JSON数据格式
for q, a in zip(questions, answers):
    conversation_data = []
    conversation_data.append({"role": "user", "content": q})
    conversation_data.append({"role": "assistant", "content": a})
    json_data.append({"conversations": conversation_data })


#重新加载数据
with open(args.output, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)


#查看总共收集的数据（一问一答，算一个数据）
print(len(json_data))

