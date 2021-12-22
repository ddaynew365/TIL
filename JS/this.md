# ***this***
## 1. this는 JS에서 어떻게 작동하나요
- this는 자바스크립트 런타임 시에 바인딩이 이루어지는 실행 컨텍스트 중 하나로, 해당 함수가 실행되는 동안에 사용할 수 있으며, 함수 호출 부분에서 this가 가리키는 것이 무엇인지를 확인할 수 있다
- 복잡한 코드에서 암시적 바인딩에 의해 혼란스러운 경우가 많은데 이런 문제를 해결하기 위해서 call이나 apply샅은 내장 유틸리티를 사용하여 명시적으로 바인딩해준다.

## 2. this
- this의 값은 함수를 호출한 방법에 의해 결정
- 실행 중에는 할당으로 설정할 수 없으며 함수를 호출할 떄마다 다를 수 있다
- ES5에서는 함수를 어떻게 호출하였는지 상관하지 않고 this 값을 설정할 수 있는 bind 메서드가 도입되었다
- ES2015는 스스로의 this 바인딩을 제공하지 않는 화살표 함수가 추가됨
  - 렉시컬 컨텍스트안의 this 값을 유지
  ### ㄱ.전역문맥
  - 전역 실행맥락에서 this는 전역 객체를 참조
  - 참고로 var은 전역 객체에 등록되지만 let, const는 블록 레벨이기 때문에 등록 x
  - ex 
    ```js
    var a = 100 //전역 객체 window에 a라는 key와 100이라는 value가 추가됨
    console.log(this === window); // true
    
    this.b = "MDN";
    console.log(window.b); // "MDN"
    console.log(b); // "MDN"
    ```
  ### ㄱ2.함수문맥(일반 함수 실행 방식)
  - 함수 내부에서 this의 값은 함수를 호출하는 방법에 의해 좌우
  - strict mode에서 this는 무조건 undefined
  ```js
  // 일반 함수 실행 방식
  function f1(){
    return this;
  }

  // 브라우저
  f1() === window; // true
  // Node.js
  f1() === global; // true

  function f2(){
    "use strict"
    return this;
  }
  
  f2() === undefinded; // true
  ```
  ### ㄴ.함수문맥(DOT NOTATION) = 암시적 바인딩
  - DOT Notation이란 우리가 Object를 만들고 그 Object의 key와 value를 부여한 후 도트(.)로 값에 접근하는 방식
  ```js
  var age = 100;

  var ken = {
    age: 35,
    foo: function () {
      console.log(this.age); 
    }
  }
  ken.foo(); // 35 // Dot Notation 방식
  ```
  - Dot Notation으로 함수가 실행되면, this는 그 도트 앞에 써있는 객체 자체를 가리킨다.
  ### ㄷ.함수문맥(new 키워드) = 생성자 바인딩
  - 함수를 foo()와 같은 형태로 실행시킬수도 있지만, new 키워드를 사용하여 생성자 함수로 만들어 사용할 수 있다. 이 때, this는 빈 객체가 된다
  ```js
  function Person() {
    console.log(this);
  }
  new Person(); // 빈 객체가 return 된다
  ```
  - 위와 같은 경우 this는 빈 객체를 가리키며 생성자 함수는 빈 객체를 return 한다(심지어 return this라는 코드가 없어도 반환한다 -> 생성자 함수의 특징 중 하나)
  
  ```js
  function Foo () {
    console.log(this.age); // undefined
    this.age = 100; // 빈 객체에 속성 추가
    console.log(this.age); // 100
  }

  new Foo(); // {age:100}이라는 객체가 리턴
  ```
  - 생성자 함수는 return 문이 있더라도 return 값이 객체가 아닌 이상 return문을 무시하고 this 객체를 return하는 특징이 있다.
  ```js
  
  function foo () {
    this.age = 100;
    return 3;
  }
  var a = new foo();
  console.log(a); // {age:100}

  
  function foo () {
    this.age = 100;
    return { haha: 23232 };
  }
  var a = new foo();
  console.log(a); // {haha:23232}
  ```
## 3. ㄹ.명백한 바인딩 = 명시적 바인딩
  - 즉 this의 역할을 우리가 직접 명확하게 지정해준다는 의미
  - function.prototype.call, function.prototype.bind, function.prototype.apply와 같은 메소드를 사용하여 할 수 있다.
  ### bind
  - f.bind(somrObject)를 호출하면 f와 같은 본문과 범위를 가졌지만 this는 원본 함수를 가진 새로운 함수를 생성. 새 함수의 this는 호출 방식과 상관없이 영구적으로 bind()의 첫 번째 매개변수로 고정

  ```js
  function f() {
    return this.a;  
  }

  var g = f.bind({a: 'azerty'});
  console.log(g()); // azerty

  var h = g.bind({a: 'yoo'}); // bind는 한 번만 동작함!
  console.log(h()); // azerty

  var o = {a: 37, f: f, g: g, h: h};
  console.log(o.a, o.f(), o.g(), o.h()); // 37, 37, azerty, azerty
  ```

  ### call와 apply
  - this의 값을 한 문맥에서 다른 문맥으로 넘기기 위한 기능
  ```js
  function add(c, d) {
    return this.a + this.b + c + d;
  }

  var o = {a:1 b: 3};
  // 첫 번째 인자는 'this'로 사용할 객체이고,
  // 이어지는 인자들은 함수 호출에서 인수로 전달된다.
  add.call(o, 5, 7); // 16
  // 첫 번째 인자는 'this'로 사용할 객체이고,
  // 두 번째 인자는 함수 호출에서 인수로 사용될 멤버들이 위치한 배열이다.
  add.apply(o,[10, 20]) // 34
  ```

  - 비엄격 모드에서 this로 전달된 값이 객체가 아닌 경우, call과 apply는 이를 객체로 변환하기 위한 시도를 한다
    - null과 undefined 값은 전역 객체가 된다
    - 7이나 'foo'와 같은 원시값은 관련된 생성자를 사용해 객체로 변환 -> new Number(7), new String('foo')

  ```js
  function bar() {
  console.log(Object.prototype.toString.call(this));
  }

  bar.call(7);     // [object Number]
  bar.call('foo'); // [object String]
  bar.call(undefined); // [object global]
  ```

  ## 4. 바인딩의 싸움
  new 바인딩 >= 명시적 바인딩(bind, apply, call) >>>>넘사>>>> 암시적 바인딩(Dot Notation) > 기본 바인딩(전역, 일반 함수)

  ## 5. Arrow Function
  - arrow function이 선언된 부분 스코프의 this context를 this context로 사용(뭔말?)
  - arrow function이 자신을 둘러싼 환경의 this 문맥을 그대로 따르기 때문이다. 9라인에서 간접 실행이 일어나며 this의 문맥이 결정되면, arrow function도 이를 그대로 따르는 것이다. 따라서 arrow function은 실행도중 this의 스코프를 바꾸고 싶지 않을때 유용하다.
  - 자기 scope 내부에서 this가 없기 때문에, 상위 스코프로 스코프 체이닝때문
  ```js
  function objFunction() { 
    console.log('Inside `objFunction`:', this.foo); // 13 
    return { 
      foo: 25,
      bar: () => console.log('Inside `bar`:', this.foo) // 13 
    };
   }
    objFunction.call({foo: 13}).bar();

  ```