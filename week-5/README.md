## 要求三：CRUD
+ #### 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。  
  ```mysql
  INSERT INTO member(name, username, password) VALUES("Admin", "test", "test");
  INSERT INTO member(name, username, password) VALUES("Mike Portnoy", "DreamTheater1985", "DanceOfEternity");
  INSERT INTO member(name, username, password) VALUES("Kurt Cobain", "Nirvana1987", "ComeAsYouAre");
  INSERT INTO member(name, username, password) VALUES("Tatiana Shmailyuk", "Jinjer2008", "ISpeakAstronomy");
  INSERT INTO member(name, username, password) VALUES("Till Lindemann", "Rammstein1994", "DuHast");
  ```
  ![image](https://user-images.githubusercontent.com/107986642/196201336-7b9453c5-2169-49a7-af0d-1d419973c4eb.png)
  
+ #### 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
  ```mysql
  SELECT * FROM member;
  ```
  ![image](https://user-images.githubusercontent.com/107986642/196210528-23ffadca-9973-4b67-a220-7248538634f8.png)
+ #### 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
  ```mysql
  SELECT * FROM member ORDER BY time DESC;
  ```
  ![image](https://user-images.githubusercontent.com/107986642/196228532-d2ea23c4-516a-45ae-bd47-24aed1dca88e.png)

+ #### 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
  ```mysql
  SELECT * FROM member ORDER BY time DESC LIMIT 1,3;
  ```
  ![image](https://user-images.githubusercontent.com/107986642/196248796-cdf0768b-dc85-4407-b7b6-428085ed8d02.png)

+ #### 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
  ```mysql
  SELECT * FROM member WHERE username = "test";
  ```
  ![image](https://user-images.githubusercontent.com/107986642/196253190-75418b16-3883-44ed-b9eb-d1fd01a36be2.png)

+ #### 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
  ```mysql
  SELECT * FROM member WHERE username = "test" AND password = "test";
  ```
  ![image](https://user-images.githubusercontent.com/107986642/196253708-d63c795e-2d1e-41dc-aab8-caa87ca3279a.png)

+ #### 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
  ```mysql
  UPDATE member SET name = "test2" WHERE username = "test";
  ```
  ![image](https://user-images.githubusercontent.com/107986642/196255749-f9a50d6e-b003-4190-b468-8ebe62a5d641.png)

## 要求四：SQL Aggregate Functions
___
### :cookie:後來又新增了幾筆資料並更新追蹤人數
![image](https://user-images.githubusercontent.com/107986642/196415847-b7568e04-c12d-4681-a23b-7dc225bc65c2.png)

___
+ #### 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
  ```mysql
  SELECT COUNT(*) FROM member;
  ```
  ![image](https://user-images.githubusercontent.com/107986642/196421030-115c570b-adc1-4c97-afc3-4e2d41cdd887.png)


+ #### 取得 member 資料表中，所有會員 follower_count 欄位的總和。
  ```mysql
  SELECT SUM(follower_count) FROM member;
  ```
  ![image](https://user-images.githubusercontent.com/107986642/196419927-27d3be2e-1086-45b2-a88d-69c7bf1c695d.png)

+ #### 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
  ```mysql
  SELECT AVG(follower_count) FROM member;
  ```
  ![image](https://user-images.githubusercontent.com/107986642/196420729-29fe56f8-0317-451c-9222-93f5fcab76a3.png)

## 要求五：SQL JOIN (Optional)
```mysql
CREATE TABLE message(
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  member_id BIGINT NOT NULL,
  content VARCHAR(255) NOT NULL,
  like_count INT UNSIGNED NOT NULL DEFAULT 0,
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(member_id) REFERENCES member(id)
);
```
![image](https://user-images.githubusercontent.com/107986642/196427662-a6de7982-e1f4-41b8-8494-50ad10fff692.png)
