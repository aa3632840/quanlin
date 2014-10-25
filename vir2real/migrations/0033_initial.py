# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RealClass'
        db.create_table(u'vir2real_realclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('discription', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('has_generate_fields', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'vir2real', ['RealClass'])

        # Adding model 'RealFeild'
        db.create_table(u'vir2real_realfeild', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pclass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.RealClass'])),
            ('discription', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'vir2real', ['RealFeild'])

        # Adding model 'RealFieldAlias'
        db.create_table(u'vir2real_realfieldalias', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('real_field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.RealFeild'])),
            ('alias_key', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alias_choice', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'vir2real', ['RealFieldAlias'])

        # Adding model 'VirtualClass'
        db.create_table(u'vir2real_virtualclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('discription', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'vir2real', ['VirtualClass'])

        # Adding model 'VirtualFeild'
        db.create_table(u'vir2real_virtualfeild', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pclass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.VirtualClass'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='TYPE_CHAR', max_length=50)),
        ))
        db.send_create_signal(u'vir2real', ['VirtualFeild'])

        # Adding model 'DataAdapter'
        db.create_table(u'vir2real_dataadapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('real_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.RealClass'])),
        ))
        db.send_create_signal(u'vir2real', ['DataAdapter'])

        # Adding model 'DataFeildAdapter'
        db.create_table(u'vir2real_datafeildadapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_adapter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.DataAdapter'])),
            ('real_field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.RealFeild'])),
            ('order_id', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('is_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'vir2real', ['DataFeildAdapter'])

        # Adding model 'Virtual2RealAdapterClassMap'
        db.create_table(u'vir2real_virtual2realadapterclassmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('virtual_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.VirtualClass'])),
            ('real_class_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'vir2real', ['Virtual2RealAdapterClassMap'])

        # Adding model 'Virtual2RealAdapterFieldMap'
        db.create_table(u'vir2real_virtual2realadapterfieldmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('class_map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.Virtual2RealAdapterClassMap'])),
            ('virtual_field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.VirtualFeild'])),
            ('real_field_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('order_id', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'vir2real', ['Virtual2RealAdapterFieldMap'])

        # Adding model 'Person'
        db.create_table(u'vir2real_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('phone_num', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('qq_num', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('alipay_num', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'vir2real', ['Person'])

        # Adding model 'QuickAddJob'
        db.create_table(u'vir2real_quickaddjob', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('data_adapter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.DataAdapter'])),
            ('data_adapter_details', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('source_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'vir2real', ['QuickAddJob'])

        # Adding model 'VirtualData'
        db.create_table(u'vir2real_virtualdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_adapter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.DataAdapter'])),
            ('quick_job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vir2real.QuickAddJob'], null=True, blank=True)),
            ('source_json', self.gf('django.db.models.fields.TextField')()),
            ('source_line', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('can_be_restore_real', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('matching_objects_count', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('matching_objects', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('erro_msg', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'vir2real', ['VirtualData'])


    def backwards(self, orm):
        # Deleting model 'RealClass'
        db.delete_table(u'vir2real_realclass')

        # Deleting model 'RealFeild'
        db.delete_table(u'vir2real_realfeild')

        # Deleting model 'RealFieldAlias'
        db.delete_table(u'vir2real_realfieldalias')

        # Deleting model 'VirtualClass'
        db.delete_table(u'vir2real_virtualclass')

        # Deleting model 'VirtualFeild'
        db.delete_table(u'vir2real_virtualfeild')

        # Deleting model 'DataAdapter'
        db.delete_table(u'vir2real_dataadapter')

        # Deleting model 'DataFeildAdapter'
        db.delete_table(u'vir2real_datafeildadapter')

        # Deleting model 'Virtual2RealAdapterClassMap'
        db.delete_table(u'vir2real_virtual2realadapterclassmap')

        # Deleting model 'Virtual2RealAdapterFieldMap'
        db.delete_table(u'vir2real_virtual2realadapterfieldmap')

        # Deleting model 'Person'
        db.delete_table(u'vir2real_person')

        # Deleting model 'QuickAddJob'
        db.delete_table(u'vir2real_quickaddjob')

        # Deleting model 'VirtualData'
        db.delete_table(u'vir2real_virtualdata')


    models = {
        u'vir2real.dataadapter': {
            'Meta': {'object_name': 'DataAdapter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'real_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.RealClass']"})
        },
        u'vir2real.datafeildadapter': {
            'Meta': {'object_name': 'DataFeildAdapter'},
            'data_adapter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.DataAdapter']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'real_field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.RealFeild']"})
        },
        u'vir2real.person': {
            'Meta': {'object_name': 'Person'},
            'alipay_num': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_num': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'qq_num': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'vir2real.quickaddjob': {
            'Meta': {'object_name': 'QuickAddJob'},
            'data_adapter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.DataAdapter']"}),
            'data_adapter_details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'vir2real.realclass': {
            'Meta': {'object_name': 'RealClass'},
            'discription': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'has_generate_fields': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'vir2real.realfeild': {
            'Meta': {'object_name': 'RealFeild'},
            'discription': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'null': ('django.db.models.fields.BooleanField', [], {'max_length': '50'}),
            'pclass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.RealClass']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'vir2real.realfieldalias': {
            'Meta': {'object_name': 'RealFieldAlias'},
            'alias_choice': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'alias_key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'real_field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.RealFeild']"})
        },
        u'vir2real.virtual2realadapterclassmap': {
            'Meta': {'object_name': 'Virtual2RealAdapterClassMap'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'real_class_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'virtual_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.VirtualClass']"})
        },
        u'vir2real.virtual2realadapterfieldmap': {
            'Meta': {'object_name': 'Virtual2RealAdapterFieldMap'},
            'class_map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.Virtual2RealAdapterClassMap']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'real_field_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'virtual_field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.VirtualFeild']"})
        },
        u'vir2real.virtualclass': {
            'Meta': {'object_name': 'VirtualClass'},
            'discription': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'vir2real.virtualdata': {
            'Meta': {'object_name': 'VirtualData'},
            'can_be_restore_real': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_adapter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.DataAdapter']"}),
            'erro_msg': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matching_objects': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'matching_objects_count': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'quick_job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.QuickAddJob']", 'null': 'True', 'blank': 'True'}),
            'source_json': ('django.db.models.fields.TextField', [], {}),
            'source_line': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        },
        u'vir2real.virtualfeild': {
            'Meta': {'object_name': 'VirtualFeild'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pclass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vir2real.VirtualClass']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'TYPE_CHAR'", 'max_length': '50'})
        }
    }

    complete_apps = ['vir2real']