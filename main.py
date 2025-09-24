from agent import FFmpegAgent

def main():
    agent = FFmpegAgent()

    print("🎬 FFmpeg Agent 已启动，输入自然语言命令（输入 exit 退出）")
    while True:
        user_input = input("\n你: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 再见！")
            break

        response = agent.handle(user_input)
        print("🤖 Agent:", response)

if __name__ == "__main__":
    main()
