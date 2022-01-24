# HTML & JS

## 1. HTML 문서 구조

- HTML은 계층적 → 브라우저는 HTML 정보를 tree 구조로 보관(DOM Tree)
- <!DOCTYPE>: 마크업 언어용 DTD 태그
- <html>: 위의 DTD를 제외한 HTML 문서는 html이라는 태그로 시작해서 html 태그로 끝난다
- <head>: html 문서의 meta정보
- <body>: 화면에 보여지기 위한 정보. HTML 5 이전에는 body안에 6가지의 속성이 있었지만 이 역할을 CSS가 대체하게 되면서 HTML5에서부터는 지원하지 않게 되었다.
- <title>: HTML의 제목을 선언하는 태그
- <meta>: HTML의 부가 정보를 선언하는 태그
- <link>: 별도의 CSS 선언 파일등을 연결하는 태그

## 2. 텍스트 관련 태그

- <hgroup>: 제목 태그(<h1>~<h6>)을 그룹으로 묶기 위한 태그. 하지만 현재 브라우저 상에서는 아무런 역할 없이 div와 비슷하게 동작하고 있으며 W3C에서는 <header>태그로 대체할 것을 권장
- <p></p>: 문단을 묶어주는 태그
- <b>: 두껍게 효과
- <i>: 기울임꼴
- <string>: 강하게 강조
- <em> : 약하게 강조
- <ins>: 밑줄
- <del>: 취소선
- <s>: del보다 약한 취소선
- <u>: <ins>와 구별되게 철자 오류를 지적하는 밑줄
- <sup>: 위첨자
- <sub>: 아래첨자
- <br>: 줄바꿈
- <hr>: 가로선

## 3. 목록 관련 태그

- <ul>: 순서가 없는 목록
- <ol>: 순서가 있는 목록
- <li>: 목록의 각 항목들을 표시 → <li></li>사이에 목록을 또 넣으면 하위 목록도 가능(<ol>,<ul>사이도 가능)
- <dl> : 한 문장 혹은 단어의 정의나 설명 목록을 표현하고 싶을 때 사용

## 4. 이번에 공부한 태그

![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled.png)

