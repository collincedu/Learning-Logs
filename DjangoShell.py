import os
os.environ.setdefault("DJANGO_SETTINGS_MODLUE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic

topics = Topic.objects.all()

for t in topics:
    print(t.id, ' ',t.text)

#select * from Topic where id =1
t = Topic.objects.get(id=1)

print(t.text)
print(t.date_added)

#get all corresponding entries for chess (topic)
entries = t.entry_set.all()

for e in entries:
    print(e.text)