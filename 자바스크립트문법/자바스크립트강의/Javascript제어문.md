# 1. Javascript 제어문
***

## 학습한 내용

#### 1)  프로그램, 프로그래밍, 프로그래머
- 자바스크립트는 컴퓨터 언어인 동시에 컴퓨터 프로그래밍 언어이다. (HTML은 단순히 컴퓨터 언어)
- 프로그래밍이란 시간의 순서를 만드는 행위이다.

#### 2) 조건문
- 조건문은 c언어나 java와 유사한 모습을 보여주었다.
- 다른 언어와는 달리 print가 없고 console.log()나 document.write()를 사용한다. ( 둘의 차이는 추후에 배울 예정)
  
  ~~~
  if(true){
    console.log(1)
  } else {
    console.log(2)
  }
  ~~~

#### 3) 리팩토링
- 코드를 작성한 후 동작은 그대로, 가독성을 올리고, 유지보수는 편리하게, 중복코드는 줄이는 작업
- 중복을 제거하는 예
    ~~~
    if(this.value === 'night'){
  }
  ~~~
  
#### 4) 배열
- 선언
    ~~~
    var alist = ['1', '2']
    ~~~
- 사용
    ~~~
    document.write(alist[0])
    ~~~
- 개수세기
    ~~~
    document.write(alist.length)
    ~~~
- 원소 추가
    ~~~
    alist.push('3')
    ~~~
- 원소 삭제
    ~~~
    alist.splice('2')
    ~~~

#### 5) 반복문(Loop)
- 마찬가지로 c언어나 java와 유사
- 아래는 리스트로 출력하는 방법이다.
    ~~~
    <ul>
        <li>a</li>
        <li>b</li>
    </ul>
    ~~~
- 결과 
<ul>
    <li>a</li>
    <li>b</li>
</ul>

    
    <ol>
        <li>a</li>
        <li>b</li>
    </ol>
    
- 결과 

<ol>
    <li>a</li>
    <li>b</li>
</ol>