# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'products_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'products', ['Category'])

        # Adding model 'Color'
        db.create_table(u'products_color', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'products', ['Color'])

        # Adding model 'Style'
        db.create_table(u'products_style', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'products', ['Style'])

        # Adding model 'Product'
        db.create_table(u'products_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('picture2', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('best_seller', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('index_picture', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'products', ['Product'])

        # Adding M2M table for field color on 'Product'
        m2m_table_name = db.shorten_name(u'products_product_color')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False)),
            ('color', models.ForeignKey(orm[u'products.color'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'color_id'])

        # Adding M2M table for field style on 'Product'
        m2m_table_name = db.shorten_name(u'products_product_style')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False)),
            ('style', models.ForeignKey(orm[u'products.style'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'style_id'])

        # Adding model 'EmailSignup'
        db.create_table(u'products_emailsignup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'products', ['EmailSignup'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'products_category')

        # Deleting model 'Color'
        db.delete_table(u'products_color')

        # Deleting model 'Style'
        db.delete_table(u'products_style')

        # Deleting model 'Product'
        db.delete_table(u'products_product')

        # Removing M2M table for field color on 'Product'
        db.delete_table(db.shorten_name(u'products_product_color'))

        # Removing M2M table for field style on 'Product'
        db.delete_table(db.shorten_name(u'products_product_style'))

        # Deleting model 'EmailSignup'
        db.delete_table(u'products_emailsignup')


    models = {
        u'products.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'products.color': {
            'Meta': {'ordering': "['name']", 'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'products.emailsignup': {
            'Meta': {'ordering': "['email']", 'object_name': 'EmailSignup'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'products.product': {
            'Meta': {'ordering': "['category', 'name']", 'object_name': 'Product'},
            'best_seller': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Category']"}),
            'color': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Color']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_picture': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'picture2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'style': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Style']", 'symmetrical': 'False'})
        },
        u'products.style': {
            'Meta': {'ordering': "['name']", 'object_name': 'Style'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['products']