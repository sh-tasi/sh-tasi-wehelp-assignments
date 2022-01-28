要求三
=============
>3-1 新增數筆資料進入SQL
>--- 
>語法 :INSERT INTO 資料表(項目)VALUES(資料內容)
>```MYSQL
>INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ("使用者","test","test",10);
>INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ("majiko","oiol1122","ogkbor5",54213);
>INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ("likinpark","ckao562","asoqq99326q",545641);
>INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ("ivy","wulia39873","446as8787",4541);
>INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ("jason","sarrowq997","asdi663",65432);
>INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES ("rookie","ppaink4696","7q5s5445s",230545);
>```
> 圖片：
>
> ![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E4%B8%89-1.PNG)
> 
> 3-2 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
> ---
> 語法 :SELECT 項目 FROM 資料表;
> ```MYSQL
> 1. SELECT * FROM `member`;
> ```
>  PICTURE:
> 
> ![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E4%B8%89(%E8%A3%9C).PNG)
>
> 3-3 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
> ---
> 語法: SELECT 項目(*=全部) FROM 資料表 ORDER BY 主要排序項目 DESC(逆敘) P.S 預設為順;
> ```MYSQL
>1. SELECT * FROM `member` ORDER BY `time` DESC;
>```
> PICTURE
>
> ![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E4%B8%89-2.PNG)
>
>3-4 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
>---
>語法:SELECT 項目 FROM 表單 ORDER BY 排列項目 DESC(逆向) limit (忽略N筆數量),(收尋N筆資料量) 
>```MYSQL
>1. SELECT * FROM `member`
>2. ORDER BY `time` DESC
>3. limit 1,3;
>```
> PICTURE
>
>![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%823-4(2).PNG)
>
>3-5 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
>---
>語法:SELECT 項目 FROM 資料表 WHERE 條件項目=條件內容;
>```MYSQL
>1. SELECT * FROM `member`
>2. WHERE `username`="test" ;
>```
> PICTURE
>
>![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E4%B8%89-4.PNG)
>
>3-6 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
>---
>語法:SELECT 項目 FROM 資料表 WHERE 條件項目=條件內容 AND 條件項目2=條件內容2;
>```MYSQL
>1. SELECT * FROM `member`
>2. WHERE `username`="test" and `password`="test";
>```
>PICTURE
>
>![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E4%B8%89-5.PNG)
>
>3-7 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
>---
>語法: 更新前先輸入 SET SQL_SAFE_UPDATES=0; UPDATE 資料表 SET 項目=修改後項目內容 WHERE 條件項目=符合條件內容;
>```MYSQL
>1. SET SQL_SAFE_UPDATES=0;
>2. UPDATE `member`
>3. SET `name`="test2"
>4. WHERE `username`="test";
>```
> PICTURE
>
>![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E4%B8%89-6.PNG)
>===

要求四
=============
>4-1 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
>---
>語法:SELECT COUNT(項目)AS 想顯示的項目名稱 FROM 資料表; COUNT(項目)=計算table總共有幾筆資料
>```MYSQL
>1. SELECT COUNT(*) AS "總共會員數量" from `member`;
>```
> PICTURE
>
>![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E5%9B%9B-1.PNG)
>
>4-2  取得 member 資料表中，所有會員 follower_count 欄位的總和。
>---
>語法:SELECT SUM(想計算的項目) AS 想顯示的項目名稱 FROM 資料表  SUM=加總項次中的所有變項
>```MYSQL
>1. SELECT SUM (follower_count) AS "所有會員總追蹤人數" from `member`;
>```
> PICTURE
>
>![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E5%9B%9B-2.PNG)
>
>4-3 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
>---
>語法:SELECT AVG(想計算平均的項目) AS 想顯示的項目名稱 FROM 資料表 AVG=計算項次中所有變相的平均值
>```MYSQL
>1. SELECT AVG (follower_count) AS "所有會員平均追蹤數" from `member`;
>```
>PICTURE
>
>![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E5%9B%9B-3.PNG)
>
>---

要求五
=============
>5-1 在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定：
>---
>語法:CREAT TABLE 創建資料表名稱(項目 限制,項目2 限制),FOREIGN KEY 鍵外連接值 REFERENCES 外部資料表(外部資料表項目); show table=目前資料庫所有資料表
>```MYSQL
>1. creat table `message`(
>2. id BIGINT AUTO_INCREMENT PRIMARY KEY,`member_id` BIGINT NOT NULL,`content` VARCHAR(255) NOT NULL,`time` TIMESTAMP NOT NULL DEFAULT NOW(),
>3. FOREIGN KEY (`member_id`) REFERENCES `member`(`id`));
>4. show tables;
>```
> PICTURE
>
>![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%825.PNG)
>
>5-2 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
>---
>語法:SELECT 資料表.資料表項目,資料表2.資料表2項目 FROM 資料表1 AS 資料表縮寫 JOIN 加入的資料料表2 AS 資料表2縮寫 ON 資料表1.欲依據的重複項目=資料表2.欲依據的重複項目; P.S 如果沒有指定，兩個資料表如有重複的項目(如：id)會有衝突展生，將會無法使用join
>```MYSQL
>1. SELECT a.name, a.id, b.content FROM `member AS a
>2. JOIN `message` AS b
>3. ON a.id=b.member_id;
>```
> PICTURE
>
>![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E4%BA%94-2.PNG)
>
>5-3 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
>---
>語法:SELECT 資料表.資料表項目,資料表2.資料表2項目 FROM 資料表1 AS 資料表縮寫 JOIN 加入的資料料表2 AS 資料表2縮寫 ON 資料表1.欲依據的重複項目=資料表2.欲依據的重複項目 WHERE 條件項目=符合條件內容;
>```MYSQL
>1. SELECT a.name, a.id,a.username, b.content FROM `member` AS a
>2. JOIN `message` AS b
>3. ON a.id = b.member_id
>4. WHERE a.name="test2";
>```
> PICTURE
>
>
>![Alt text](https://github.com/sh-tasi/sh-tasi-wehelp-assignments/blob/master/week-5/picture/%E8%A6%81%E6%B1%82%E4%BA%94-3.PNG)
>---
