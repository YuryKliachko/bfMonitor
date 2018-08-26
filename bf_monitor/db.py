from bf_monitor.models.test_data import TestUser
from bf_monitor import db
from bf_monitor.models.user import User

#db.create_all()
#user_1 = User(username='Yury', email='uraklechko@gmail.com', password='Iraura1988')
#db.session.add(user_1)
#test_data_1 = TestUser(username='r2app181@mailinator.com', password='Nttdata@123', type='PAYM', user_id='1')
#db.session.add(test_data_1)
#test_data_2 = TestUser(username='v4payg34@yopmail.com', password='Nttdata@1', type='PAYG', user_id='1')
#db.session.add(test_data_2)
#test_data_3 = TestUser(username='dr161@yopmail.com', password='Nttdata@123', type='PAYG', user_id='2')
#db.session.add(test_data_3)
#db.session.commit()
user = User.query.all()
test_data = TestUser.query.all()
print(user)
print(test_data)

