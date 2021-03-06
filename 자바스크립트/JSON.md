# ***JSON***
- JSON은 클라이언트와 서버 간의 HTTP 통신을 위한 텍스트 데이터 포맷
- 자바스크립트에 종속되지 않는 언어 독립형 데이터 포맷으로 대부분의 프로그래밍 언어에서 사용가능

## 1. JSON 표기 방식
- JSON은 자바스크립트의 객체 리터럴과 유사하게 키와 값으로 구성된 순수한 텍스트
- JSON의 키는 반드시 큰따옴표로 묶어야 한다
- 값은 객체 리터럴과 같은 표기법을 그대로 사용 가능
- 하지만 문자열은 반드시 큰따옴표로 묶어야 한다


## 2. JSON.stringify
- 객체를 JSON 포맷의 문자열로 변환
- 클라이언트가 서버로 객체(+배열)를 전송하려면 객체를 문자열화해야하는데 이를 직렬화라고 한다.

## 3. JSON.parse
- JSON 포맷의 문자열을 객체로 변환
- 이를 역직렬화라고 한다.

# ***XMLHttpRequest***
- 자바스크립트를 사용하여 HTTP 요청을 전송하려면 XMLHttpRequest 객체를 사용한다
- WebAPI인 XMLHttpRequest 객체는 HTTP 요청 전송과 HTTP 응답 수신을 위한 다양한 메서드와 프로퍼티를 제공
- 브라우저에서 제공하는 WebAPI이므로 브라우저 환경에서만 정상적으로 실행

