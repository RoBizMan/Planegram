from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

DECISION = ((0, "Awaiting"), (1, "Accepted"), (2, "Rejected"))


class Aircraft(models.Model):
    '''
    Represents an aircraft with make and model details.
    '''
    plane_make = models.CharField(max_length=40)
    plane_model = models.CharField(max_length=40)

    class Meta:
        '''
        Sorts the list of planes by name of plane make order.
        '''
        ordering = ["plane_make"]

    def __str__(self):
        '''
        Displays the list with name of plane make and model.
        '''
        return f"{self.plane_make} | {self.plane_model}"


class Gram(models.Model):
    '''
    Represents a photograph taken of an aircraft.

    Stores a single Gram upload entry related to
        :model:`auth.User` and :model:`blog.Aircraft`.

    Attributes:
        caption (str): A unique caption for the photograph.
        image (CloudinaryField): The image of the aircraft.
        plane (ForeignKey from :model:`blog.Aircraft`): The aircraft associated
            with the photograph.
        date_photographed (date): The date the photograph was taken.
        photographer (ForeignKey from :model:`user.Auth`): The user who took
            the photograph.
        love (ManyToManyField): Users who liked the photograph.
        created_on (datetime): The timestamp when the photograph was created.
    '''
    caption = models.CharField(max_length=50, unique=True)
    image = CloudinaryField('image', default='placeholder')
    plane = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    date_photographed = models.DateField()
    photographer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="gram_posts"
    )
    love = models.ManyToManyField(User, related_name="loved_grams", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Sorts the list of grams by the date the gram was created on.
        '''
        ordering = ["-created_on"]

    def __str__(self):
        '''
        Displays the list with caption and photographer.
        '''
        return f"{self.caption} by {self.photographer}"

    def futuredate(self):
        '''
        Prevents the user from uploading with the future date photographed
            beyond today's date.
        '''
        if self.date_photographed > datetime.date.today():
            raise ValidationError(
                "Date photographed cannot be dated past today's date."
            )


class Report(models.Model):
    '''
    Represents a report submitted for a Gram.

    Stores a single report entry related to
        :model:`auth.User` and :model:`blog.Gram`.

    Attributes:
        gram (ForeignKey from :model:`blog.Gram`): The Gram
            that is being reported.
        user (ForeignKey from :model:`auth.User`): The user
            who submitted the report.
        message (str): The content of the report.
        decision (int): The decision made regarding the report.
        date_reported (datetime): The timestamp when the report was submitted.
    '''
    gram = models.ForeignKey(Gram, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    decision = models.IntegerField(choices=DECISION, default=0)
    date_reported = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Sorts the list of reports by the date the gram was reported.

        Prevents the user from potential spamming the post by reporting
            the same post multiple times.
        '''
        ordering = ["-date_reported"]
        unique_together = ["gram", "user"]

    def __str__(self):
        '''
        Displays the list of reports reported on gram by whom.
        '''
        return f"Report on {self.gram} submitted by {self.user}"
