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
## 要求五：SQL JOIN (Optional)
