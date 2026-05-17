from django.shortcuts import render




def home(request):
    data = {
        "name": "Ashok",
        "age": 22,
        "skills": ["Python", "Django", "SQL", "HTML", "CSS"],
       
        "students": [
            {"name": "Rahul", "age": 23},
            {"name": "Priya", "age": 21},
            {"name": "Vikram", "age": 24}
        ],

        "profile": {
            "personal": {
                "email": "ashok@gmail.com",
                "phone": "9999999999"
            }
        }
    }

    return render(request, "data.html", data)
   