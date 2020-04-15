# classroom
deadline yyyymmdd

# login
```
http://domain/login/    POST 
{
"username":"mojo",
"password":"qwerty"
}
```

# logout
```
http://domain/logout/    POST 
```
# changepassword
```
http://domain/changePassword/    POST 

{
    "old_password": "",
    "new_password": ""
}
```
# signup or profile
```
http://domain/profile/<optional:id>  POST PUT DELETE GET
    {
        "user": {
            "username": "dhunu",
            "password": "qwerty",
            "email": "diki4bhuyan@gmail.com"
        },
        "name": "Chinmoy Bhuyan",
        "image": null,
        "address": "Dergaon Assam India",
        "phone": "9876543210"
    }
```

# group

```
http://domain/group/<optional:id>   POST PUT DELETE GET
{
    "name": "",
    "description": ""
}
```

# grouprole

```
http://domain/add/<optional:id>    POST DELETE GET
{
    "username": "ssdg",
    "groupid": "2",
    "role": "teacher"
}
```

# notes

```
http://127.0.0.1:8000/group/<optional:id>    POST PUT DELETE GET
{
    "groupid": "2",
    "title": "lololol",
    "description": "dararataya"
}
```

# assignment 

```
http://127.0.0.1:8000/class/assignment/<optional:id>    POST PUT DELETE GET
{
    "groupid": "2",
    "title": "kor kla harami",
    "description": "mok kla dibi",
    "deadline": "20200530" <yyyymmdd>
}

PUT
{
    "groupid":2,
    "title": "kokshdgfrkshdkfr kla harami",
    "description": "mkjabdfkahkfdsok kla dibi",
    "deadline": "20200530",
    "file": null,
    "created_by": 1
}
```

# assignment submit
```
http://127.0.0.1:8000/class/submit/<optional:id>    POST PUT DELETE GET
{
    "assignmentid": "1",
    "title": "this is the result",
    "description": "fuck you"
}
```
