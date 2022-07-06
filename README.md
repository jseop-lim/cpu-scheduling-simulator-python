# cpu-scheduling-simulator-python

운영체제 CPU 스케줄링 알고리즘 7가지(FCFS, SJF, SRTF, 우선순위, 선점 우선순위, 비선점 우선순위 & RR)를 python을 이용해 구현했다.

GUI 도구로 Pygame과 plotly를 이용했다.

## Table of Contents

- [Background](#background)
- [Quickstart](#quickstart)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Documents](#documents)
- [Contributors](#contributors)

## Background

2022학년도 1학기 운영체제 과목 텀프로젝트로 진행되었다.

팀은 4인 1조로 구성되었다.

## Quickstart

*두 가지* 방법으로 실행 파일을 설치 및 실행할 수 있다.

Windows에서는 .exe 파일 실행을 포함한 모든 방법을 지원하며, Linux 및 MacOS에서는 .py 파일 실행만 가능하다.

### 1. Execute .exe file

📁 [exe 파일 다운로드](https://github.com/jseop-lim/cpu-scheduling-simulator-python/raw/main/cpu-scheduler.exe)

위 링크에서 `cpu-scheduler.exe`를 설치하고 실행한다.

### 2. Execute .py file

>  Python과 pip이 미리 설치되어 있어야 한다.

레포지토리를 GitHub에서 다운 받는다.

```shell
git clone https://github.com/jseop-lim/cpu-scheduling-simulator-python.git
```

프로젝트 경로로 이동하고 python venv 모듈을 이용하여 `env`라는 이름의 가상환경을 생성한다.

```shell
cd cpu-scheduling-simulator-python
python -m venv env
```

가상환경을 활성화한다.

```shell
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

pip을 업그레이드하고 필요한 패키지를 설치한다.

```shell
pip install --upgrade pip
pip install -r requirements.txt
```

`main_gui.py` 파일을 실행한다.

```shell
python main_gui.py
```

## Usage

### Build .exe file

Window 환경 기준으로, pyinstaller 패키지를 이용해 `cpu-scheduler.exe` 파일을 생성한다.

exe 파일은 다른 경로에 놓아도 정상 작동한다.

```shell
env\Scripts\pyinstaller --clean --distpath=. main_gui.spec
```

## Technology Stack

### Python packages

* Python 3.9.5
* PyQt5 5.15 - GUI 프로그래밍
* plotly 5.9.0 - 스케줄링 결과를 간트차트로 시각화
* html2image 2.0.1 - html로 생성한 간트차트를 png 파일로 변환
* Pyinstaller 5.1 - py 파일을 exe 파일로 변환

## Documents

🎙️ [중간 발표자료](https://github.com/jseop-lim/cpu-scheduling-simulator-python/blob/main/docs/ppt.pdf)

📄 [최종 보고서](https://github.com/jseop-lim/cpu-scheduling-simulator-python/blob/main/docs/report.pdf)

## Contributors

* 임정섭([jseop-lim](https://github.com/jseop-lim)): 스케줄러 제작
* 진시윤([JinSY515](https://github.com/JinSY515)): 간트차트 구현, GUI 프로그래밍
* 이영섭([Rhycha](https://github.com/Rhycha)): UI 디자인 및 제작
* 박상호([sangho00](https://github.com/sangho00)): 보고서 및 PPT 작성
