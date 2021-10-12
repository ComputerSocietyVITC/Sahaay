## Where should you run the Uvicorn App
Uvicorn usually resolves app packages from top to bottom therefore it'd not resolve the logic app when it is being run inside the nested Core Directory 

## Which directory should the app be run under?
The app should be run under the parent Core directory that is the directory should be


```sh
./Core/
```

Refer the other docs to know how to run the app