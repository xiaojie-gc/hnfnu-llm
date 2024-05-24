# hnfnu-llm
把原始的AdvertiseGen数据转换为chatGLM3支持的格式：

{"conversations": [{"role": "user", "content": "类型#裙*裙长#半身裙"}, {"role": "assistant", "content": "这款百搭时尚的仙女半身裙，整体设计非常的飘逸随性，穿上之后每个女孩子都能瞬间变成小仙女啦。料子非常的轻盈，透气性也很好，穿到夏天也很舒适。"}]}

使用：python prepare_data.py <input json file> <output json file>

