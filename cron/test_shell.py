from django_cron import CronJobBase, Schedule
from django.utils import timezone

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 0.01 # every 2 hours
    MIN_NUM_FAILURES = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.my_cron_job'    # a unique code

    def do(self):
         cur_time = timezone.datetime.now()
         print cur_time
        # open('orcn.job','a').write(cur_time)
        # pass    # do your thing here