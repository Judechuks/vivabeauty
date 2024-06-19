# To avoid passing the contact details as context to every template, you can use Django’s context processors. Context processors allow you to add data to the context of every template without explicitly passing it in each view function.

from app.models import Contact

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