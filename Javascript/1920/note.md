# 📘 백준 1920 - 수 찾기 (JavaScript)

## 1. `in` 방식이 동작하지 않았던 이유

처음에는 다음과 같이 작성했다.

```javascript
if (MInputArr[index] in NInputArr) {
  console.log(1);
} else {
  console.log(0);
}
```

하지만 `in` 연산자는 **값(value)** 이 아니라 **key(인덱스)** 존재 여부를 확인한다.

예시

```javascript
const arr = [3, 5, 7];

console.log(0 in arr); // true
console.log(1 in arr); // true
console.log(3 in arr); // false
```

즉 `"1" in arr` 은 **arr[1]이 존재하는지** 확인하는 것이다.  
따라서 **배열 안에 특정 값이 있는지 확인하는 용도로는 사용할 수 없다.**

### 1-1. 중첩 for문

위와 같은 문제로 인해 제출에 실패하고 중첩 for문을 이용해서 해결해 보았지만,

시간 초과로 실패했다.

---

## 2. `includes()` 방식

배열에 특정 값이 존재하는지 확인하려면 `includes()`를 사용할 수 있다.

```javascript
for (let i = 0; i < M; i++) {
  console.log(NInputArr.includes(MInputArr[i]) ? 1 : 0);
}
```

### 특징

- 배열을 **처음부터 끝까지 탐색**
- 시간 복잡도: **O(N × M)**

입력이 커지면 **시간 초과가 발생할 수 있다.**

---

## 3. `Set` 방식 (권장)

```javascript
const set = new Set(NInputArr);

for (let i = 0; i < M; i++) {
  console.log(set.has(MInputArr[i]) ? 1 : 0);
}
```

### 특징

- `Set`은 **해시 기반 자료구조**
- 값 존재 여부 확인이 매우 빠름

시간 복잡도

```
O(N + M)
```

---

## 4. `includes` vs `Set`

| 방법 | 시간 복잡도 | 특징 |
|-----|-------------|------|
| includes | O(N × M) | 배열을 매번 탐색 |
| Set | O(N + M) | 해시 탐색으로 빠름 |

✔ **결론**

이 문제에서는

```
Set + has()
```

방식이 가장 효율적인 해결 방법이다.