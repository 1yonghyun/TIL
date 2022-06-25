```
// while문으로 구구단 쓰기
package first;

public class OperationEx {
	public static void main(String[] args) {
		int dan = 2;
		int times = 1;
		
		while(dan <= 9) {
			times = 1;
			while(times <=9) {
				System.out.println(dan + "X" + times + "=" + dan*times);
				times++;
			}
			dan++;
			System.out.println();
		}
		
	}

}

```

for문 예시

```
package first;

public class OperationEx {
	public static void main(String[] args) {
		for(int i =0; i < 10; i++) {
			System.out.println("hello, world");
		}
		
		System.out.println();
		
//		for(int i = 1; i <= 10; i++) {
//			System.out.print("hello, world");
//		}
//		
	}

}
```

continue 문

반복문과 함께 쓰이며, 반복문 내부 continue 문을 만나면 이후 반복되는 부분을 수행하지 않고 조건식이나 증감식을 수행함

break 문

반복문에서 break 문을 만나면 더 이상 반복을 수행하지 않고 반복문을 빠져 나옴

중첩된 반복문 내부에 있는 경우 가장 가까운 반복문 하나만 빠져 나옴 

break예시

```
package first;

public class OperationEx {
	public static void main(String[] args) {
		int sum = 0;
		int num = 1;
		
		while(true) {
			sum += num;
			if(sum > 100)
				break;
			num++;
		}
		
		System.out.println(sum);
		System.out.println(num);
	}

}
```

객체

"의사나 행위가 미치는 대상"

구체적, 추상적 데이터 단위



객체지향 프로그래밍

객체를 기반으로 하는 프로그래밍



클래스(class)

객체에 대한 속성과 기능을 코드로 구현 한 것

"클래스를 정의 한다"라고 함



객체의 속성

객체의 특성, 속성, 멤버 변수



객체의 기능

객체가 하는 기능들을 메서드로 구현



클래스 정의 하기

(접근 제어자) class 클래스 이름{

​	멤버 변수;

​	메서드;

}

class는 대부분 대문자로 시작, 자바의 모든 코든는 class 내부에 위치

