from django.db import models


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    QA_SPECIALIST = 2
    DEV_OPS_SPECIALIST = 3

    SOFTUNI = 'SoftUni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    COMPANIES = (SOFTUNI, GOOGLE, FACEBOOK)

    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=49,
        null=True,
        blank=True,
    )

    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN',
    )

    job_title = models.IntegerField(
        choices=(
            (SOFTWARE_DEVELOPER, 'Software Developer'),
            (QA_SPECIALIST, 'QA Engineer'),
            (DEV_OPS_SPECIALIST, 'DevOps Specialist'),
        ),
    )

    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=((c, c) for c in COMPANIES),
    )
    # One-to-Many
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('company', 'first_name',)


class User(models.Model):
    email = models.EmailField()

    # One-to-One Relation
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )

    dead_line = models.DateField(
        null=True,
        blank=True,
    )
    # Many-to_Many
    employees = models.ManyToManyField(
        to=Employee
    )
