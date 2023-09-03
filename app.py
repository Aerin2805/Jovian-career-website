from flask import Flask  , render_template , jsonify

app = Flask(__name__)

JOBS = [
    {
        "id" : 1,
        "Title" : "Data Analyst",
        "Location" : "Surat , India",
        "Salary" : "Rs. 1,00,000"
    },
    {
        "id" : 2,
        "Title" : "Data Scientist",
        "Location" : "Ahemdabad , India",
        "Salary" : "Rs. 10,00,000"
    },
    {
        "id" : 3,
        "Title" : "Frontented engineer",
        "Location" : "Bharuch , India",
        "Salary" : "Rs. 8,00,000"
    },
    {
        "id" : 4,
        "Title" : "Bakend Engineer",
        "Location" : "Maheshana, India",
        "Salary" : "Rs. 12,00,000"
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html" , jobs=JOBS , company_name = "Jovian")

@app.route("/api/jobs")

def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__" :
    app.run(host='0.0.0.0' , debug=True)