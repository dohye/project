#### github 시작할 때
- git init
- git add README.md
- git commit -m "first commit"
- git remote add origin https://github.com/dohye/study.git
- git push -u origin master

#### git에 파일 올리기 

- cmd 에서
- cd C:\Users\dohye\Desktop\git
- git init
- git add .
- git commit -m "adding files" # add 된 file 명 볼 수 있음 , ""안에 들어가는 말은 내가 남기고자 하는 메세지, 코드의 변경사항, 기능 추가 등 이런 내용을 짧게 작성
- git remote add origin https://github.com/dohye/study.git
- git push origin master

#### push 오류나서 pull 해준 후 다시 push
- git pull --rebase origin master
- git push origin master

#### CRLF will be replaced by LF 에러날때
- git config --global core.autocrlf true
- 이 프로젝트만 해결하고싶으면 --global 빼도됨 

####  [rejected] master -> master (non-fast-forward) 에러날때 (근데 함부로 하면 안된다고 함)
- git pull origin master --allow-unrelated-histories

#### github error : 'commit' is not possible because you have unmerged files.
이건 내가 git폴더에서 가지고 있는 파일이랑 git 페이지에서 가지고 있는 파일이랑 달라서 나타나는 오류. merge가 안됬다. 즉, merge를 해야함

- cd C:\Users\dohye\Desktop\git
- git init
- git status # 에러난 파일 확인
- git reset 파일이름
- git add 파일이름
- git commit -m "adding files" # add 된 file 명 볼 수 있음
- git remote add origin https://github.com/dohye/study.git
- git push origin master

#### push 강제로 하는 방법
- git push -f origin master


<br/>

#### push, pull, commit

- 방금 만든 파일은 현재 우리 컴퓨터 디렉토리(작업 디렉토리)에 있습니다.
- 이 파일을 깃에 전달하기 위해서는 준비를 해야합니다(스테이징 영역) # add해주면 스테이징 영역으로 이동
- 준비가 된 파일들을 전달합니다(커밋 - 로컬저장소)
- 커밋한 파일들을 원격저장소로 업로드합니다(푸시- 원격저장소)

출처 : <https://codevkr.tistory.com/46>

#### Git의 구조 알아보기
출처 : <https://victorydntmd.tistory.com/72>
