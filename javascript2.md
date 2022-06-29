-논리 연산자

|| (OR)

&& (AND)

! (NOT)



-switch

if문과 동일하지만 케이스가 다양할 경우 보다 간결하게 쓸 수 있다는 장점이 있다.

```
switch(평가){

	case A:
	// A일떄 코드
	case B:
	// B일때 코드
	...
}

if(평가 == A){
	//A일때 코드
}else if(평가 == B){
	//B일때 코드
}
```

break를 넣지 않으면 이후에 있는 코드를 모두 실행한다.

case 대신에 default를 입력하면 기본값을 설정할 수 있다.

바로 밑의 조건과 같은 값이라면 빈칸으로 적으면 된다.

```
switch(fruit){
	case '멜론' :
	case '수박' :
		console.log('500원 입니다.');
		break;
	default :
		console.log('그런 과일은 없습니다.');
}
```



-함수

장점 : 편리함, 유지보수가 쉽다

함수가 바뀔 가능성이 있다면 let을 이용해서 수정할 수 있다.

```
function sayHello(name){
	let msg = `Hello`;
	if(name){
		msg = `Hello, ${name}`;
	}
	console.log(msg);
}
다음과 같이 써도 동일하다

function sayHello(name){
	let msg = `Hello`;
	if(name){
		msg += ', 'name;
	}
	console.log(msg);
}

function sayHello(name){
	let msg = `Hello`;
	if(name){
		msg += `, ${name}`;
	}
	console.log(msg);
}
```



OR를 사용한 경우 매개변수를 입력하지 않으면 다른 값이 나오게 만들 수 있다.

```
function sayHello(name){
	let newName = name || 'friend';
	let msg = `Hello, ${newName}`
	console.log(msg)
}

sayHello();
라고 입력한다면 
"Hello, friend"
라는 값이 나온다.

sayHello('Jane');
이라고 입력한다면
"Hello, Jane"
이라는 값이 나온다.
```

default 값을 설정하는 방법도 있다.

```
function sayHello(name = 'friend'){
	let msg = `Hello, ${name}`
	console.log(msg)
}

sayHello();
라고 입력한다면 
"Hello, friend"
라는 값이 나온다.

sayHello('Jane');
이라고 입력한다면
"Hello, Jane"
이라는 값이 나온다.
```



return 으로 값 반환

```
function add(num1, num2){
	return num1 + num2;
}
이런식으로 쓰면된다


return이 없거나 return뒤에 아무것도 안쓰면 undefined가 반환된다. 
return을 입력하면 함수가 반환되고 종료된다.
function showError(){
	alert('에러가 발생했습니다.');
}
const result = showError();
console.log(result);
```

-함수 사용 tip

	- 한번에 한작업에 집중
	- 읽기 쉽고 어떤 동작인지 알 수 있게 네이밍





