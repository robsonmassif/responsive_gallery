
from google.appengine.ext import ndb


class Composition(ndb.Model):
  '''
  An avant guard piece of art that is just a single integer
  Described by a label that is just a string
  Pretty cool, right?
  '''
  label = ndb.StringProperty()
  art = ndb.IntegerProperty()


# ex = Composition(label="R. Starr", art=48)
# k = ex.put()
#
# test_query = Composition.query()

# print test_query.count()
# for item in test_query:
#   print item.key.delete()


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

# local_labels = ["A. Art", "B. Free", "C. Saw", "D. Lite"]
def collect_query():
  '''
  Loads a LabelCollection with the contents of the Datastore kind

  :return: LabelCollection of items in the database entry
  '''
  test_query = Composition.query()
  return LabelCollection(items=[Greeting(label=ent.label, art=ent.art) for ent in test_query])


@endpoints.api(name='gallery', version='v1')
class GalleryApi(remote.Service):
  """Helloworld API v1."""

  ID_RESOURCE = endpoints.ResourceContainer(
          message_types.VoidMessage,
          art=messages.IntegerField(1, variant=messages.Variant.INT32),
          label=messages.StringField(2, variant=messages.Variant.STRING))

  @endpoints.method(message_types.VoidMessage, Greeting,
                    path='gallery', http_method='GET',
                    name='messages.sayHello')
  def greetings_list(self, unused_request):
    return hello_grt


  @endpoints.method(message_types.VoidMessage, LabelCollection,
                    path='labels', http_method='GET',
                    name='fill.labels')
  def label_list(self, unused_request):
    return collect_query()

  @endpoints.method(ID_RESOURCE, Greeting,
                    path='new_art/{art,label}', http_method='GET',
                    name='new.composition')
  def new_composition(self, request):
    print("request", request.art, request.label)
    created = Greeting(art=request.art, label=request.label)
    new_ent = Composition(art=request.art, label=request.label)
    new_ent.put()

    # test_query = Composition.query()
    # print test_query.count()
    # for item in test_query:
    #   print item.label, item.art
    return created


  ID_RESOURCE = endpoints.ResourceContainer(
      message_types.VoidMessage,
      id=messages.IntegerField(1, variant=messages.Variant.INT32))


APPLICATION = endpoints.api_server([GalleryApi])
