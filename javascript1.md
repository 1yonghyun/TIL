javascript

-변수

문자열(string)은 ''나 ""을 사용한다.

class라는 단어는 변수로 쓸 수 없다. 기존에 있는 class와 겹치기 때문이다

```
name = "Mike";
age = 30;


```



const : 절대로 바뀌지 않는 상수, 수정이 안된다



자바스크립트에서 변수를 선언할때는, 변하지 않는 값은 const, 변할 수 있는 값은 let으로 선언한다.

대부분 const로 선언, 변경 될 수 있는건 let으로 선언한다.



정리

1. 변수는 문자와 숫자, $와 _만 사용

   ```
   const MY_HOME = "...";
   let_ = 1;
   let$ = 3;
   ```



2. 첫글자는 숫자가 될 수 없다

3. 예약어는 사용할 수 없다.

   ```
   let let = 99;
   ```

4. 가급적 상수는 대문자로 알려준다.

   ```
   const MAX_SIZE = 99;
   ```

5. 변수명은 읽기 쉽고 이해할 수 있게 선언

   ```
   let a = 1; X
   let userNumber = 3;
   ```

   

사용자와 상호대화 할 수 있는 대화상자

alert, prompt, confirm

단점: 

1. 스크립트 일시 정지
2. 스타일링이 불가능하다.



-형변환

String() -> 문자형으로 변환

Number() -> 숫자형으로 변환

​						Number("문자") 로 입력하면 NaN이 반환된다

Boolean() -> 불린형으로 변환

​					0, '', null, undefined, NaN은 false가 반환된다.



prompt 입력 -> 문자형

"9080" / 2 = 4540

"6" / "2" = 3

같은 식으로 자동 형변환이 일어난다.

의도를 가지고 원하는 타입으로 형변환을 시키는 것을 명시적 형변환이라고 한다.



-명시적 형변환

String()

String(3) => "3"

String(true) => "true"



Number()

Number("1234") => 1234

Number("1234a") => NaN

Number(true) => 1

Number(false) => 0



Boolean()

false

- 숫자 0
- 빈 문자열''
- null
- undefined
- NaN

이 외에는 true가 된다.



주의사항

Number(null) => 0

Number(undefined) => NaN



Boolean(0) => false

Boolean('0') => true



Booelan('') => false

Boolean(' ') => true