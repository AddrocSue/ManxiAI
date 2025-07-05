from django.apps import AppConfig


class ModelManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.model_management'
    verbose_name = '模型管理' 