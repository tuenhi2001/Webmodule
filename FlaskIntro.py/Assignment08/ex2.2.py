from flask import Flask

# class Flask:
#     def return:
#         return(self.name)
#         return(self.age)
#         return(self.hobby)
#         return(self.gender)

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello C4T4, this is homepage"

space = ()
@app.route("/user/<username>")
def user(username):
    users = {
    "huy":  {
                "name": "Nguyen Quang Huy",
                "age": "29",
                "gender": "male",
                "hobby": "coding"
            },
    "don": {
                "name": "Don zoombie",
                "age": "23",
                "hobby": "coding",
                "gender": "male"
        },
    "nhi":{
                "name": "Nhi Tran",
                "age": "17",
                "hobby": "reading",
                "gender": "female"

        }
    }
    
    if username in users.keys():
        return ("Name: " +  users[username]["name"] + "\t"  
        + "Age: " + users[username]["age"] + "\t"  +
        "Gender: " + users[username]["gender"] + "\t"  +
        "Hobby: " + users[username]["hobby"])
    else:
        return "User not found"


if __name__ == "__main__":
    app.run(debug=True)
