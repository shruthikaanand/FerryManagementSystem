DELIMITER $$
CREATE procedure user_booking(
IN UID int, OUT msg varchar(30))
BEGIN
DECLARE count_tickets int;
set count_tickets= (SELECT Ticket_no from TICKET where Admin_id=UID);

IF count_tickets = 0 THEN
   set msg= 'Booked zero tickets';

ELSE
   set msg=(SELECT P_id FROM PASSENGER WHERE Admin_id = UID);
   
END IF;

END;$$
DELIMITER ;

SET @M="";
CALL user_booking(2,@M);
SELECT @M as ans;



























SELECT * FROM ans;
