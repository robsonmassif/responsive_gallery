
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = 'Gallery'


class Greeting(messages.Message):
  """Greeting that stores a message."""
  message = messages.StringField(1)

hello_grt = Greeting(message="Hi World")

@endpoints.api(name='gallery', version='v1')
class GalleryApi(remote.Service):
  """Helloworld API v1."""

  @endpoints.method(message_types.VoidMessage, Greeting,
                    path='gallery', http_method='GET',
                    name='messages.sayHello')
  def greetings_list(self, unused_request):
    return hello_grt

  ID_RESOURCE = endpoints.ResourceContainer(
      message_types.VoidMessage,
      id=messages.IntegerField(1, variant=messages.Variant.INT32))


APPLICATION = endpoints.api_server([GalleryApi])
