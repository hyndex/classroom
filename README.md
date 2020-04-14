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
http://domain/changePassword/<optional:id>    POST 

{
    "old_password": "",
    "new_password": ""
}
```
# signup
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