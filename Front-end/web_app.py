from flask import Flask, render_template, request, flash
#from backend_controller import run_script, is_running


app = Flask(__name__)
app.secret_key = 'buddies'


@app.route('/index',  methods=['POST', 'GET'])
def home_page():
    if request.method == "POST":
        job_title = request.form.getlist('job-title')
        job_location = request.form.getlist('job-location')
        job_websites = request.form.getlist('website')
        if is_running():
            flash('Transaction is already running', 'info')
        else:
            run_script(job_title, job_location, job_websites)
            flash('You request has been passed', 'info')
    return render_template('index.html')


@app.route('/recommended',  methods=['POST', 'GET'])
def recommended():
    return render_template('recommended.html')


if __name__ == "__main__":
    app.run()
