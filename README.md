# showmethatcode

## 1. 기본 셋팅


### `git & ssh` 설정

[참고 사이트](https://xho95.github.io/macos/security/openssh/ssh/gitlab/2017/02/21/Using-SSH-on-Mac.html)

### 프로젝트 `clone`

[showmethatcode Repository](https://github.com/showmethatcode/showmethatcode-server)
```bash
$ git clone git@github.com:showmethatcode/showmethatcode-server.git
```

### `pip` & 가상환경 라이브러리 설치 및 실행
```bash
$ sudo easy_install pip
$ sudo pip install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

### `requirements` 라이브리러 설치

```bash
# 반드시 가상환경으로 프로젝트 폴더 안에서 실행
$ pip3 install -r requirements.txt
```


## 2. 구글 API KEY 환경 변수 셋팅
> google key와 secret key는 팀원이 제공합니다

```bash
$ echo 'export SOCIAL_AUTH_GOOGLE_OAUTH2_KEY="[your google key]"' >> ~/.zshrc
$ echo 'export SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET="[your google secret key]"' >> ~/.zshrc
$ source ~/.zshrc
```

## 3. 서버 실행

```bash
$ python manage.py migrate
$ python manage.py runserver
```
