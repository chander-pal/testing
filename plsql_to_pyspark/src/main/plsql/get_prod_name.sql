CREATE OR REPLACE FUNCTION simple_redaction(
  input VARCHAR2,
  price NUMBER)
return varchar2
as
BEGIN
  IF (price > 100) THEN
    RETURN SUBSTR(input,0,1)||'*****'||SUBSTR(input,-1);
  ELSE
    RETURN input;
  END IF;
END;
/