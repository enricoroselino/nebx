import schedule
import math


class ScheduleManager:
    @staticmethod
    def get_schedules() -> list[schedule.Job]:
        return schedule.get_jobs()

    @staticmethod
    def add_next_job(countdown_seconds: float | int, job: any, *job_tags, **job_params) -> None:
        converted_int: int = math.ceil(countdown_seconds) if isinstance(countdown_seconds, float) else countdown_seconds
        schedule.every(converted_int).seconds.do(job, **job_params).tag(*job_tags)

    @staticmethod
    def clear_jobs(*tags):
        schedule.clear(*tags)

    @staticmethod
    def run_jobs(immediate: bool = False) -> None:
        schedule.run_all() if immediate is True else schedule.run_pending()
