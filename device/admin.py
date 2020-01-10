from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *


class SwitchResource(resources.ModelResource):

    class Meta:
        model = Switch
        skip_unchanged = True
        report_skipped = False
        import_name_fields = ['name']
        exclude = 'id'

        # Django是根据主键是否存在来判定是使用insert还是update的，使用sql是可以修改主键的。


@admin.register(Switch)
class SwitchAdmin(ImportExportModelAdmin):
    resources_class = SwitchResource
    # 要显示的字段
    list_display = ('id', 'name', 'ip', 'position', )
    list_display_links = ('name',)

    # 需要搜索的字段
    search_fields = ('name', 'ip')

    # 分页显示，一页的数量
    list_per_page = 15

    actions_on_top = True

