from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError


#Limit Profile Picture Upload to 1MB
def validate_image(image):
    file_size = image.file.size
    limit_mb = 1
    if file_size > limit_mb * 1024 * 1024:  # 1kb = 1024b ; 1mb = 1024kb
        raise ValidationError("Max size of file is %s MB" % limit_mb)

class MyAccountManager(BaseUserManager):
    
    def create_user(self, email, name, password):
        if not email:
            raise ValueError('New user must have an email!')
        if not name:
            raise ValueError('New user must have a name!')
        if not password:
            raise ValueError('New user must have a password!')
        
        #create user instance
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            password = password
        )

        #set password
        user.set_password(password)

        #commit the new user
        user.save(using=self.db)
        return user

    def create_superuser(self, email, name, password):
        if not email:
            raise ValueError('New user must have an email!')
        if not name:
            raise ValueError('New user must have a name!')
        if not password:
            raise ValueError('New user must have a password!')
        
        #create user instance
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            password = password
        )

        #set password
        user.set_password(password)

        #set admin attribute
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        #commit the new user
        user.save(using=self.db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=500, unique=True, null=False)
    name = models.CharField(max_length=500, null=False)
    password = models.CharField(max_length=500, null=False)

    #upload profile picture with size <= 1MB to "media/pp/" directory in Cloudinary
    profile_pict = models.ImageField(upload_to='pp/', validators=[validate_image], blank=True)

    # Required fields for custom user model
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    #Set the login identifier
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS =  ['name', 'password']

    objects = MyAccountManager()

    def __str__(self) -> str:
        return self.email
