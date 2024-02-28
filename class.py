import hashlib  # hashlib 모듈 적용


# ----- 코드 정의 ------
class Member:
    name = ""
    username = ""
    password = 0000

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        # 비밀번호 sha256 방식으로 저장
        m = hashlib.sha256()
        self.password = m.update(str(password).encode('utf-8'))
        # hashlib.sha256()로 생성한 객체 m에 해싱할 문자열을 인수로 update() 함수를 호출하면 문자열이 해싱
        # 유니코드 문자열을 UTF-8 형식의 바이트 문자열로 변환
        print(m.digest())
        # 문자열을 해싱한 다음에는 digest() 또는 hexdigest() 함수를 사용하여 해싱한 문자열을 얻을 수 있다.

    def display(self):
        print(f"당신의 이름은 {self.name}, 아이디는 {self.username} 입니다.")


class Post:
    title = ""
    content = ""

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"{self.title}, {self.content}, {self.author}")


Jin = Member("Jin", "Won", 0000)
Bang = Member("Bang", "Yu", 1111)
Sugar = Member("Sugar", "Lily", 2222)


# ----- 코드 실행 ------
members = []
posts = []

members.append(Jin)
members.append(Bang)
members.append(Sugar)

for i in members:
    i.display()

for i in members:
    if (i.name == "Jin"):
        posts.append(Post("ㅋㅋㅋ", "이름 : Jin, 아이디 : Won", i.username))
    if (i.name == "Bang"):
        posts.append(Post("음?", "이름 : Bang, 아이디 : Yu", i.username))
    if (i.name == "Sugar"):
        posts.append(Post("나는 도마뱀", "이름 : Sugar, 아이디 : Lily", i.username))

# 멤버 만들기
while (True):
    print("멤버를 생성하겠습니까? y / n")
    answer = input()

    if (answer.lower() == 'y'):
        print("이름을 입력하세요 : ")
        new_name = input()
        print("아이디를 입력하세요 : ")
        new_username = input()
        print("비밀번호를 입력하세요 : ")
        new_password = input()
        members.append(Member(new_name, new_username, new_password))
        print("멤버 생성이 완료되었습니다.")
        continue
    elif (answer.lower() == 'n'):
        for i in members:
            i.display()
        break
    else:
        print("유효하지 않은 문자입니다. y / n 중 입력해주세요")
        continue


# 포스트 생성
while True:
    right = 0
    print("포스트를 생성하시겠습니까? y /n ")
    answer = input()

    if (answer.lower() == 'y'):
        print("제목을 입력하세요 : ")
        new_title = input()
        print("내용을 입력하세요 : ")
        new_content = input()
        print("작성자를 입력하세요 : ")
        new_author = input()

        for i in members:
            if (new_author == i.username):
                right += 1

        if (right == 0):
            print("올바른 사용자가 아닙니다. 올바른 사용자를 입력해주세요.")
            continue
        posts.append(Post(new_title, new_content, new_author))
        print("포스트 생성이 완료되었습니다.")
        continue
    elif (answer.lower() == 'n'):
        for i in members:
            i.display()
        break
    else:
        print("유효하지 않은 입력입니다. y / n 중 입력해주세요.")
        continue

# 특정 사용자 게시물 제목 표시
id_cheak = input("검색하고 싶은 ID를 입력하세요 : ")

for member in members:
    if (member.username == id_cheak):
        for post in posts:
            if post.author == id_cheak:
                print(f"{id_cheak}의 게시물 제목 : {post.title}")

# 특정 단어가 포함된 게시물의 제목 출력
content_cheak = input("검색하고 싶은 단어를 입력하세요 : ")

for post in posts:
    if content_cheak in post.title:
        for member in members:
            if member.username == post.author:
                print(f"게시물 제목 : {post.title}, 작성자 : {member.username}")
