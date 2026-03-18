# 📘 백준 11004 - K번째 수 (JavaScript)

## 🔎 문제 핵심

N개의 수가 주어졌을 때  
정렬했을 때 **K번째 수**를 구하는 문제

---

# 🧠 풀이 시도 과정 (시행착오)

## 1️⃣ sort() 사용

```javascript
A.sort((a, b) => a - b);
console.log(A[K - 1]);
```

### 결과
❌ 시간 초과

### 이유

- 전체 배열을 정렬 → **O(N log N)**
- 우리는 K번째 값만 필요한데 불필요한 작업이 많음

---

## 2️⃣ Quick Select 시도

### 아이디어

- pivot 기준으로 분할
- K번째 위치만 찾아가면 됨
- 평균 시간복잡도: **O(N)**

### 결과
❌ 시간 초과 발생

### 원인

- pivot 선택이 좋지 않으면
- 한쪽으로 쏠리면서 **O(N²)** 발생 가능

👉 JavaScript에서는 특히 성능이 불안정

---

## 3️⃣ Heap (우선순위 큐) 사용 ✅

### 핵심 아이디어

- **K개의 가장 작은 값만 유지**
- 그 중 가장 큰 값 = K번째 수

👉 **Max Heap 사용**

---

## 🔧 구현 방법

```javascript
class MaxHeap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  peek() {
    return this.heap[0];
  }

  push(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  pop() {
    if (this.heap.length === 1) return this.heap.pop();

    const max = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return max;
  }

  bubbleUp() {
    let index = this.heap.length - 1;

    while (index > 0) {
      const parent = Math.floor((index - 1) / 2);
      if (this.heap[parent] >= this.heap[index]) break;

      [this.heap[parent], this.heap[index]] = [this.heap[index], this.heap[parent]];
      index = parent;
    }
  }

  bubbleDown() {
    let index = 0;
    const length = this.heap.length;

    while (true) {
      let left = index * 2 + 1;
      let right = index * 2 + 2;
      let largest = index;

      if (left < length && this.heap[left] > this.heap[largest]) {
        largest = left;
      }

      if (right < length && this.heap[right] > this.heap[largest]) {
        largest = right;
      }

      if (largest === index) break;

      [this.heap[index], this.heap[largest]] = [this.heap[largest], this.heap[index]];
      index = largest;
    }
  }
}
```

---

## 🚀 풀이 코드

```javascript
const maxHeap = new MaxHeap();

for (const num of A) {
  if (maxHeap.size() < K) {
    maxHeap.push(num);
  } else if (num < maxHeap.peek()) {
    maxHeap.pop();
    maxHeap.push(num);
  }
}

console.log(maxHeap.peek());
```

---

## ⏱ 시간 복잡도

```txt
O(N log K)
```

- N개의 숫자를 순회
- heap 연산은 log K

---

# 📊 방법 비교

| 방법 | 시간 복잡도 | 특징 |
|------|------------|------|
| sort | O(N log N) | 구현 쉬움, 하지만 비효율 |
| Quick Select | 평균 O(N) | 빠르지만 최악 O(N²) |
| Heap | O(N log K) | 안정적이고 실전에서 많이 사용 |

---

# 💡 핵심 정리

- 이 문제는 단순 정렬 문제가 아니라  
  👉 **선택(Selection) 문제**
- 전체 정렬이 아니라 **K번째 값만 찾는 게 중요**
- JavaScript에서는 Quick Select가 불안정할 수 있음
- 👉 Heap 방식이 안정적인 대안

---

# 🧩 한 줄 요약

```
K개의 최소값만 유지하는 Max Heap으로 K번째 수를 구한다.
```