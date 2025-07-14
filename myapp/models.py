from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    blog_content = CKEditor5Field("Content", config_name='extends', blank=True, null=True)
    blog_image = models.ImageField(upload_to='blogs/')
    posted_on = models.DateTimeField(auto_now_add=True)
    
    meta_title = models.CharField(max_length=255, help_text="Meta title for SEO", blank=True, null=True)
    meta_description = models.TextField(help_text="Meta description for SEO", blank=True, null=True)
    meta_keywords = models.TextField(help_text="Comma-separated keywords for SEO", blank=True, null=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-posted_on']

    def __str__(self):
        return self.blog_title
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.blog_title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

class Services(models.Model):
    service_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, help_text="Automatically Generate")
    service_description = CKEditor5Field("Content", config_name='extends')
    service_image = models.ImageField(upload_to='services/')
    priority = models.IntegerField(default=5)

    faq_question_1 = models.CharField(max_length=255, blank=True, null=True)
    faq_answer_1 = models.TextField(blank=True, null=True)
    faq_question_2 = models.CharField(max_length=255, blank=True, null=True)
    faq_answer_2 = models.TextField(blank=True, null=True)
    faq_question_3 = models.CharField(max_length=255, blank=True, null=True)
    faq_answer_3 = models.TextField(blank=True, null=True)
    faq_question_4 = models.CharField(max_length=255, blank=True, null=True)
    faq_answer_4 = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-created_at']

    def __str__(self):
        return self.service_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.service_title)
        super(Services, self).save(*args, **kwargs)

class Newsletter(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'
        ordering = ['-created_at']

    def __str__(self):
        return self.email
    
class Certificates(models.Model):
    certificate_name = models.CharField(max_length=200)
    certificate_image = models.ImageField(upload_to='certificates/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
        ordering = ['-created_at']

    def __str__(self):
        return self.certificate_name