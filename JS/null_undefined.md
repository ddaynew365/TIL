# null과 undefined의 차이는?
- 두 타입 모두 값이 없음을 의미
- 둘 다 데이터 타입이자 그 변수의 값
- JS에서 변수를 선언하면 초기값으로 undefined를 할당 -> 타입을 확인해보면 'undefined'
- null은 값이 비어있음을 나타내며 값이 없다는 값이 등록되어 있다. -> 타입을 확인해보면 'object'
  - 즉, null은 변수를 선언하고 의도를 갖고 빈 값을 할당한 상태, undefined는 변수를 선언하고 값을 할당하지 않은 상태

> - undefined == null은 true
> - undefined === null은 false
> 이 둘을 이용하여 에러처리할 때, 변수 == null(or undefined)를 사용하면 코드가 간단해진다

## undefined가 나오는 경우의 예시
1. 존재하지 않는 객체의 프로퍼티를 읽으려고 할 떄
2. 존재하지 않는 배열의 element를 읽으려고 할 떄