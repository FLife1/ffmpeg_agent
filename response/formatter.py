def format_response(task, success, output):
    if not success:
        return f"执行失败: {output}"

    action = task["action"]

    if action == "convert":
        return f"{task['input']} 转换为 {task['output']}"

    if action == "extract_audio":
        return f"{task['output']}"

    if action == "screenshot":
        return f"{task['time']} 截取截图 {task['output']}"

    if action == "watermark":
        return f"{task['input']} 添加水印，保存为 {task['output']}"

    return "ok"
