def write_board(texts,next_number):
    title = input("제목을 입력해주세요: ").strip()
    author = input("작성자를 입력해주세요: ").strip()
    content = input("내용을 입력해주세요: ").strip()
    next_number += 1
    text = {"번호" : next_number , "제목" : title , "저자" : author , "내용" : content}
    texts.append(text)
    return next_number

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
    check = False
    for text in texts:
        if find_text in text["제목"]:
            print(f"{text['제목']}")
            check = True
    if not check:
        print("검색 결과가 없습니다.")
   
        



def content_board(texts):
    list_board(texts)
    if not texts:
        return
    print("내용 상세 보기")
    
    
    choice=check_choice(texts)
    
    text=find_text_board(texts,choice)[0]
    print(f"{text['번호']} . {text['제목']} - {text['저자']} : {text['내용']}")
    
    


def delete_board(texts):
    list_board(texts)
    if not texts:
        return
    print("게시판 삭제")
    
    choice=check_choice(texts)     
        
    text,index=find_text_board(texts,choice)
    texts.pop(index)
    print(f"{text['제목']}이 삭제되었습니다.")

def test_number(texts,choice):
    for text in texts:
        if choice == text['번호']:
            return False
    return True

def check_choice(texts):
    while True:
        try:
            choice = int(input("번호를 입력해주세요: "))
            test = test_number(texts,choice)
            if test:
                print("잘못입력하셨습니다.")
                continue
            return choice
        except ValueError:
            print("잘못입력하셨습니다.")

def find_text_board(texts,choice):
    for index,text in enumerate(texts):
        if choice == text['번호']:
            return text,index