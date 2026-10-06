import json

FILENAME = "BOARD.JSON"
def load_board():
    try:
        with open(FILENAME,"r",encoding='utf-8')as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_board(texts):
    with open(FILENAME,"w",encoding='utf-8')as file:
        json.dump(texts,file,ensure_ascii=False,indent=4)