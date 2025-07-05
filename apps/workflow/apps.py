from django.apps import AppConfig


class WorkflowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.workflow'
    verbose_name = '工作流编排' 