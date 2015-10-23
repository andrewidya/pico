# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PicoRow'
        db.create_table(u'pico_column_picorow', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'pico_column', ['PicoRow'])

        # Adding model 'PicoColumn'
        db.create_table(u'pico_column_picocolumn', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('large_width', self.gf('django.db.models.fields.CharField')(default='1', max_length=50)),
            ('medium_width', self.gf('django.db.models.fields.CharField')(default='1', max_length=50)),
            ('small_width', self.gf('django.db.models.fields.CharField')(default='1', max_length=50)),
            ('extra_small_width', self.gf('django.db.models.fields.CharField')(default='1', max_length=50)),
        ))
        db.send_create_signal(u'pico_column', ['PicoColumn'])


    def backwards(self, orm):
        # Deleting model 'PicoRow'
        db.delete_table(u'pico_column_picorow')

        # Deleting model 'PicoColumn'
        db.delete_table(u'pico_column_picocolumn')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'pico_column.picocolumn': {
            'Meta': {'object_name': 'PicoColumn', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'extra_small_width': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '50'}),
            'large_width': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '50'}),
            'medium_width': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '50'}),
            'small_width': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '50'})
        },
        u'pico_column.picorow': {
            'Meta': {'object_name': 'PicoRow', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['pico_column']