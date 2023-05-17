create trigger Availabseats
after INSERT 
on TICKETS 
for each row 
update FERRY_INFO set Seat_availability = Seat_availability - 1 where Ferry_id = new.Ferry_id;

INSERT INTO TICKETS(Ticket_no,Ferry_name, Ferry_id, Seat_no, Admin_id ,Passenger_name) VALUES
(139,'Black pearl ','A102','N13',2,'Jack'),
(8991,'Black swan','A122B','P92',7,'Sherin');

SELECT * FROM FERRY_INFO;