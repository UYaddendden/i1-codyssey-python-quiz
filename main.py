def show_menu():
    print("=" * 32)
    print("       항공우주 퀴즈 게임")
    print("=" * 32)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록 확인")
    print("4. 최고 점수 확인")
    print("5. 종료")
    print("=" * 32)


def main():
    while True:
        show_menu()

        try:
            choice = input("메뉴를 선택하세요 (1~5): ").strip()

        except (KeyboardInterrupt, EOFError):
            print("\n게임을 종료합니다.")
            break

        if choice == "1":
            print("퀴즈 풀기 기능은 개발 예정입니다.")

        elif choice == "2":
            print("퀴즈 추가 기능은 개발 예정입니다.")

        elif choice == "3":
            print("퀴즈 목록 기능은 개발 예정입니다.")

        elif choice == "4":
            print("최고 점수 기능은 개발 예정입니다.")

        elif choice == "5":
            print("게임을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 1~5 중에서 선택하세요.")

        print()


if __name__ == "__main__":
    main()
