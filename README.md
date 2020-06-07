# RATE-APP
This is a web application where users post their projects so that other users can vote on them and also write a review about them

A link to the website is provided so that can view the live web application before casting their vote

## Required features
- Python3.6
- Django framework
- Django rest-framework
- Postman
- Virtual environment

## Technologies & Languages
- Git (Version control)
- Python -Main programming language
- Django framework
- Html-layout of the web application
- Css and Bootstrap-Styling application
# Installation and Setup

Clone the repository below

```
git clone https://github.com/victormongare1/rate-app.git
```

### Create and activate a virtual environment

    virtualenv venv --python=python3.6

    source venv/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

### Copy environment variable

    cp env.sample .env

### Load/refresh .environment variables

    source .env

## Running the application

```
python manage.py server
```


## Endpoints Available
Available endpoints

| Method | Endpoint                        | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| POST   |        /accounts/register           | sign up a user                        | users         |
| POST   |         /accounts/login             | log in  a user                        | users         |
| POST   |         /newpost | users         |   post a new project


## Support and contact details
If you run into any issues or have questions, ideas or concerns  contact me at vicmongz254@gmail.com/0792651899 or make a contribution to the code.

## License
*{MIT License

Copyright (c) [2020] [Victor Mongare]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE..}*
Copyright (c) {2020} **{Victor Mongare}**