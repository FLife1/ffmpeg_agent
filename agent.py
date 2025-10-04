from nlp.intent_parser import parse_intent
from commands.builder import build_command
from executor.runner import run_command
from response.formatter import format_response

class FFmpegAgent:
    def handle(self, user_input: str) -> str:
        # 先分析inputinput
        task = parse_intent(user_input)
        if not task:
            return "听不懂"

        # cmd生成+执行
        cmd = build_command(task)
        if not cmd:
            return "不会"
        success, output = run_command(cmd)

        # 格式化结果
        return format_response(task, success, output)
