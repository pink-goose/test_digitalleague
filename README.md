# Test

### install requirements 
```
pip install -r .\requirements.txt
```

### Run
```
cd src  
python app.py
```

### run docker-compose:
```
docker-compose -f docker-compose.yml up --build server
```

### stop docker-compose:
```
docker-compose -f docker-compose.yml down -v
```

Example of Ambari request-response
``` 
https://github.com/apache/ambari/blob/trunk/ambari-server/docs/api/v1/hosts-host.md
```
