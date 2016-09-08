from models import *


db.drop_tables([Counter])
db.create_tables([Counter], safe=True)
