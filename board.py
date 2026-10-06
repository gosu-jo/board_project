def write_board(texts,next_number):
    title = input("제목을 입력해주세요: ").strip()
    author = input("작성자를 입력해주세요: ").strip()
    content = input("내용을 입력해주세요: ").strip()
    next_number += 1
    text = {"번호" : next_number , "제목" : title , "저자" : author , "내용" : content}
    texts.append(text)
    return texts,next_number

def list_board(texts):
    if not texts:
        print("저장된 게시글이 없습니다.")
        return
    for text in texts:
        print(f"{text['번호']} . {text['제목']} : {text['저자']}")

def find_board(texts):
    if not texts:
        print("저장된 게시글이 없습니다.")
        return
    find_text = input("검색할 제목을 입력해주세요: ").strip()
    find_texts = []
    for text in texts:
        if find_text in text["제목"]:
            key = text["제목"]
            find_texts.append(key)
            print(f"{text["제목"]}")
    if not find_texts:
        print("검색 결과가 없습니다.")
   
        



def content_board(texts):
    list_board(texts)
    if not texts:
        return
    while True:
        try:
            choice = int(input("상세내용을 볼려면 게시판 번호를 눌러주세요: "))
            test = test_number(texts,choice)
            if test:
                print("잘못입력하셨습니다.")
                continue
            for text in texts:
                if choice == text['번호']:
                    print(f"{text['번호']} . {text['제목']} - {text['저자']} : {text['내용']}")
                    return
        except ValueError:
            print("잘못된입력입니다.")


def delete_board(texts):
    list_board(texts)
    if not texts:
        return
    while True:
        try:
            choice = int(input("삭제할 번호를 입력해주세요: "))
            test = test_number(texts,choice)
            if test:
                print("잘못입력하셨습니다.")
                continue
            for index,text in enumerate(texts):
                if choice == text['번호']:
                    delete_text =texts.pop(index)
                    print(f"{delete_text['제목']}이 삭제되었습니다.")
                    return
            
                
        except ValueError:
            print("잘못된 입력입니다.")

def test_number(texts,choice):
    number_texts = []
    for text in texts:
        number_text = text['번호']
        number_texts.append(number_text)
    if not choice in number_texts:
        return True