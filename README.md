Sequential Time-Based UUIDs
===========================

A UUID class that combines the timestamp with random bytes to create a unique
identifier that is orderable by creation date.  

Bit Layout is:  
[32 bits timestamp high]-[16 bits timestamp mid]-[16 bits timestamp low]-[16 bits random]-[48 bits random]

Creations
---------  
- Create a TimeUUID: `timeUUID.TimeUUID()`
- Create a TimeUUID from a hex string: `timeUUID.TimeUUID('541b8dce-08a9-11e5-8f7a-60f81dcfcde')`  
- Create a TimeUUID from a timestamp: `timeUUID.TimeUUID(timestamp=time.time())`  

Fields  
------  
- `str(timeUUID.TimeUUID())`, the hex string representation  
- `timeUUID.TimeUUID().timestamp`, the timestamp corresponding to the UUID    
- `timeUUID.TimeUUID().datetime`, the datetime corresponding to the UUID  
