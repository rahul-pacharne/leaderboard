from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    pic = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def getUserScore(self):
        return UserScore.query.join(
            User, (User.id == UserScore.uid)).filter_by(id=self.id).all()

    def getUserLevel(self):
        return UserScore.query.join(
            User, (User.id == UserScore.uid)).filter_by(id=self.id).all()

    def setUserScore(self,score):
        uid = self.id
        s = UserScore(score=score, uid=uid, latest_medal_id = 2)
        db.session.add(s)
        db.session.commit()

    def getMaxScore(self):
        return Levels.query.join(
            User, (User.id == Levels.uid)).filter_by(id=self.id).order_by(Levels.max_score.desc()).limit(1).all()

    def setMaxScore(self,score):
        uid = self.id
        item = Levels.query.get(uid) 
        try:
            item.max_score = score
        except AttributeError:
            s = Levels(max_score=score, uid=uid, name = self.name)
            db.session.add(s)
        #s = Levels(max_score=score, uid=uid, name = self.name)
        #db.session.add(s)
        db.session.commit()

    def getLowerUsers(self):
        try:
            s = self.getMaxScore()[0].max_score
        except IndexError:
            s = 0
        return Levels.query.join(
            User, (User.id == Levels.uid)).filter((Levels.max_score < s) & (Levels.uid != self.id)).order_by(Levels.max_score.desc()).limit(5).all()

    def getHigherUsers(self):
        try:
            s = self.getMaxScore()[0].max_score
        except IndexError:
            s = 0
        return Levels.query.join(
            User, (User.id == Levels.uid)).filter((Levels.max_score > s)).order_by(Levels.max_score.desc()).limit(5).all()


        

    

    def __repr__(self):
        return '<User {}>'.format(self.name)


class UserScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    score = db.Column(db.Integer)
    latest_medal_id = db.Column(db.Integer)
    

    def __repr__(self):
        return '<UserScore {}>'.format(self.score)


class Levels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(64))
    max_score = db.Column(db.Integer)
    

    def __repr__(self):
        return '<UserLevel {}>'.format(self.max_score)




@login.user_loader
def load_user(id):
    return User.query.get(int(id))
