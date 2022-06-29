# Test

### Tasc description:
Написать микросервисное приложение на Flask + SqlAlchemy.
Оно по команде через Swagger должно запустить ansible-playbook,
который будет опрашивать сервисы Ambari и получать информацию о хостах
кластеров Hadoop. Эту информацию требуется хранить в БД Postgres,
версионировать и по запросу выводить в виде JSON-сообщения. Вместо
сервисов Ambari допустимо использовать заглушки. Вместо Swagger
допустимо использование front-end.

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


### swagger url:
[swagger editor](https://editor.swagger.io/?url=https://raw.githubusercontent.com/pink-goose/test_digitalleague/main/sw.yaml)
