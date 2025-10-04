import os
from dotenv import load_dotenv

# 加载 .env 文件，别把.env的key传上来了啊啊啊啊！！！
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
