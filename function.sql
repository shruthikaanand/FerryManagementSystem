DELIMITER $$

CREATE FUNCTION payment_due_date(payment_date DATE)
RETURNS VARCHAR(50)

 BEGIN
 
    DECLARE pay VARCHAR(50);
	
    IF CURRENT_DATE() > payment_date THEN 
	   SET pay = 'Payment done';
	   
    ELSEIF CURRENT_DATE() <= payment_date THEN 
	   SET pay = 'Payment not done';
	
	
	   
    END IF;
    
	RETURN pay;
	
END; $$

DELIMITER ;

SELECT Trans_id,Amount,Mode_of_payment,Ticket_no,CURDATE(),payment_due_date(Date_trans)  FROM  PAYMENT;
