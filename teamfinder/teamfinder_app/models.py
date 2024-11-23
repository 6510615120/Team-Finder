from django.db import models
from django.contrib.auth.models import AbstractUser, User
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(username, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=32)
    email_address = models.EmailField(blank=True)
    name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='', blank=True, null=True, default="fallback.png")
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Faculty(TagBase):
    faculty = models.TextField()

class FacultyTag(GenericTaggedItemBase):
    tag = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="faculty_tag")

class Major(TagBase):
    major = models.TextField()

class MajorTag(GenericTaggedItemBase):
    tag = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="major_tag")

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_groups")
    group_name = models.CharField(max_length=255)

class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")

class DirectMessage(models.Model):
    message = models.OneToOneField(Message, on_delete=models.CASCADE, primary_key=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_direct_messages")

class GroupMessage(models.Model):
    message = models.OneToOneField(Message, on_delete=models.CASCADE, primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_messages")

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    heading = models.CharField(max_length=255)
    content = models.TextField()
    finish = models.BooleanField(default=False)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class PostComment(models.Model):
    post_comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    reaction = models.CharField(max_length=50, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class ResultPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    tag = TaggableManager()

class RecruitPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    tag = TaggableManager()
    status = models.BooleanField(default=True)

class Requirement(models.Model):
    require_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(RecruitPost, on_delete=models.CASCADE, related_name="requirements")
    req_faculty = TaggableManager(through=FacultyTag)
    req_major = TaggableManager(through=MajorTag)
    year_min = models.IntegerField(default=1)
    year_max = models.IntegerField(default=4)
    description = models.TextField()

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="requests")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    message = models.TextField()
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='led_teams')
    recruit_post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_feedbacks')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_feedbacks')
    communication_pt = models.IntegerField()
    collaboration_pt = models.IntegerField()
    reliability_pt = models.IntegerField()
    technical_pt = models.IntegerField()
    empathy_pt = models.IntegerField()
    comment = models.TextField(blank=True)



    