from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from notify.models import Notify
from django.utils.html import escape



class Feed(models.Model):
    user = models.ForeignKey(User)
    post = models.TextField(max_length=255)
    parent = models.ForeignKey('Feed', null=True, blank=True)
    likes = models.IntegerField(default=0)
    comments=models.CharField(max_length=100,null=True, blank=True) 
    date = models.DateTimeField(auto_now_add=True)
   
                                                                                                                                           = models.IntegerField(default=0)

    def __unicode__(self):
        return self.post

    @staticmethod ## accessing member function using name of class
    def get_feeds(from_feed=None):
        if from_feed is not None:
            feeds = Feed.objects.filter(parent=None, id__lte=from_feed)
        else:
            feeds = Feed.objects.filter(parent=None)
        return feeds

    @staticmethod
    def get_feeds_after(feed):
        feeds = Feed.objects.filter(parent=None, id__gt=feed)
        return feeds

    def get_comments(self):
        return Feed.objects.filter(parent=self).order_by('date')

    def calculate_likes(self):
        likes = Notify.objects.filter(notify_type=Notify.LIKE, feed=self.pk).count()
        self.likes = likes
        self.save()
        return self.likes

    def get_likes(self):
        likes = Notify.objects.filter(notify_type=Notify.LIKE, feed=self.pk)
        return likes

    def get_likers(self):
        likes = self.get_likes()
        likers = []
        for like in likes:
            likers.append(like.user)
        return likers

    def calculate_comments(self):
        self.comments = Feed.objects.filter(parent=self).count()
        self.save()
        return self.comments

    def comment(self, user, post):
        feed_comment = Feed(user=user, post=post, parent=self)
        feed_comment.save()
        self.comments = Feed.objects.filter(parent=self).count()
        self.save()
        return feed_comment

    def linked(self):
        return bleach.linkify(escape(self.post))
