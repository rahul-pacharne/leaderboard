from flask import render_template,flash,redirect,url_for,request
from app import app
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = current_user
    #user = User.query.filter_by(email=email).first_or_404()
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('user',id = user.id))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/user/<id>',methods=['GET'])
def user(id):
    #user = User.query.filter_by(id=id).first_or_404()
    score = current_user.getMaxScore()
    lowUsers = current_user.getLowerUsers() 
    highUsers = current_user.getHigherUsers() 
    print("Here the users are")
    try:
        for usr in lowUsers:
            print(usr.name)
            print(print(usr.max_score))
    except:
        print("No users to show")
    try:
        print(highUsers[0].name)
    except:
        print("No users to show")
    return render_template('user.html', title='Home', user=current_user, score=score, lowUsers = lowUsers, highUsers = highUsers)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/play')
def play():
    l1 = ['Who are you?', 'Sky is yellow', 'Earth is Green']
    l2 = ['Giraffe is tall','Buffalo is red', 'Cow gives milk' ]
    level = current_user.getMaxScore()
    try:
        maxScore = level[0].max_score
    except IndexError:
        maxScore = 0
        
    if(int(maxScore) < 50): 
        q = app.config['L1']
    elif(int(maxScore) < 100):
        q = app.config['L2']
    elif(int(maxScore) < 150):
        q = app.config['L3']
    elif(int(maxScore) < 200):
        q = app.config['L4']
    elif(int(maxScore) < 250):
        q = app.config['L5']
    else:
        q = app.config['L6']
    return render_template('play.html', title = 'Play',user=current_user, level=level, questions = q )


@app.route('/calculate', methods=['POST'])
def calculate():
    ans1 = request.form['exampleRadios1']
    ans2 = request.form['exampleRadios2']
    ans3 = request.form['exampleRadios3']
    ans4 = request.form['exampleRadios4']
    ans5 = request.form['exampleRadios5']
    my_ans = [ans1,ans2,ans3,ans4,ans5]
    mul_fact = 1
    level = current_user.getMaxScore()
    try:
        maxScore = level[0].max_score
    except IndexError:
        maxScore = 0
    print(maxScore)
    if(int(maxScore) < 50): 
        correct_answers= app.config['A1']
    elif(int(maxScore) < 100):
        mul_fact = 2
        correct_answers = app.config['A2']
    elif(int(maxScore) < 150):
        mul_fact = 3
        correct_answers = app.config['A3']
    elif(int(maxScore) < 200):
        mul_fact = 4
        correct_answers = app.config['A4']
    elif(int(maxScore) < 250):
        mul_fact = 5
        correct_answers = app.config['A5']
    else:
        mul_fact = 6
        correct_answers = app.config['A6']
    print(correct_answers)
    score = 0
    score = sum(x == y for x, y in zip(my_ans, correct_answers))*10*mul_fact
    print("My score is")
    print(score)
    print("============")
    print(my_ans)
    current_user.setUserScore(score) 
    if(score > maxScore):
        current_user.setMaxScore(score) 
    return redirect(url_for('index'))
