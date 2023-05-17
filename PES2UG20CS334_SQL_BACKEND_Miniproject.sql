CREATE TABLE ADMIN(Admin_id int, Fname varchar(30), Lname varchar(30), DOB date, Phone_no int, Email varchar(40), City varchar(30), Pincode int, Street varchar(40), PRIMARY KEY(Admin_id));
CREATE TABLE FERRY_INFO(Ferry_id varchar(20), Ferry_name varchar(35), Seat_availability int, source varchar(40), dest varchar(40), Vehicle_spots int, Type_of_ferry varchar(20), PRIMARY KEY(Ferry_id));
CREATE TABLE TICKET(Ticket_no int, Ferry_name varchar(35) , Ferry_id varchar(20)  , Seat_no varchar(10), Admin_id int, Passenger_name varchar(30), PRIMARY KEY(Ticket_no), FOREIGN KEY(Admin_id) REFERENCES ADMIN(Admin_id));
CREATE TABLE PAYMENT(Trans_id int, Amount int, Date_trans date, Mode_of_payment varchar(20), Ticket_no int, PRIMARY KEY(Trans_id), FOREIGN KEY(Ticket_no) REFERENCES Ticket(Ticket_no));
CREATE TABLE PASSENGER(P_id int, Fname varchar(30), Mname varchar(30), Lnamme varchar(30), Phone_no int, Address varchar(50), Email varchar(40), Admin_id int, PRIMARY KEY(P_id), FOREIGN KEY(Admin_id) REFERENCES ADMIN(Admin_id));
CREATE TABLE ROUTE_INFO(Source varchar(20), Dest varchar(20), Travel_time int, Ferry_id varchar(20) UNIQUE);
CREATE TABLE FERRY_STAFF(Captain varchar(40), Vice_captain varchar(40), Helpers int, Ferry_id varchar(20) UNIQUE);
CREATE TABLE VEHICLE_SLOT(Slot_no int UNIQUE, Location varchar(25), Ticket_no int, FOREIGN KEY(Ticket_no) REFERENCES TICKET(Ticket_no));
CREATE TABLE ACCOMPANY(Id int, P_id int, PRIMARY KEY(Id), FOREIGN KEY(P_id) REFERENCES PASSENGER(P_id));

INSERT INTO ADMIN(Admin_id,Fname,Lname,DOB,Phone_no,Email,City,Pincode,Street) VALUES
(2,'Riya','Jha','2002-12-1',12234567,'riya@gmail.com','Chennai',560078,'KK nagar'),
(3,'Arun','Vishwakumar','2000-2-5',82635237,'arun@gmail.com','Bangalore',560078,'Whitefield'),
(4,'Harry','Styles','1998-12-21',91726536,'style101@gmail.com','Chennai',901038,'Marina'),
(5,'Zayn','Malik','1980-12-1',12211567,'zma@gmail.com','Hyderabad',510098,'Whitefield'),
(6,'Louis','Phillip','2002-11-6',126876567,'lp89@gmail.com','Chennai',590078,'Kasi street'),
(7,'Liam','Payne','1999-4-3',11234567,'payno@gmail.com','Bangalore',560068,'Marthahalli');

INSERT INTO FERRY_INFO(Ferry_id,Ferry_name, Seat_availability, source , dest , Vehicle_spots, Type_of_ferry) VALUES
('A102','Black pearl',90,'Australia','England',85,'Deluxe'),
('B102','Scavenger',100,'Australia','Japan',50,'Regular'),
('G2222','Avenger',28,'India','Germany',12,'Luxury'),
('A1021D','Titanic',70,'China','England',10,'Cargo'),
('A122B','Black swan',45,'Russia','Canada',45,'Deluxe'),
('PE502','Bisleri',91,'Russia','Netherlands',60,'Regular');

INSERT INTO TICKET(Ticket_no,Ferry_name, Ferry_id, Seat_no, Admin_id ,Passenger_name) VALUES
(124,'Black pearl','A102','H12',2,'Jack'),
(1253,'Scavenger','B102','E100',5,'Quill'),
(756,'Avenger','G2222','A28',3,'Yasmin'),
(1097,'Titanic','A1021D','T56',6,'Chadeler'),
(12,'Black swan','A122B','J90',7,'Rachel'),
(645,'Bisleri','PE502','P23',2,'Joey');

INSERT INTO PAYMENT(Trans_id, Amount ,Date_trans , Mode_of_payment,Ticket_no) VALUES
(1000919,1500,'2021-09-11','UPI',124),
(2000283,1000,'2020-12-8','CASH',1253),
(45355526,5000,'2020-09-7','CASH',756),
(563637464,2567,'2019-05-26','NET BANKING',1097);

INSERT INTO PASSENGER(P_id,Fname, Mname ,Lnamme, Phone_no, Address, Email, Admin_id) VALUES
(334,'Cassie','Williams','Horan',16274533,'No.5, AECS , Bangalore','cwh54@yahoo.co.in',5),
(400,'Rue','Williams','Horan',16274533,'No.5, AECS , Bangalore','rwh9@yahoo.co.in',5),
(064,'Monica','Malvi','Geller',273547,'No.3, Neeladiri , Chennai','cwh54@yahoo.co.in',7),
(001,'Arjun','Venkata','Das',8991727,'No.82,Twin towers , Mumbai','cwh54@yahoo.co.in',2),
(093,'Rahul','Jagadesh','Annamalai',91754726,'No.109D, Shriram Spurthi , Delhi','cwh54@yahoo.co.in',3),
(982,'Ninad','James','Swift',9097436,'No.K12, UB City , Chennai','cwh54@yahoo.co.in',4);

INSERT INTO ROUTE_INFO(Source, Dest , Travel_time , Ferry_id) VALUES
('Mumbai','Boston',48,'A102'),
('Hong kong','Sydney',16,'A1021D'),
('Mumbai','Seattle',24,'B102'),
('Yeman','New york',15,'G2222'),
('Mumbai','London',18,'PE502');

INSERT INTO FERRY_STAFF(Captain, Vice_captain, Helpers, Ferry_id ) VALUES
('Jagadish','Kumar',15,'A102'),
('Jacobs','Nate',10,'A1021D'),
('Gunther','Vijay',10,'B102'),
('Jyoti','Surya',5,'G2222'),
('Arjun','Das',25,'PE502');

INSERT INTO VEHICLE_SLOT(Slot_no, Location , Ticket_no ) VALUES
(10,'Upper deck',1253),
(24,'Upper deck',756),
(19,'Patio',12),
(4,'Lower deck',645);

INSERT INTO ACCOMPANY(Id, P_id) VALUES
(1093,334),
(12,064),
(872,001);

SELECT * FROM ADMIN;
SELECT * FROM FERRY_INFO;
SELECT * FROM TICKET;
SELECT * FROM PAYMENT;
SELECT * FROM PASSENGER;
SELECT * FROM ROUTE_INFO;
SELECT * FROM FERRY_STAFF;
SELECT * FROM ROUTE_INFO;
SELECT * FROM ACCOMPANY;