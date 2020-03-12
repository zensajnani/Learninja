from learninja import app
from learninja.models import Users, Topics
from learninja import db

if __name__ == '__main__':

    with app.app_context():
        db.create_all()
        db.session.commit()

        # for i in range(5):
        #     user = Users(username="zen" + str(i+1), email='zen'+str(i+1)+'@appsolutenerd.com', password='password', user_type=1)
        #     db.session.add(user)
        # db.session.commit()

        n = 4


        for i in range(n):
            for j in range(n):
                for k in range(n):
                    topic = Topics(course='Course ' + str(i + 1), subject='Subject ' + str(j + (i * n) + 1),
                                   topic='Topic ' + str(k + (j * n) + (i * n * n) + 1))
                    db.session.add(topic)
        db.session.commit()
