from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from pico_column.models import PicoRow, PicoColumn
from django.utils.translation import ugettext_lazy as _
from pico_column.forms import PicoRowForm
from cms.models import CMSPlugin

class PicoRowPlugin(CMSPluginBase):
    model = PicoRow
    module = _("Pico Row Container")
    name = _("Row Container")
    render_template = "pico_column/row.html"
    allow_children = True
    child_classes = ["PicoColumnPlugin"]
    form = PicoRowForm

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder':placeholder,
        })
        return context

    def save_model(self, request, obj, form, change):
        response = super(PicoRowPlugin, self).save_model(request, obj, form, change)
        for x in range(int(form.cleaned_data['create'])):
            col = PicoColumn(parent=obj, placeholder=obj.placeholder, language=obj.language, large_width=form.cleaned_data['create_width'], position=CMSPlugin.objects.filter(parent=obj).count(), plugin_type=PicoColumnPlugin.__name__)
            col.save()
        return response

class PicoColumnPlugin(CMSPluginBase):
    model = PicoColumn
    module = _("Pico Multi Columns")
    name = _("Column")
    render_template = "pico_column/column.html"
    parent_classes = ["PicoRowPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder':placeholder,
            })
        return context

plugin_pool.register_plugin(PicoRowPlugin)
plugin_pool.register_plugin(PicoColumnPlugin)