from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        now_time = timezone.now()
        local_time_now = timezone.localtime(now_time)
        if self.leaved_at:
            delta = timezone.localtime(self.leaved_at)\
                    - timezone.localtime(self.entered_at)
        else:
            delta = local_time_now - timezone.localtime(self.entered_at)
        return delta
    def format_duration(self):
        return str(self.get_duration())


    def is_visit_long(self, minutes=60):
        return self.get_duration().total_seconds() // 60 > minutes
