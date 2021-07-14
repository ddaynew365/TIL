# 1. 웹과 자바스크립트
***

## 학습한 내용

#### 1)  HTML과 JS의 만남 : script 태그
- ~~~
  <script> </script> 
  ~~~ 
  => html위에서 javascript를 코드를 작성하겠다는 태그
- ~~~
  <input>
  ~~~
  => 어떠한 기능을 가지는 도구를 추가하겠다는 태그

#### 2)  HTML과 JS의 만남 : 이벤트
- 자바스크립트의 동적인 움직임을 파악하기 위함
    - 예시
        ~~~
          onclick='' => 클릭하면 이벤트 발생
          
          onchange='' => 값이 변화하면 이벤트 발생
          
          onkeydown='' => 어떤 키를 누르면 이벤트 발생
        ~~~
#### 3) 데이터 타입(문자열과 숫자)
- 데이터타입은 다른 언어와 크게 다른 점이 없었고 특히, 문자열은 파이썬과 유사한 모습을 보여주었다.
    - 문자열(string)
    - 숫자
     ~~~
      1+1 = 2
      '1'+'1'='11'
     ~~~
  
#### 4) 변수와 대입연산자
- 추후에 깊게 배우겠으나 현재는 변수 앞에 var이라는 자료형을 쓰는 것으로 충분하다.

#### 5) CSS 기초(style 속성, 태그 / 선택자)
- CSS 언어는 디자인을 위한 언어로 HTML과 Javascript 언어와 자주 같이 사용된다.
- 자바스크립트에서 'script' 태그를 사용하듯이 CSS에서는 'style' 태그를 사용한다.
- 무색 무취 태그
    - div라는 태그는 화면 전체를 사용하는 무색무취의 태그로서 줄 바꿈이 적용된다.
        ~~~
        <div></div>
        ~~~
    - 줄 바꿈을 하지 않으려면 똑같은 특징의 span 태그를 사용하면 된다.
        ~~~
       <span></span>
        ~~~
    
- 선택자
    - CSS는 선택자라는 중요한 요소가 존재한다
        - 태그, 클래스(class), 아이디(id) 순으로 갈수록 좀 더 구체적인 적용 범위를 가지고 있다.   따라서 
  위 3개의 특징을 가지고 있는 데이터는 id, class, 태그 순으로 적용 우선순위를 가진다. 

## 실습

- 아래 코드는 위에서 배운 내용들을 사용하여 내 나름대로 여러 실험을 한 html 코드다. 
  ~~~
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>
                    환영합니다
                </title>
                <style>
                    span{
                        font-weight: bold;
                        background-color:black;
                        color:white;
                    }
                    .js{
                        background-color:yellow;
                        }
                    #js{
                        background-color:red;
                        }
                </style>
            </head>
            <body>
                <h1>hello javascript</h1>
                <h2 style="background-color:coral;color:powerblue">JavaScript</h2>
                <span>태그</span>
                <span class="js">태그, 클래스</span>
                <span id ="js" class="js">태그, 클래스, 아이디</span>
                <input type="button" value="hi" onclick="alert('hi')">
                <input type="text" onchange="alert('changed')">
                <input type="text" onkeydown="alert('key down!')">
            </body>
        </html>
  ~~~
- 결과
![image](https://user-images.githubusercontent.com/64246267/125613725-003a39e1-5fb8-433f-89fb-2e9f5df697a1.png)
