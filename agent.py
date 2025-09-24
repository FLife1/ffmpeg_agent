from nlp.intent_parser import parse_intent
from commands.builder import build_command
from executor.runner import run_command
from response.formatter import format_response

class FFmpegAgent:
    def handle(self, user_input: str) -> str:
        # 1. 解析意图
        task = parse_intent(user_input)
        if not task:
            return "抱歉，我没听懂你的命令。"

        # 2. 生成命令
        cmd = build_command(task)
        if not cmd:
            return "暂不支持该操作。"

        # 3. 执行命令
        success, output = run_command(cmd)

        # 4. 格式化结果
        return format_response(task, success, output)
