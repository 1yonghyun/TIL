-익명 함수

(function (){

​	i = 0;

​	while(i < 10) {

​		document.write(i);

​		i += 1;

​	}

})();



-push

인자로 전달된 값을 배열의 끝에 추가하는 명령이다.

ex) li.push('f')



-concat

복수의 원소를 배열에 추가하는 방법이다.

 ex) li.concat(['f', 'g'])



-unshift

배열의 시작점에 원소를 추가하는 방법이다.

ex) li.unshift('z')



-splice

첫번째 인자(인덱스)에 해당하는 원소부터 두번째 원소의 숫자만큼의 값을 배열로부터 제거한더. 세번째 인자에 있는 인자들을 첫번째 인자의 원소 뒤에 추가한다.

ex) li.splice(2, 0, 'B')는 li의 2번 인덱스에 있는 값부터 0개의 값을 제거하고 2번 인덱스에 'B'를 추가한다.



-shift

배열의 첫번째 원소를 제거한다.



-pop

배열 끝점의 원소를 제거한다.



-sort

순서대로 정렬하는 방법이다.



-reverse

역순으로 정렬하는 방법이다.



인덱스를 문자로 사용하고 싶다면 객체(dictionary)를 사용해야 한다.



객체를 만드는 법

예시

```
var grades = {'egoing': 10, 'k8805': 6, 'sorialgi': 80};

var grades = {};
grades['egoing'] = 10;
grades['k8805'] = 6;
grades['sorialgi'] = 80;

var grades = new Object();
grades['egoing'] = 10;
grades['k8805'] = 6;
grades['sorialgi'] = 80;

var grades = {'egoing': 10, 'k8805': 6, 'sorialgi': 80};
alert(grades['sorialgi']);

alert(grades.sorialgi);
```



for in 문 예시

```
var grades = {'egoing': 10, 'k8805': 6, 'sorialgi': 80};
for(key in grades) {
    document.write("key : "+key+" value : "+grades[key]+"<br />");
    
결과:
key :   egoing value : 10
key :   k8805 value : 6
key :   sorialgi value : 80
```



-모듈

로직을 파일로 저장하여 다른 파일에서 동일한 로직을 사용하는 것을 뜻한다.

모듈화가 된다면 유지보수도 쉽고 코드도 더 짧아진다.

ex)

```
function welcome(){
    return 'Hello world';
}
```

위 파일을 greeting.js라고 저장한다면

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <script src="greeting.js"></script>
</head>
<body>
    <script>
        alert(welcome());
    </script>
</body>
</html>
```

라고 script안에 src를 작성하면 모듈을 사용할 수 있다.



