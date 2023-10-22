# Fuzzing

### Fuzzing이란?

- 소프트웨어 테스트 기법으로서, 컴퓨터 프로그램에 유효한, 예상치 않은 또는 무작위 데이터를 입력하는 것

### 실습 내용

- file_fuzzer.py를 참고 및 응용하여 fuzzer를 구현하고 Software의 버그를 찾는다

### file_fuzzer.py 기능

- fuzzing 실행
- 취약점 정보 기록
- fuzzing 파일 생성

### fuzzing 실행

- target Appliaction program을 실행하고 기본 디버거 thread에 접속
- EXCEPTION_ACCESS_VIOLATION handler 설치
- Debugger Monitoring Thread 시작

### 취약점 정보 기록

- 타겟 APP에서 발생한 메모리 액세스 위반 정보를 기록하고 파일로 저장
- fuzzing에 영향 받지 않은 타겟 프로세스 종료

### fuzzing 파일 생성

- 테스트 케이스 요소를 반복하여 테스트 케이스 패턴을 생성함
- 테스트 케이스 패턴을 퍼즈파일의 원본에 합성하여 퍼즈파일을 작성함

### 메모리 액세스 위반 버그 종류

- Buffer overflow(Stack overflow, Heap overflow)
- Integer overflow
- Format String overflow
