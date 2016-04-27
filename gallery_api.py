
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = 'Gallery'


class Greeting(messages.Message):
  """Greeting that stores a message."""
  message = messages.StringField(1)


class GreetingCollection(messages.Message):
  """Collection of Greetings."""
  items = messages.MessageField(Greeting, 1, repeated=True)


STORED_GREETINGS = GreetingCollection(items=[
    Greeting(message='Hello world!'),
    Greeting(message='goodbye world!'),
])

@endpoints.api(name='gallery', version='v1')
class GalleryApi(remote.Service):
  """Helloworld API v1."""

  @endpoints.method(message_types.VoidMessage, GreetingCollection,
                    path='gallery', http_method='GET',
                    name='greetings.listGreeting')
  def greetings_list(self, unused_request):
    return STORED_GREETINGS

  ID_RESOURCE = endpoints.ResourceContainer(
      message_types.VoidMessage,
      id=messages.IntegerField(1, variant=messages.Variant.INT32))


APPLICATION = endpoints.api_server([GalleryApi])
