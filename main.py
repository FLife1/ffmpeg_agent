from agent import FFmpegAgent

def main():
    agent = FFmpegAgent()

    print("FFmpeg Agent 已启动，输入命令（ exit 可退出）")
    while True:
        user_input = input("\n你: ")
        if user_input.lower() in ["exit", "quit"]:
            print("bye bye~")
            break

        response = agent.handle(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    main()
