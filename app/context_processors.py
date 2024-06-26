from django.contrib.auth.decorators import login_required
from app.models import Contact, Cart

# To avoid passing the contact details as context to every template, you can use Django’s context processors. Context processors allow you to add data to the context of every template without explicitly passing it in each view function.
def admin_contact_details(request):
  try:
    contact = Contact.objects.get(pk=1)  # Assuming there's only one contact record
    return {
      'admin_address': contact.address,
      'admin_phone_number': contact.phone_number,
      'admin_email': contact.email,
      'admin_facebook': contact.facebook,
      'admin_whatsapp': contact.whatsapp,
      'admin_twitter': contact.twitter,
      'admin_instagram': contact.instagram,
      'admin_tiktok': contact.tiktok,
      'admin_linkedin': contact.linkedin,
    }
  except Contact.DoesNotExist:
    return {}  # Return empty dictionary if no contact record found
  
# In your app’s apps.py, add the context processor to the context_processors list.
# In your project’s settings.py, add your context processor to the context_processors list.
# You can then acces the contact details in any template, using {{address}}

# to get the total item a user have in a cart, to avaoid passing it in all the views, I'm using the context_processor
def cart_length(request):
  user = request.user
  if user.is_anonymous:
    return {'totalCartItem': 0} # Return 0 total cart item if user is not logged in
  else:
    try:
      cart = Cart.objects.filter(user=user)
      return {
        'totalCartItem': len(cart)
      }
    except Cart.DoesNotExist:
      return {'totalCartItem': 0}  # Return 0 total cart item if no cart record found
  # In your project’s settings.py, add your context processor to the context_processors list. register the cart_length