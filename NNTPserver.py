from twisted.internet import reactor

from twisted.news import database, news, nntp



GROUPS = [

 'local.example'

 ]

SMTP_SERVER = 'localhost:2500'

STORAGE_DIR = 'Inbox'



newsStorage = database.NewsShelf(SMTP_SERVER, STORAGE_DIR)

for group in GROUPS:

    newsStorage.addGroup(group, [])

factory = news.NNTPFactory(newsStorage)

reactor.listenTCP(2000, factory)

reactor.run( )