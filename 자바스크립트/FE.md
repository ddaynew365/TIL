## 일급 합수

- 함수는 그저 하나의 '값' 이다. 따라서 다른 값과 같이 사용할 수 있다.
- 대표적으로, 함수는 인자로 쓰일 수 있고, 반환될 수 있다.

```jsx
function foo(fn) {
    const val = 10;
    return fn(val);
}

foo( (value) => {
    return value * 10;
}) 
//100
```

- 또한 배열의 원소나, 객체의 속성으로 사용할 수 있음은 물론이다.

## Closure

- 클로저는 함수 자신이 포함하는 스코프의 변수들을 추적하는 함수이다.
- 우리가 변수에 접근하려면, 함수의 실행이 종료되기 전이어야 한다.
- 자바스크립트에서 특이한 부분은 함수의 실행이 끝나고 나서 접근이 가능한 경우가 있다는 것이다.

## var과 let의 차이

var은 함수 레벨 스코프를 지원하며 let은 블록 레벨 스코프를 지원하다(const도 블록레벨 스코프)

```jsx
function foo() {
    if (true) {
        var color = 'blue';
    }
    console.log(color); // blue
}
foo();
```

```jsx
function foo() {
    if(true) {
        let color = 'blue';
        console.log(color); // blue
    }
    console.log(color); // ReferenceError: color is not defined
}
foo();
```

## closure의 장점 활용

```jsx
function sum(a,b) {
    return a+b;
}

function divide(a,b) {
    return a/b;
}

function calculate(fn, prev) {
    return function(next){
        return fn(prev, next)
    }
}

const sum100 = calculate(sum, 100)
const divide100 = calculate(divide, 100)
console.log(sum100(20));  //120
console.log(divide100(20)); //5
// 이렇게 인자를 줄여 가벼운 함수를 만들어낼 수 있다.
// calculate 함수를 curryed 함수, 이 방식을 currying이라고 한다
```

## curry 함수 예시

```jsx
curry = f => a => b => f(a, b)
```

```jsx
let curry = (fn) => { 
    return function curryFn(...args1) {
        if (args1.length >= fn.length) { // 여기서 fn.length는 fn이라는 함수의 인자 개수를 의미
            return fn(...args1);
        } else {
            return (...args2) => curryFn(...args1, ...args2);
        }
    }
}

function multiply(a, b, c){
    return a * b * c;
}

let curriedMultiply = curry(multiply);
let result = curriedMultiply(2,3)(4);
```
