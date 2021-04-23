from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

class Sheet(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Sheet/images", default="")
    
    def __str__(self):
        return self.name                      


class ClassDetails(models.Model):
    className = models.CharField(verbose_name="ClassName", max_length=60, default=None, blank=True)
    classTitle = models.CharField(verbose_name="ClassTitle", max_length=200, default=None, blank=True)
    remark = models.TextField(verbose_name="remark", max_length=600, default=None, blank=True)
    def __str__(self):
        return self.className + " | " + self.remark


class Subject(models.Model):
    className = models.ForeignKey(ClassDetails,on_delete=models.CASCADE, related_name="ClassDetails")
    SubjectName = models.CharField(verbose_name="SubjectName", max_length=60, default=None, blank=True)
    SubjectTitle = models.CharField(verbose_name="SubjectTitle", max_length=200, default=None, blank=True)
    remark = models.TextField(verbose_name="remark", max_length=600, default=None, blank=True)
    def __str__(self):
        return self.SubjectName + " | " + self.className.className

class Topic(models.Model):
    Subject = models.ForeignKey(Subject,on_delete=models.CASCADE, related_name="Subject")
    TopicName = models.CharField(verbose_name="TopicName", max_length=60, default=None, blank=True)
    topicTitle = models.CharField(verbose_name="topicTitle", max_length=200, default=None, blank=True)
    #remark = models.TextField(verbose_name="remark", max_length=600, default=None, blank=True)
    def __str__(self):
        return self.Subject.className.className + " | " + self.Subject.SubjectName + " | " + self.TopicName


class SubTopic(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name="topic")
    SubTopicName = models.CharField(verbose_name="SubTopicName", max_length=60, default=None, blank=True)
    subtopicTitle = models.CharField(verbose_name="subtopicTitle", max_length=200, default=None, blank=True)
    #remark = models.TextField(verbose_name="remark", max_length=600, default=None, blank=True)
    def __str__(self):
        return self.SubTopicName + " | " + self.topic.TopicName

        
class Explain(models.Model):
    SubTopic = models.ForeignKey(SubTopic,on_delete=models.CASCADE, related_name="SubTopic")
    explaintitle = models.CharField(verbose_name="explaintitle", max_length=200, default=None, blank=True, null=True)
    body = models.TextField(verbose_name="SubTopicName", max_length=6000, default=None, blank=True)
    imgBlack = models.ImageField(upload_to ='uploads/gallery/Black/', default=None, blank=True, null=True)
    imgColor = models.ImageField(upload_to ='uploads/gallery/Color/', default=None, blank=True, null=True)
    #remark = models.CharField(verbose_name="remark", max_length=60, default=None, blank=True)
    def __str__(self):
        return self.SubTopic.SubTopicName + " | " + self.body[:30]

class Package(models.Model):
    pkg_name = models.CharField(verbose_name="pkg_name", max_length=100, default=None, blank=True)
    pkg_price = models.IntegerField()
    pkg_feature_1 = models.CharField(verbose_name="feature", max_length=100, default=None, blank=True, null=True)
    pkg_feature_2 = models.CharField(verbose_name="feature", max_length=100, default=None, blank=True, null=True)
    pkg_feature_3 = models.CharField(verbose_name="feature", max_length=100, default=None, blank=True, null=True)
    pkg_feature_4 = models.CharField(verbose_name="feature", max_length=100, default=None, blank=True, null=True)
    pkg_feature_5 = models.CharField(verbose_name="feature", max_length=100, default=None, blank=True, null=True)
    pkg_feature_6 = models.CharField(verbose_name="feature", max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.pkg_name

class Feature(models.Model):
    pkg_name = models.ForeignKey(Package,on_delete=models.CASCADE, related_name="Package")
    feature_name = models.CharField(verbose_name="pkg_name", max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.feature_name


# class LoggedInUser(models.Model):
#     user = models. OneToOneField(settings.AUTH_USER_MODEL, related_name="logged_in_user", on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=32, blank=True, null=True)

#     def __str__(self):
#         return self.user.email