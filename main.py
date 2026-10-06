from board import write_board,list_board,find_board,content_board,delete_board
from storage import load_board,save_board

def main():
    texts = load_board()
    if texts:
        text=texts[-1]
        next_number=text['번호']
    else:
        next_number = 0
    print("======게시판 작성 프로그램======")
    menu(texts,next_number)

def menu(texts,next_number):
    while True:
            print("1.게시글 작성")
            print("2.게시글 목록")
            print("3.제목 검색")
            print("4.글 상세 보기")
            print("5.글 삭제")
            print("6.종료")
            choice = input("메뉴 번호를 입력해주세요: ")
            if choice == "1":
                next_number=write_board(texts,next_number)
                save_board(texts)
            elif choice == "2":
                list_board(texts)
            elif choice == "3":
                find_board(texts)
            elif choice == "4":
                content_board(texts)
            elif choice == "5":
                delete_board(texts)
                save_board(texts)
            elif choice == "6":
                print("프로그램을 종료합니다")
                return
            else:
                print("잘못입력하셨습니다.")

if __name__ == "__main__":
    main()