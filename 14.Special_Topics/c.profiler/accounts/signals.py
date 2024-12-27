from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from accounts.models import Profile, Website

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Create a profile when a new user is created
        Profile.objects.create(user=instance)

def update_user_biography(user):
    # Safeguard to ensure there are no recursive signal issues
    if hasattr(user, 'profile'):
        # Get all websites associated with this user
        websites = user.website_set.all()

        # Sort websites by URL
        bio_list = sorted(website.url for website in websites)

        # Update the profile biography and save it
        profile = user.profile
        profile.bio = "\n".join(bio_list)
        profile.save()

@receiver(m2m_changed, sender=Website.users.through)
def update_biography(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        if reverse:
            # The signal was triggered from the User side of the relationship
            users = [instance]
        else:
            # The signal was triggered from the Website side
            users = instance.users.all()

        for user in users:
            if isinstance(user, User):  # Ensure user is an instance of User
                update_user_biography(user)



