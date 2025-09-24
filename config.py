import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