- <a>: anchor로 웹 페이지나 외부 사이트 연결. 링크로 사용할 텍스나 이미지를 <a>로 묶고 href 속성을 이용하여 연결할 웹 페이지의 이름이나 웹 사이트 주소를 지정한다.
    
    ![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled%201.png)
    
    (출처: [https://pridiot.tistory.com/6](https://pridiot.tistory.com/6))
    
    - <button> vs <a>
        - 사용자의 특정한 액션이 필요할 때는 button 태그(로그인 같은), 어딘가로 이동할 때는 a태그
- <div>: 박스 또는 레이어. <table> 태그 대신 자주 사용되고 있다 → 컨텐츠들을 어떤 목적에 따라 묶어야 할 때 사용
- <span>: <div>의 인라인 버전
- (div와 span의 차이: div는 줄 바꿈이 존재하고 span은 줄 바꿈이 존재하지 않는다)
- <header>: 원래는 <hgroup>태그가 사용되었지만 W3C에서 <header>태그로 대체할 것을 권장 → 제목 지정, 문서에서 여러 번 사용 가능 → 소개 및 탐색에 도움을 주는 콘텐츠를 나타냄.제목, 로고, 검색 폼, 작성자 이름 등의 요소도 포함할 수 있음
    - 예시 코드 (출처:[https://developer.mozilla.org/ko/docs/Web/HTML/Element/header](https://developer.mozilla.org/ko/docs/Web/HTML/Element/header))
    
    ```xml
    // html
    <header class="page-header">
        <h1>Cute Puppies Express!</h1>
    </header>
    
    <main>
        <p>I love beagles <em>so</em> much! Like, really, a lot. They’re adorable and their ears are so, so snuggly soft!</p>
    </main>
    
    // CSS
    header.page-header {
        background: no-repeat left/cover url(/media/examples/puppy-header-logo.jpg);
        display: flex;
        height: 120px;
        min-width: 120px;
        align-items: center;
        color: #fff;
        text-shadow: #000 0 0 .2em;
    }
    
    header.page-header > h1 {
        font: bold calc(1em + 2 * (100vw - 120px) / 100) 'Dancing Script', cursive,
            fantasy;
        margin: 2%;
    }
    
    main {
        font: 1rem 'Fira Sans', sans-serif;
    }
    ```
    
    - 결과물
        
        ![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled%202.png)
        
- <nav>: 문서 연결 링크. 같은 사이트 안의 페이지나 다른 사이트의 페이지로 연결하는 링크를 말한다. 위치에 영향을 받지 않기 때문에 <header>나 <footer>, <aside>에 포함시키거나 따로 사용할 수 있다. → 메뉴, 목차, 색인에 자주 사용
    - 예시 코드
    
    ```xml
    // HTML
    <nav class="crumbs">
        <ol>
            <li class="crumb"><a href="#">Bikes</a></li>
            <li class="crumb"><a href="#">BMX</a></li>
            <li class="crumb">Jump Bike 3000</li>
        </ol>
    </nav>
    
    <h1>Jump Bike 3000</h1>
    <p>This BMX bike is a solid step into the pro world. It looks as legit as it rides and is built to polish your skills.</p>
    // CSS
    nav {
        border-bottom: 1px solid black;
    }
    
    .crumbs ol {
        list-style-type: none;
        padding-left: 0;
    }
    
    .crumb {
        display: inline-block;
    }
    
    .crumb a::after {
        display: inline-block;
        color: #000;
        content: '>';
        font-size: 80%;
        font-weight: bold;
        padding: 0 3px;
    }
    ```
    
    - 결과
    
    ![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled%203.png)
    
- <footer>: 제작 정보와 저작권 정보 → 구획의 작성자, 저작권 정보, 관련 문서 등의 내용을 포함
    - 예시 코드
    
    ```xml
    // HTML
    <article>
        <h1>How to be a wizard</h1>
        <ol>
            <li>Grow a long, majestic beard.</li>
            <li>Wear a tall, pointed hat.</li>
            <li>Have I mentioned the beard?</li>
        </ol>
        <footer>
            <p>© 2018 Gandalf</p>
        </footer>
    </article>
    
    // CSS
    article {
        min-height: 100%;
        display: grid;
        grid-template-rows: auto 1fr auto;
    }
    
    footer {
        display: flex;
        justify-content: center;
        padding: 5px;
        background-color: #45a1ff;
        color: #fff;
    }
    ```
    
    - 결과
    
    ![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled%204.png)
    
- <aside>: 본문 이외의 내용. 블로그 양 옆의 광고나 링크 같은 사이드 바를 표시할 때 사용. 필수 요소가 아니기 때문에 필요한 경우에만 사용
    - 예시 코드
    
    ```xml
    // HTML
    <p>Salamanders are a group of amphibians with a lizard-like appearance, including short legs and a tail in both larval and adult forms.</p>
    
    <aside>
        <p>The Rough-skinned Newt defends itself with a deadly neurotoxin.</p>
    </aside>
    
    <p>Several species of salamander inhabit the temperate rainforest of the Pacific Northwest, including the Ensatina, the Northwestern Salamander and the Rough-skinned Newt. Most salamanders are nocturnal, and hunt for insects, worms and other small creatures.</p>
    
    // CSS
    aside {
        width: 40%;
        padding-left: .5rem;
        margin-left: .5rem;
        float: right;
        box-shadow: inset 5px 0 5px -5px #29627e;
        font-style: italic;
        color: #29627e;
    }
    
    aside > p {
        margin: .5rem;
    }
    
    p {
        font-family: 'Fira Sans', sans-serif;
    }
    ```
    
    - 결과
    
    ![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled%205.png)
    
- <section>: 맥락에 따라 주제별로 컨텐츠를 묶을 때 사용. <section>은 header와 section, footer를 구분하기 위한 기능으로 사용(?)
    - 예시 코드
    
    ```xml
    // HTML
    <h1>Choosing an Apple</h1>
    <section>
        <h2>Introduction</h2>
        <p>This document provides a guide to help with the important task of choosing the correct Apple.</p>
    </section>
    
    <section>
        <h2>Criteria</h2>
        <p>There are many different criteria to be considered when choosing an Apple — size, color, firmness, sweetness, tartness...</p>
    </section>
    
    // CSS
    hgroup > h1, h2 {
        margin: 0;
    }
    ```
    
    - 결과
    
    ![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled%206.png)
    

## 5. 주석

```xml
<!-- 주석 내용-->

<!-- 주석
주석
주석
내용
-->
```

## 6. script 태그는 어디에 위치하는게 좋을까?

### SCRIPT 파일은 서로 이어질 수 있다(하지만 선언 순서는 지켜야 한다)

### 브라우저의 동작 방식

1. HTML을 읽기 시작한다.
2. HTML을 파싱
3. DOM 트리 생성
4. Render 트리 생성
5. Display에 표시

- 여기서 HTML을 태그들을 읽어나가는 도중 <script> 태그를 만나면 파싱을 중단하고 javascript 파일을 로드 후 javascript 코드를 파싱. 그 후 다시 HTML 파싱
    - 여기서 두 가지 문제가 발생
        1. HTML을 읽는 과정에 <script>를 만나면 중단 시점이 생기고 그만큼 Display에 표시되는 것이 지연
        2. DOM 트리가 생성되기 전에 자바스크립트가 생성되지도 않은 DOM의 조작을 시도할 수 있음
    
    ![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled%207.png)
    

### ***결론***

- <script> 태그는 body 태그의 최하단이 가장 좋다.

### 만약 피치 못할 사정으로 script 태그를 body 태그 최하단에 놓을 수 없는 상황이라면?

- async와 defer 속성을 사용하면 된다 ⇒ script 태그를 만나도 HTML 파싱이 멈추지 않고 HTML 파싱과 script로드가 동시에 이루어지다가 script로드가 끝나면 script가 실행되는 시점에 HTML 파싱이 잠시 중단되고 실행이 끝나면 HTML 파싱이 재개

![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled%208.png)

```css
<script async src="script.js">
```

- defer 속성을 사용하면 script로드가 끝나도 바로 script가 실행이 되지않고 HTML 파싱이 모두 이뤄진 이후에 script가 실행된다.

![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled%209.png)

```css
<script defer src="script.js">
```

## 7. style 태그는 어디에 위치하는게 좋을까?

- style 태그가 가장 하단에 위치한다면 HTML을 위에서부터 순서대로 파싱하면서 나온 결과가 style 태그의 CSS가 적용되지 않은 상태로 Display 되었다가 style 태그를 파싱한 후에 CSS가 적용될 것이기 때문에 HTML 상단에 정의하는 것이 좋다. 당연 이게 더 성능이 좋다
- 물론 이렇게 사용하면 html을 먼저 다 실행한 후 자바스크립트 코드가 실행되어 에러가 풀리긴한다(그냥 뒤에 놓는게 맘 편하지 않을까?)

```bash
<script>
window.onload =function(){
	자바스크립트 코드
}
</script>
```

## 8. form 태그

- 사용자로부터 입력받은 데이터를 서버에 전송하는데 사용하는 태그
- 보통 input 태그를 사용하여 데이터를 입력받고 전송
- form 태그의 action 속성으로 데이터를 보낼 서버를 선택할 수 있다.
- 이 때 form 태그의 method 속성으로 get, post 둘 중 하나의 방식으로 전송할 수 있다 ( 편법으로 다른 http  메소드 요청 방식을 사용할 수 있다)
    - get 방식은 url을 통해서 데이터 전송, post 방식은 url이 아닌 데이터를 숨겨서 데이터 전송(간단하게 설명)

```bash
<form action='http://localhost:3000'>
	<input type='text' name='id'>
	<input type='text' name='id'>
	<input type='text' name='id'>
</form>
```

## 9. HTML와 javascript

- input 태그의 onclick 속성의 값은 자바스크립트
- onchange, onkeydown 등등이 더 있다 → 이벤트들을 찾아봐라
- 그러나 html안에 제어를 담당하는 자바스크립트가 있다고 유지보수가 쉽지 않다. 또한 html은 정보를 담당하기 때문에 다른 문제가 있다
- 따라서 script 코드를 사용하는 것이 현대적으로 많이 사용된다
- script 태그 사용 예시

![Untitled 1](https://user-images.githubusercontent.com/64246267/138597298-1a9b68eb-5b27-4b1f-89a7-a8eb457ac88e.png)

- 좀 더 엄격하게 자바스크립트 코드를 분리하는 방법 - 외부 파일 분리

## 10. getElmentById('아이디이름')

- 이것도 하나만(애초에 아이디는 하나여야만 한다)

![Untitled 2](https://user-images.githubusercontent.com/64246267/138597307-4e0aa88f-e41a-4f68-8661-7e4ec172b3ad.png)

## 11. querySelector('')

- element들의 객체를 찾아서 return 해준다.(하나만. 여러개 다 가져오려면 All을 붙인다.)

![Untitled](HTML%20&%20JS%2093a6bb4211ac472ca018b3f7b5f3696d/Untitled%2012.png)

### 12. canvas 태그

선을 그리는 방법은 beginPath로 Path의 시작을 알리고 moveTo로 시작 지점으로 이동한 다음, lineTo 등으로 선을 계속 이어가다가 마지막으로 stroke함수를 호출함으로써 선 그리기를 종료하게 되는 형태이다. 

```jsx
const canvas = document.querySelector('.statistics_pie_chart');
const ctx = canvas.getContext('2d');

ctx.beginPath(); // 그리기 시작
ctx.moveTo(0,100); // 시작점 이동
ctx.lineTo(300,100); / 리/ 그리기
ctx.rect(0,0,300,200);
ctx.stroke();
ctx.closePath();
```

### 13. insertAdjacentHTML()

해당 태그, 아이디, 클래스에 HTML을 집어 넣는 메소드

첫번쨰 인자는 위치, 두번째 인자는 HTML

- 첫 번째 인자
    
    ```
    <!--beforebegin -->
    <p>
    <!--afterbegin -->
    foo
    <!--beforeend -->
    </p>
    <!--afterend -->
    ```
    
    **`'beforebegin'`**
    
    element 앞에(형제 앞)
    
    **`'afterbegin'`**
    
    element 안에 가장 첫번째 child(자식 맨첨)
    
    **`'beforeend'`**
    
    element 안에 가장 마지막 child(자식 맨뒤)
    
    **`'afterend'`**
    
    element 뒤에(형제 뒤)
    
- 두 번째 인자는 html 형태로 적는다

```jsx
// <div id="one">one</div>
var d1 = document.getElementById('one');
d1.insertAdjacentHTML('afterend', '<div id="two">two</div>');

// At this point, the new structure is:
// <div id="one">one</div><div id="two">two</div>
```

### 14. JS에서 InsertAdjacentHTML 외에 html에 코드 넣는 법

```html
// 기존 HTML
h1>오늘의 할 일</h1>
<ul class="itemList">
	<li>
		<input type="checkbox" id="item1">
		<label for="item1">이벤트 버블링 학습</label>
	</li>
	<li>
		<input type="checkbox" id="item2">
		<label for="item2">이벤트 캡쳐 학습</label>
	</li>
</ul>
```

```jsx
// 새 리스트 아이템을 추가하는 코드
var itemList = document.querySelector('.itemList');

var li = document.createElement('li');
var input = document.createElement('input');
var label = document.createElement('label');
var labelText = document.createTextNode('이벤트 위임 학습');

input.setAttribute('type', 'checkbox');
input.setAttribute('id', 'item3');
label.setAttribute('for', 'item3');
label.appendChild(labelText);
li.appendChild(input);
li.appendChild(label);
itemList.appendChild(li);
```

## 15. Element().closest()

- 지정된 엘리먼트의 가장 가까운 조상을 반환
- 조상이 없다면 null을 반환
