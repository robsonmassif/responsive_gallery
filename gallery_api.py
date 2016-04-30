
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = 'Gallery'


class Greeting(messages.Message):
  """Greeting that stores a message."""
  message = messages.StringField(1)

class LabelCollection(messages.Message):
  """Collection of Labels."""
  items = messages.MessageField(Greeting, 1, repeated=True)

hello_grt = Greeting(message="Hi World")

local_labels = ["A. Art", "B. Free", "C. Saw", "D. Lite"]

STORED_LABELS = LabelCollection(items=[Greeting(message=label) for label in local_labels])

next_label = Greeting(message="A. Art")

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
