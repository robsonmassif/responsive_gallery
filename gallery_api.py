
from google.appengine.ext import ndb

class Person(ndb.Model):
  name = ndb.StringProperty()
  age = ndb.IntegerProperty()


p = Person(name='Arthur Dent', age=42)
k = p.put()

test_query = Person.query()

print test_query.count()
for person in test_query:
    print person.name

#
# class Piece(ndb.Model):
#     '''
#     An avant guard piece of art that is just a single integer
#     Described by a label that is just a string
#     Pretty cool, right?
#     '''
#     label = ndb.StringProperty()
#     art = ndb.IntegerProperty()
#
# AN_ART = Piece(label="R. Starr", art=48)
#
# AN_ART.put()
# #
# # print("<<><><><><", AN_ART.query())
# #
# # #The Stuff that follows is just API things

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

import random

package = 'Gallery'


class Greeting(messages.Message):
  """Greeting that stores a message."""
  label = messages.StringField(1)
  art = messages.IntegerField(2)


class LabelCollection(messages.Message):
  """Collection of Labels."""
  items = messages.MessageField(Greeting, 1, repeated=True)

hello_grt = Greeting(label="Hi World", art=6)

local_labels = ["A. Art", "B. Free", "C. Saw", "D. Lite"]

STORED_LABELS = LabelCollection(items=[Greeting(label=title, art=random.randint(0, 99)) for title in local_labels])


@endpoints.api(name='gallery', version='v1')
class GalleryApi(remote.Service):
  """Helloworld API v1."""

  @endpoints.method(message_types.VoidMessage, Greeting,
                    path='gallery', http_method='GET',
                    name='messages.sayHello')
  def greetings_list(self, unused_request):
    return hello_grt


  @endpoints.method(message_types.VoidMessage, LabelCollection,
                    path='labels', http_method='GET',
                    name='fill.labels')
  def label_list(self, unused_request):
    return STORED_LABELS



  ID_RESOURCE = endpoints.ResourceContainer(
      message_types.VoidMessage,
      id=messages.IntegerField(1, variant=messages.Variant.INT32))


APPLICATION = endpoints.api_server([GalleryApi])
