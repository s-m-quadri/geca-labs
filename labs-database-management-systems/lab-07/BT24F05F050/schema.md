+----------------+        1        N       +----------------+
|   Customer     |------------------------>|     Order      |
+----------------+                         +----------------+
| PK Customer_ID |                         | PK Order_ID    |
| Name           |                         | Order_Date     |
| Email          |                         | Total_Amount   |
| Phone          |                         | Status         |
| Address        |                         | FK Customer_ID |
+----------------+                         +----------------+
                                                  |
                                                  | 1
                                                  | 
                                                  | N
                                          +-------------------+
                                          |   Order_Item      |
                                          +-------------------+
                                          | PK Order_Item_ID  |
                                          | Quantity          |
                                          | Subtotal          |
                                          | FK Order_ID       |
                                          | FK Item_ID        |
                                          +-------------------+
                                                  |
                                                  | N
                                                  |
                                                  | 1
                                          +----------------+
                                          |   Menu_Item    |
                                          +----------------+
                                          | PK Item_ID     |
                                          | Name           |
                                          | Description    |
                                          | Price          |
                                          | FK Restaurant_ID|
                                          +----------------+
                                                  |
                                                  | N
                                                  |
                                                  | 1
                                          +----------------+
                                          |  Restaurant    |
                                          +----------------+
                                          | PK Restaurant_ID|
                                          | Name            |
                                          | Location        |
                                          | Contact_Number  |
                                          +----------------+

        +----------------+           +----------------+
        |    Payment     |           |    Delivery    |
        +----------------+           +----------------+
        | PK Payment_ID  |           | PK Delivery_ID |
        | Amount         |           | Delivery_Time  |
        | Method         |           | Status         |
        | Status         |           | Address        |
        | FK Order_ID    |           | FK Order_ID    |
        +----------------+           +----------------+

Order 1 -------- 1 Payment  
Order 1 -------- 1 Delivery