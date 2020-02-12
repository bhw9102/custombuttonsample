from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.html import format_html
from sample.models import Case


def test_custom_method(request):
    print('TEST CUSTOM')
    return HttpResponseRedirect(reverse('admin:test'))


class CaseAdmin(admin.ModelAdmin):
    class Meta:
        model = Case

    def get_urls(self):
        urls = super(CaseAdmin, self).get_urls()
        added_urls = [
            path('test/', test_custom_method, name='test'),
        ]
        return urls + added_urls

    def test_custom(self, obj):
        return format_html(
            '<a class="button" href={0}>TEST CUSTOM</a>',
            reverse('admin:test')
        )
    list_display = ('pk', 'content', 'test_custom')


admin.site.register(Case, CaseAdmin)

