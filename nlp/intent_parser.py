import re
from config import OPENAI_API_KEY

def parse_with_rules(text: str):
    text = text.lower()

    # 转换格式
    match = re.match(r".*?(\S+)\.(\w+).*转换.*(\w+)", text)
    if match:
        return {
            "action": "convert",
            "input": match.group(1) + "." + match.group(2),
            "output": match.group(1) + "." + match.group(3),
        }

    # 提取音频
    match = re.match(r".*?(\S+)\.(\w+).*提取.*(mp3|m4a|aac)", text)
    if match:
        return {
            "action": "extract_audio",
            "input": match.group(1) + "." + match.group(2),
            "output": match.group(1) + "." + match.group(3),
        }

    # 截图
    match = re.match(r".*?(\S+)\.(\w+).*在 (\d+:\d+:\d+).*截.*(png|jpg)", text)
    if match:
        return {
            "action": "screenshot",
            "input": match.group(1) + "." + match.group(2),
            "time": match.group(3),
            "output": match.group(1) + "_shot." + match.group(4),
        }

    # 水印
    match = re.match(r".*?(\S+)\.(\w+).*水印.*?(\S+)\.(png|jpg)", text)
    if match:
        return {
            "action": "watermark",
            "input": match.group(1) + "." + match.group(2),
            "watermark": match.group(3) + "." + match.group(4),
            "output": match.group(1) + "_wm." + match.group(2),
        }

    return None


def parse_with_llm(text: str):
    if not OPENAI_API_KEY:
        return None

    from openai import OpenAI
    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
    你是一个FFmpeg命令助手。
    用户输入: "{text}"
    请输出一个JSON，包含:
    - action: 操作类型 (convert, extract_audio, screenshot, watermark, merge)
    - input: 输入文件名
    - output: 输出文件名
    - time: (可选) 截图时间
    - watermark: (可选) 水印图片文件
    - files: (可选) 合并文件列表
    """

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        import json
        return json.loads(resp.choices[0].message.content.strip())
    except Exception as e:
        print("LLM 解析失败:", e)
        return None


def parse_intent(text: str):
    # rules to anay
    task = parse_with_rules(text)
    if task:
        return task

    task = parse_with_llm(text)
    return task
