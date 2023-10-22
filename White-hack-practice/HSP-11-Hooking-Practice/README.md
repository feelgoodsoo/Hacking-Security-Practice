# Hooking

### Hooking이란?

- OS나 APP 등 각종 프로그램이 정상적으로 처리하는 메시지, 이벤트, 함수 호출 등을 중간에 바꾸거나 가로채는 기술

### Hook

- 이벤트 메시지 처리 또는 함수 호출을 가로채는 프로그램 코드
- 훌 메커니즘에 따라 soft hook, hard hook으로 구분
- Soft hook : CPU Exception을 발생시킴으로써 OS가 hook handler를 호출하게 함
- Soft hook example - INT3을 hook 설치점에 삽입
- Hard hook : User Routine(hook handler)으로 제어 흐름을 변경하는 명령
- Hard hook example - JMP을 훅 설치점에 hard coding

### Hooking 목적

- 프로세스 모니터링
- 프로세스 은폐
- 디버깅
- 기능 확장

### 실습 내용

- Soft hooking : SSL 도청
- Hard hooking : Heap Monitoring
