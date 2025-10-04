def build_command(task: dict):
    action = task["action"]

    if action == "convert":
        return f'ffmpeg -i "{task["input"]}" "{task["output"]}"'

    if action == "extract_audio":
        return f'ffmpeg -i "{task["input"]}" -vn "{task["output"]}"'

    if action == "screenshot":
        return f'ffmpeg -i "{task["input"]}" -ss {task["time"]} -frames:v 1 "{task["output"]}"'

    if action == "watermark":
        return f'ffmpeg -i "{task["input"]}" -i "{task["watermark"]}" -filter_complex "overlay=10:10" "{task["output"]}"'

    return None
