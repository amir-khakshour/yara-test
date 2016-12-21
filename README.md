yaraholding.com Interview
=======
Here is a task assigned to me under the interview process of yaraholding.com as a backend Developer:

    به یک REST API جهت انجام عملیات CRUD برای یک مدل که بتواند اطلاعات ذیل را ثبت و نمایش دهد نیاز داریم
    Date Time [datetime]
    Purchase [string 150]
    Purchase ID [integer]
    User ID [integer]
    Name [string 150]
    Phone Number [string 20]
    Email [string 150]
    Address [logtext]
    لطفا برای انجام پروژه از Python 3.4 و Django 1.8 و 3 Django Rest Framework استفاده شود.

    فیلدهایی مانند شماره تلفن و ایمیل باید اعتبارسنجی شوند تا اطلاعات نادرست وارد سیستم نشوند.
    در صورتی که تونستید Authentication و Throttling برای امنیت API اضافه کنید.
    
    
Installation Guide:
1- Run:
    ./manage.py runserver

2- Open http://127.0.0.1:8000/ in your browser.

3- Navigate to:

    http://127.0.0.1:8000/api/1.0/misc_api/
    
4- to access the API you need to login with the following credentials:

     username: admin
     password: admin
    

Some notes
-----
-- Permissions are model based:
   permissions.DjangoModelPermissions
 
-- I used a custom throttling class for accessing the afformentioned API: 
   JokingThrottling
   
  
 PS: IMHO there are better ways to test a good programmar!



